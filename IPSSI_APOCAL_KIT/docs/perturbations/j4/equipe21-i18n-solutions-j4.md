# Solutions d'internationalisation (i18n) — EduTutor IA

**Document :** equipe21-i18n-solutions-j4.md

**Projet :** EduTutor IA

**Équipe :** Groupe 21

**Version :** v1.0

**Date :** 02/07/2026

**Statut :** Livrable J4 — Passage à l'échelle (axe i18n)

---

## 1. Objectif du document

La perturbation J4 (adoption nationale + levée de fonds → internationalisation)
impose deux questions distinctes de la Direction :

1. **Comment change-t-on la langue du site ?** → i18n de l'**interface** (textes statiques, dates, formats).
2. **Comment les outils IA répondent-ils dans la langue de l'élève, à la volée ?** → i18n du **contenu généré par le LLM**.

Ce document cadre les deux, propose des choix techniques justifiés sur la stack
existante (React Vite + Django + Llama 3.1 8B / Ollama), et relie chaque solution
aux user stories du backlog v3.0.

Persona de référence : **Lucia Martínez** (lycéenne à Séville, malvoyante, révise
en espagnol) — voir `Cadrage/persona-lucia.md`.

---

## 2. Périmètre : deux problèmes à ne pas confondre

| Dimension | Ce qui est traduit | Nature | User stories |
|---|---|---|---|
| **i18n interface (statique)** | Menus, boutons, labels, messages d'erreur, emails | Textes finis, connus à l'avance, traduits une fois | US-32 |
| **i18n contenu IA (dynamique)** | Questions/QCM générés depuis un cours | Texte infini, généré à la volée par le LLM | US-32, US-33 |
| **Sécurité multilingue** | Robustesse des garde-fous prompt injection | Transverse | US-35 |

> ⚠️ Erreur classique : croire qu'un seul mécanisme couvre les deux. L'interface se
> traduit avec un **fichier de langue** ; le contenu IA se pilote avec un **paramètre
> de langue passé au LLM**.

---

## 3. Axe A — Internationalisation de l'interface (bascule de langue du site)

### 3.1 Principe

Externaliser **tous** les textes de l'interface dans des fichiers de langue
(`fr.json`, `es.json`, `en.json`…), et remplacer les chaînes en dur par des clés.
La langue devient un paramètre de l'application, choisi par l'utilisateur et
persisté (préférence compte + `localStorage`).

### 3.2 Choix technique — Frontend (React Vite)

