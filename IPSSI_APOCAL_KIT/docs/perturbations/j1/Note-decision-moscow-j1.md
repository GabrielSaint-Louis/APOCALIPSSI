# Note de décision — Intégration cible enseignante (Perturbation J1)

> Équipe : Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS 
> Date : 29/06/2026 — 14h00  
> Version : v1.0  
> Statut : En revue PO

---

## Contexte de la décision

À 14h00 le lundi 29/06, le sponsor signale l'intérêt de **Mme Sophie Lefèvre**, 42 ans, enseignante BTS Communication à Lyon (28 étudiants), pour EduTutor IA. Il demande d'intégrer cette cible secondaire dans le cadrage et de trancher son périmètre pour la Release 1.

La question posée à l'équipe : **la cible enseignante est-elle MUST, SHOULD ou COULD pour la Release 1 ?**

---

## Analyse de l'impact

### Chevauchement avec le MVP étudiant existant

Plusieurs features du MVP étudiant (F1–F6) servent **directement** Mme Lefèvre sans modification :

| Feature | Réutilisable pour Mme Lefèvre | Commentaire |
|---|---|---|
| F1 · Auth email | ✅ Oui | Même mécanisme de compte |
| F2 · Upload PDF/texte | ✅ Oui | Elle uploade ses cours BTS |
| F3 · Génération 10 QCM | ✅ Oui | Elle génère des quiz pour ses étudiants |
| F4 · Correction automatique | ✅ Oui | Identique |
| F5 · Score + détail réponses | ✅ Partiel | Elle veut voir les scores de ses 28 étudiants, pas seulement le sien |
| F6 · Historique par utilisateur | ⚠️ Partiel | Elle veut un historique **par classe**, pas seulement individuel |

### Nouvelles stories spécifiques enseignant

Les besoins propres à Mme Lefèvre génèrent **5 nouvelles user stories** :

| ID | User Story | SP estimés | MoSCoW |
|---|---|---|---|
| US-E1 | En tant qu'enseignante, je veux voir les scores de tous mes étudiants sur un quiz afin d'identifier ceux qui décrochent | 5 | SHOULD |
| US-E2 | En tant qu'enseignante, je veux exporter les résultats d'un quiz en CSV afin de les intégrer dans mon suivi Pronote | 3 | COULD |
| US-E3 | En tant qu'enseignante, je veux envoyer un message de conseil à un étudiant depuis l'app afin de l'accompagner | 8 | COULD |
| US-E4 | En tant qu'enseignante, je veux créer un quiz partageable par lien afin que mes 28 étudiants le passent depuis leur smartphone | 8 | SHOULD |
| US-E5 | En tant qu'enseignante, je veux voir un dashboard de progression par étudiant afin de repérer les lacunes communes | 5 | COULD |

**Total nouvelles stories enseignant : 29 SP**

---

## Capacité disponible Release 1

| Sprint | Capacité (h-pers) | Vélocité cible (SP) |
|---|---|---|
| S1 (Lun PM) | 28 | 8-10 |
| S2 (Mar matin) | 24.5 | 8-10 |
| S3 (Mar PM) | 28 | 10 |
| S4 (Mer matin) | 24.5 | 8-10 |
| S5 (Mer PM) | 28 | 8-10 |
| **TOTAL R1** | **133** | **~44-50 SP** |

Scope MVP étudiant F1–F6 : **~25 SP** (US-01 à US-06)  
Marge disponible après MVP : **~19-25 SP**  
Coût stories enseignant prioritaires (US-E1 + US-E4) : **13 SP**

---

## Décision

### ✅ Cible enseignante : **MUST pour la Release 1**

**Justification :**

1. **Effort raisonnable** : les 2 stories les plus critiques (US-E1 dashboard scores + US-E4 quiz partageable) totalisent 13 SP, absorbables dans la marge disponible après MVP étudiant (~19-25 SP).

2. **Chevauchement favorable** : F1, F2, F3, F4 du MVP étudiant sont réutilisables sans modification. L'effort marginal est donc inférieur à un développement from scratch.

3. **Valeur stratégique forte** : Mme Lefèvre représente la cible B2B enseignant, levier d'acquisition institutionnelle (établissements scolaires). La négliger en Release 1 reviendrait à manquer une opportunité de différenciation face aux concurrents (Wilgo, Quizlet) qui sont étudiant-first.

4. **Risque maîtrisé** : en classant la cible en MUST (pas SHOULD), l'équipe préserve la priorité absolue du MVP étudiant F1–F6. Si la capacité manque en S4/S5, les stories enseignant sont sacrifiées sans mettre en péril la Release 1.

### Ce qui est sacrifié si capacité insuffisante

Si l'équipe manque de temps en S4/S5, les stories reportées en Release 2 sont, dans cet ordre :

1. US-E3 (messagerie conseil) — 8 SP, effort élevé, valeur indirecte
2. US-E5 (dashboard progression détaillé) — 5 SP, base déjà fournie dans le kit
3. US-E2 (export CSV Pronote) — 3 SP, utile mais non bloquant

### Ce qui est **non négociable**

Les 6 features F1–F6 du MVP étudiant restent **MUST** et ne peuvent pas être sacrifiées au profit des stories enseignant. Le MVP étudiant est la condition sine qua non de la Release 1.

---

## Artefacts mis à jour suite à cette décision

| Artefact | Action | Version |
|---|---|---|
| Personas | Ajout Mme Lefèvre (6 dimensions) | v1.1 |
| Customer Journey Map | Ajout parcours Mme Lefèvre (5 étapes) | v1.1 |
| Story Map | Ajout stories US-E1 à US-E5 en ligne SHOULD/COULD | v1.1 |
| Product Backlog | Ajout US-E1 à US-E5 avec INVEST + MoSCoW | v1.1 |
| Sprint Backlog S1 | Inchangé (stories enseignant à partir de S4) | v1.0 |

---

## Validation PO requise

> ☐ Approuvé tel quel  
> ☐ Approuvé avec modifications (voir commentaire)  
> ☐ Refusé — retour à l'équipe
>
> Commentaire PO : _______________________________________________  
> Signature PO : ___________________ Date : ___________________
