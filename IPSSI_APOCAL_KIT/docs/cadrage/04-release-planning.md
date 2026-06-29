# Release Planning - EduTutor IA
> CADRAGE MATINAL · ARTEFACT 5 SUR 7
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum
> Auteur du modèle : Mohamed Amine EL AFRIT · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|---|---|
| **Équipe n°** | 21 |
| **Membres** | Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS |
| **Sprint concerné** | Cadrage |
| **Version** | v1.0 (initiale) |
| **Date de remise** | 29/06/2026 avant 13h00 |
| **Statut** | Draft |

> Convention de nommage : `equipe-21-release-planning-v1.0.md`

---

## PRÉAMBULE - Pourquoi cet artefact ?

Le Release Planning donne la vue d'ensemble de la semaine : pour chaque sprint demi-journée, un objectif clair et démontrable, la capacité réaliste de l'équipe, la vélocité cible et les user stories engagées (taguées US-XX pour la traçabilité avec le Product Backlog). Il positionne les 2 releases (MVP fin Sprint 5, Release 2 fin Sprint 7).

> Traçabilité : les tags US-01 à US-06 correspondent aux features F1 à F6 du [Product Backlog](03-product-backlog.md) et du [Product Vision Board](01-product-vision-board.md). Les stories US-07+ relèvent de la Release 2.

---

## 1. Release Planning - Semaine APOCAL'IPSSI 2026

**7 sprints × demi-journée + cadrage matinal + soutenance vendredi · équipe de 6 personnes**

| Sprint | Jour | Horaires | Capacité (h-pers) | Vélocité cible (SP) | Objectif sprint | Stories engagées | Release / Jalon |
|---|---|---|---|---|---|---|---|
| **Cadrage** | Lundi matin | 9h00 – 13h30 | 21 | n.c. | Produire les 7 artefacts agiles (Vision, Personas, Customer Journey, Story Map, Release Planning, Product Backlog, Sprint Backlog) | n.c. | Validation PO 14h00 |
| **Sprint 1** | Lundi PM | 14h00 – 18h00 | 24 | 8 | Setup technique + démarrage MVP (F1 inscription, F2 upload cours) | US-01, US-02 | Sprint Review 18h |
| **Sprint 2** | Mardi matin | 9h00 – 12h30 | 21 | 8 | Génération quiz F3 (Llama 3.1 8B via Ollama local) | US-03 | Sprint Review 12h30 |
| **Sprint 3** | Mardi PM | 14h00 – 18h00 | 24 | 5 | Correction + scoring F4/F5 | US-04, US-05 | Sprint Review 18h |
| **Sprint 4** | Mercredi matin | 9h00 – 12h30 | 21 | 5 | Historique F6 + finitions UI MVP | US-06 | Sprint Review 12h30 |
| **Sprint 5** | Mercredi PM | 14h00 – 18h00 | 24 | 6 | Finalisation MVP F1-F6 + correctifs + tests | Correctifs F1-F6 | **Release 1 (MVP) 17h45** |
| **Sprint 6** | Jeudi matin | 9h00 – 12h30 | 21 | 8 | Stories Release 2 (2-3 pistes choisies) | US-07, US-09 | Sprint Review 12h30 |
| **Sprint 7** | Jeudi PM | 14h00 – 17h00 | 18 | 6 | Finalisation Release 2 + démo prête | US-10 | **Release 2 17h** |
| **Soutenance** | Vendredi | Selon planning | n.c. | n.c. | Pitch (15 min) + démo live MVP + Release 2 + Q/R jury | n.c. | Soutenance + délibération |
| **TOTAL semaine** | | | **174** | **~42 SP** | | | |

> **Capacité totale = 174 h-pers** (équipe de 6 personnes : Nicolas, Celia, Monica, Nolan, Ilham, Gabriel). Capacité par sprint recalculée à 6 × durée du sprint.

### Légende

| Symbole | Signification |
|---|---|
| **Sprint Review** | Démo des stories à la fin du sprint + validation PO |
| **Release** | Livraison incrément potentiellement déployable (tag Git + démo enregistrable) |
| **Soutenance** | Pitch + démo + retour réflexif + Q/R jury (vendredi) |

---

## 2. Détail des user stories engagées

### Release 1 - MVP (Sprints 1 à 5)