- **Bibliothèque : `react-i18next` + `i18next`** (standard de l'écosystème React, mature, SSR-compatible).
- **Détection initiale : `i18next-browser-languagedetector`** (ordre : préférence compte → `localStorage` → en-tête `navigator.language` → fallback `fr`).
- **Format des fichiers de langue :** JSON par langue, un namespace par domaine (`common`, `quiz`, `auth`, `errors`).

```
frontend/src/locales/
  fr/common.json
  es/common.json
  en/common.json
```

```jsonc
// es/common.json
{
  "quiz.generate": "Generar un cuestionario",
  "quiz.score": "Tu puntuación : {{score}}/10"
}
```

```jsx
// Avant : <button>Générer un quiz</button>
// Après :
const { t } = useTranslation();
<button>{t('quiz.generate')}</button>
```

### 3.3 Choix technique — Backend (Django)

- Django fournit **`gettext` / `django.utils.translation`** en natif (fichiers `.po`/`.mo`) : à utiliser pour les textes serveur (emails, messages d'API, admin). Pas de dépendance à ajouter.
- Négociation de langue via l'en-tête HTTP `Accept-Language` + `LocaleMiddleware`, ou paramètre explicite envoyé par le front.

> **Ponytail :** on ne réinvente rien — `react-i18next` côté front, `gettext` natif
> côté Django. Deux briques standard, zéro composant maison.

### 3.4 Points de vigilance

- **Formats locaux** : dates, nombres, pluriels → délégués à `i18next` (ICU) et à `Intl` natif du navigateur.
- **Sens de lecture (RTL)** : hors périmètre v1 (langues cibles FR/ES/EN LTR) ; à prévoir si arabe/hébreu (attribut `dir`).
- **Lien avec l'accessibilité (RGAA)** : l'attribut `lang` de `<html>` doit suivre la langue active (lecteur d'écran de Lucia → bonne voix/prononciation). Recouvre l'axe a11y.

---

## 4. Axe B — Langue du LLM à la volée (contenu généré)

### 4.1 Principe

La langue de génération est un **paramètre d'entrée** de l'appel LLM, indépendant
de la langue du cours source. Le cours de Lucia est en espagnol → le quiz doit
sortir en espagnol.

### 4.2 Mécanisme retenu — instruction de langue dans le prompt

Sur la stack imposée (Llama 3.1 8B via Ollama), le levier le plus simple et sans
nouvelle dépendance est l'**injection de la langue cible dans le prompt système** :

```python
LANG_LABELS = {"fr": "français", "es": "espagnol", "en": "anglais", "de": "allemand"}

def build_prompt(course_text: str, lang: str) -> str:
    label = LANG_LABELS.get(lang, "français")  # fallback fr
    return (
        f"Tu es un générateur de QCM. Réponds STRICTEMENT en {label}.\n"
        f"Génère 10 QCM à partir du cours suivant, quelle que soit la langue du cours.\n\n"
        f"{course_text}"
    )
```

- La langue par défaut suit la langue d'interface (§3.2), surchargeable par l'élève.
- Le **schéma de sortie reste inchangé** (validation post-LLM US-22 réutilisée) : seule la langue du texte change, pas la structure.

### 4.3 Qualité variable selon la langue → transparence (US-33)

Llama 3.1 8B est plus faible sur certaines langues que sur l'anglais/français. On
ne masque pas ce risque, on l'affiche :

- Langues **validées** (qualité mesurée sur un jeu de test) : FR, EN, ES.
- Langues **expérimentales** : bandeau UX « qualité expérimentale » (US-33).
- Fallback qualité : si file d'attente LLM saturée, bascule fournisseur de secours **Mistral** (US-31) — voir matrice de risques.

### 4.4 Alternatives étudiées

| Option | Décision | Raison |
|---|---|---|
| Instruction de langue dans le prompt | ✅ Retenue | Aucune dépendance, réutilise l'appel Ollama existant, réversible |
| Modèle multilingue dédié par langue | ❌ Rejetée v1 | Coût mémoire (16 Go), multiplie les modèles à maintenir |
| Traduction automatique post-génération (API externe) | ❌ Rejetée v1 | Dépendance externe + RGPD (données sortent de l'UE) + double latence |
| Fine-tuning multilingue | ❌ Rejetée | Hors budget/temps, non nécessaire pour le besoin de base |

---

## 5. Traçabilité backlog (v3.0)

| US | Axe | MoSCoW | SP | Sprint |
|---|---|---|---|---|
| US-32 | i18n interface + langue LLM à la volée | MUST | 13 | R3 / S10 |
| US-33 | Avertissement « qualité expérimentale » par langue | SHOULD | 3 | R3 / S10 |
| US-35 | Tests adversariaux multilingues (EN/ES/DE) | COULD | 3 | R3 / S11 |

Épic porteuse : **EP-08 — Scalabilité, Accessibilité & i18n**.

---

## 6. Bonus technique — PoC proposé (1 axe, si le temps le permet)

Le PoC le moins coûteux et le plus démontrable : **paramètre de langue du LLM à la
volée** (§4.2). Un seul point de code (`build_prompt`), aucune dépendance, démo
immédiate : même cours → quiz FR puis quiz ES.

```python
# ponytail: PoC minimal — 3 lignes suffisent à prouver l'axe i18n LLM
assert "espagnol" in build_prompt("Le théorème de Pythagore...", "es")
assert "français" in build_prompt("...", "xx")  # langue inconnue -> fallback fr
```

---

## 7. Risques associés (extraits de la matrice J4)

| Risque | Prob. × Impact | Action préventive | Story |
|---|---|---|---|
| Qualité LLM médiocre dans une langue peu couverte | Moyen × Fort | Bandeau transparence + liste de langues validées | US-33 |
| Injection de prompt via un cours en langue étrangère contournant les garde-fous | Moyen × Fort | Tests adversariaux multilingues en CI | US-35 |
| Saturation LLM sous charge internationale | Fort × Fort | Fallback Mistral | US-31 |
| Textes non externalisés oubliés (chaînes en dur) | Fort × Moyen | Lint i18n (clé manquante = build rouge) | US-32 |

---

## 8. Révision

Ce document est revu à chaque release majeure de la Release 3 (i18n) et après
ajout de toute nouvelle langue cible.

Version actuelle : **v1.0 — 02/07/2026**
