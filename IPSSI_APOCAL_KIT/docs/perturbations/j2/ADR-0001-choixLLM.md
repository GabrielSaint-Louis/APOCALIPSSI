# ADR-0001 — Choix du modèle LLM par défaut pour réduire la latence

> PERTURBATION J2 · ADR TECHNIQUE
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum
> Auteur : Monica RADIFERA · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ          | Valeur                                                 |
| -------------- | ------------------------------------------------------ |
| **Numéro ADR** | ADR-0001                                               |
| **Titre**      | Choix du modèle LLM par défaut pour réduire la latence |
| **Statut**     | ☑ Accepté                                              |
| **Date**       | 30/06/2026 17h15                                       |
| **Auteurs**    | Monica RADIFERA + équipe (decision)                    |
| **Version**    | v1.0                                                   |
| **Supersedes** | Aucun                                                  |

> 💡 Convention : un ADR doit tenir en 1 à 2 pages maximum.

---

## 1. Contexte

### 1.1 Situation actuelle

Le backend d’EduTutor IA exécute les modèles localement via Ollama. Les modèles testés sont Llama 3.1 8B, Mistral 7B et Phi-3 mini. Le cas d’usage concerné est la génération de 10 QCM à partir d’un cours fourni par l’utilisateur. La contrainte projet impose une exécution locale, sans API externe, avec maintien de la conformité RGPD.

### 1.2 Problème observé

Le benchmark local montre que les temps de génération sont trop élevés pour l’expérience utilisateur cible. Le retour terrain signale un temps d’attente d’environ 45 secondes pour 10 questions, jugé inutilisable par un étudiant. Les mesures du benchmark confirment un problème de latence d’inférence, particulièrement sensible en environnement CPU standard.

### 1.3 Impact si on ne décide rien

Le produit risque d’être rejeté en démo, abandonné par les étudiants et jugé trop lent par l’enseignante. Le problème est donc d’abord un problème de latence LLM, pas un problème d’interface.

---

## 2. Options envisagées

| Option                 | Avantages                                                         | Inconvénients                                                     | Coût (effort + risque)                                     |
| ---------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| **A. Llama 3.1 8B**    | Bonne référence de qualité                                        | Latence p50 31.75 s, p95 42.65 s, trop élevée                     | Faible effort / risque UX élevé                            |
| **B. Mistral 7B**      | Compromis intermédiaire                                           | Latence p50 26.26 s, p95 37.91 s, qualité moyenne 3/5             | Faible effort / risque moyen                               |
| **C. Phi-3 mini**      | Meilleure latence p50 du benchmark à 21.25 s, qualité moyenne 3/5 | p95 élevé à 66.81 s, risque de lenteur sur certains runs          | Effort faible à moyen / risque qualité et stabilité modéré |
| **D. Ne rien changer** | Aucun effort immédiat                                             | Conserve le problème de latence et le risque de rejet utilisateur | Effort nul / risque élevé                                  |

---

## 3. Décision retenue

**Décision : migrer le modèle LLM par défaut vers Phi-3 mini, sous Ollama.**

### 3.1 Justification

Phi-3 mini est l’option la plus rapide du benchmark sur la médiane, avec un p50 à 21.25 s, devant Mistral 7B (26.26 s) et Llama 3.1 8B (31.75 s). Sa qualité subjective moyenne est de 3/5, équivalente à Mistral et supérieure à Llama 3.1 8B (2.67/5). Même si son p95 reste élevé, c’est le meilleur compromis mesuré pour réduire la latence dans les contraintes actuelles du projet.

### 3.2 Critères de choix

- Latence p50 : prioritaire.
- Latence p95 : à surveiller.
- Qualité moyenne : doit rester acceptable pour des QCM.
- Intégration dans Ollama : obligatoire.
- Stabilité en production : requise.

## 4. Conséquences

### 4.1 Conséquences positives

- Réduction de la latence médiane par rapport aux deux autres modèles.
- Expérience utilisateur moins frustrante.
- Meilleure compatibilité avec une machine peu puissante.
- Démo produit plus défendable face au sponsor.

### 4.2 Conséquences négatives

- Le p95 reste élevé, donc certaines générations resteront lentes.
- Besoin possible d’ajuster le prompt et la validation de sortie.
- Risque de régression sur certains cas complexes.
- Une future re-migration peut rester nécessaire si un meilleur compromis apparaît.

### 4.3 Mesures de mitigation

- Rollback rapide possible via variable d’environnement.
- Validation stricte du JSON généré.
- Audit qualité hebdomadaire sur un échantillon de quiz.
- Révision de l’ADR si un meilleur compromis apparaît.

---

## 5. À surveiller

| KPI                     | Seuil cible | Seuil d’alerte | Action si dépassement               |
| ----------------------- | ----------- | -------------- | ----------------------------------- |
| Latence p50             | < 25 s      | > 30 s         | Réévaluer le modèle                 |
| Latence p95             | < 40 s      | > 60 s         | Auditer l’inférence Ollama          |
| Score qualité moyen     | ≥ 3/5       | < 2.5/5        | Ajuster prompt ou changer de modèle |
| Taux d’erreur factuelle | < 5 %       | > 10 %         | Corriger la validation post-LLM     |
| Taux de rollback        | < 5 %       | > 10 %         | Réouvrir un ADR                     |

---

## 6. Revue de la décision

**Date de revue prévue :** 2 semaines après mise en production.

Si les seuils d’alerte sont dépassés, un nouvel ADR devra être créé pour remplacer celui-ci.

---

## ✅ Grille d'auto-évaluation

| Critère qualité                                                         | Auto-évaluation | Commentaire / preuve                           |
| ----------------------------------------------------------------------- | --------------- | ---------------------------------------------- |
| L'ADR a un numéro unique (ADR-XXXX) et un statut explicite              | ✅ Oui          | ADR-0001, statut Accepté                       |
| Le contexte décrit la situation factuelle avec des chiffres mesurés     | ✅ Oui          | Benchmark local et retour terrain intégrés     |
| Au moins 3 options sont listées, incluant « ne rien faire »             | ✅ Oui          | Llama 3.1, Mistral 7B, Phi-3 mini, statu quo   |
| La décision retenue est annoncée clairement                             | ✅ Oui          | Migration vers Phi-3 mini                      |
| La justification du choix s’appuie sur le contexte                      | ✅ Oui          | Latence prioritaire, contraintes locales       |
| Les mesures de mitigation sont listées explicitement                    | ✅ Oui          | Rollback, validation JSON, audit, révision ADR |
| Les conséquences positives et négatives sont chiffrées                  | ☐ Partiel       | Chiffrage limité au benchmark disponible       |
| Au moins 3 KPIs sont définis avec seuil cible + seuil d’alerte + action | ✅ Oui          | 5 KPIs définis                                 |
| Une date de revue de l’ADR est fixée                                    | ✅ Oui          | 2 semaines après mise en production            |
| L’ADR tient en 1 à 2 pages                                              | ✅ Oui          | Format court respecté                          |

---

## 📚 Références

- Michael Nygard, _Documenting Architecture Decisions_.
- ADR GitHub, collection de modèles et exemples.
- ThoughtWorks Tech Radar, Lightweight ADRs.
- Cours Agile/Scrum (Mohamed EL AFRIT).