| ID | Feature | Story | SP |
|---|---|---|---|
| **US-01** | F1 | Inscription / connexion email + reset mot de passe | 3 |
| **US-02** | F2 | Upload PDF ≤ 5 Mo ou saisie texte ≥ 200 caractères | 5 |
| **US-03** | F3 | Génération automatique de 10 QCM via Llama 3.1 8B (Ollama local) | 8 |
| **US-04** | F4 | Soumission + correction automatique (1 bonne réponse / QCM) | 3 |
| **US-05** | F5 | Score /10 + détail bonnes / mauvaises réponses | 2 |
| **US-06** | F6 | Historique persistant des quiz par utilisateur | 3 |
| **Total Release 1** | | | **24 SP** |

### Release 2 - Should / Could (Sprints 6 à 7)

| ID | Niveau | Story | SP |
|---|---|---|---|
| **US-07** | SHOULD | Dashboard de progression par chapitre / cours | 5 |
| **US-09** | COULD | Bouton « Signaler une erreur », feedback utilisateur | 3 |
| **US-10** | COULD | Suppression compte + données (RGPD Art. 17, droit à l'oubli) | 3 |
| **Total Release 2** | | | **11 SP** |

> **Scope initial ≈ 42 SP** = 35 SP de stories nommées (Release 1 : 24 + Release 2 : 11) + ~7 SP de travail non itemisé en stories (setup technique, tests pytest/Vitest, finitions).

---

## 3. Burnup global - Semaine APOCAL'IPSSI 2026

Trajectoire des story points livrés (cumulés) vs scope total sur les 7 sprints.

| Sprint | Fin de sprint | SP livrés (idéal) | SP livrés (réel) | Scope total |
|---|---|---|---|---|
| Sprint 0 | Lun 13h30 | 0 | _[à compléter]_ | 42 (scope initial) |
| Sprint 1 | Lun 18h | 6 | _[à compléter]_ | 42 |
| Sprint 2 | Mar 12h30 | 12 | _[à compléter]_ | 42 |
| Sprint 3 | Mar 18h | 18 | _[à compléter]_ | 42 |
| Sprint 4 | Mer 12h30 | 24 | _[à compléter]_ | 42 |
| Sprint 5 | Mer 18h | 30 | _[à compléter]_ | 42 |
| Sprint 6 | Jeu 12h30 | 36 | _[à compléter]_ | 42 |
| Sprint 7 | Jeu 17h | 42 | _[à compléter]_ | 42 |

> Graphique conseillé : 3 séries (idéal en pointillés, réel en plein, scope en aire). Colonne « réel » à reporter après chaque Sprint Review. Si l'écart réel-idéal se creuse, alerte.

---

## Grille d'auto-évaluation

| Critère qualité | Auto-évaluation | Commentaire / preuve |
|---|---|---|
| Les 7 sprints sont planifiés avec jour, horaires et capacité (h-pers) chiffrée | Oui | Section 1 : 9 lignes Cadrage + 7 sprints + Soutenance, capacité par sprint |
| L'équipe taille est explicite (pas de capacité « floue ») | Oui | 6 personnes nommées, capacité totale 174 h-pers |
| Chaque sprint a un objectif clair, mesurable, livrable en démo | Oui | Colonne « Objectif sprint » : features F1-F6 + Release 2 |
| Chaque sprint liste au moins 1 user story engagée (tag US-XX) | Oui | Colonne « Stories engagées » + section 2, tags US-01 à US-10 |
| La Release 1 (MVP) est explicitement positionnée fin Sprint 5 (mercredi 17h45) | Oui | Ligne Sprint 5 : Release 1 (MVP) 17h45 |
| La Release 2 est explicitement positionnée fin Sprint 7 (jeudi 17h) | Oui | Ligne Sprint 7 : Release 2 17h |
| La feuille Burnup global est remplie avec un scope initial chiffré | Oui | Section 3 : scope initial 42 SP, trajectoire idéale 0 à 42 |
| Le Release Planning a été co-construit en équipe (toutes les voix entendues) | Partiel | À valider collectivement avant 13h |

---

## Références

- Cours Agile/Scrum (Mohamed EL AFRIT) : mohamedelafrit.com/teaching/Master_Classe_Agile/cours.html
- Scrum Guide officiel FR : scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-French.pdf
- Artefacts liés : [Vision Board](01-product-vision-board.md) · [Personas](02-personas.md) · [Product Backlog](03-product-backlog.md)
- Site APOCAL'IPSSI : mohamedelafrit.com/teaching/APOCALIPSSI
