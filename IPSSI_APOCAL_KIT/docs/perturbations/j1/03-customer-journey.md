# Customer Journey Maps — EduTutor IA

> CADRAGE MATINAL · ARTEFACT 3 SUR 7
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum
> Auteur : Monica RADIFERA RASAMOELIJAONA · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ               | Valeur                                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Équipe n°**       | 21                                                                                                                |
| **Membres**         | Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS |
| **Sprint concerné** | Cadrage                                                                                                           |
| **Version**         | v1.1 (révision PO)                                                                                                |
| **Date de remise**  | 29/06/2026 avant 13h00                                                                                            |
| **Statut**          | En revue PO                                                                                                       |

> 💡 Convention de nommage : `equipe-21-customer-journey-v1.1.md`

---

## PRÉAMBULE — Pourquoi cet artefact ?

Le Customer Journey Map raconte le parcours d'une persona étape par étape. À chaque étape, on note ses actions concrètes, ses pensées (formulées au « je »), son émotion dominante (échelle 😟 → 😐 → 😊), et les frictions ou opportunités produit.

Le journey map sert à repérer le moment exact où la persona décroche — c'est là que le produit doit briller en priorité.

Ce document contient **3 parcours** :

- **Camille Martin** (étudiante, cible primaire)
- **Mme Sophie Lefèvre** (enseignante, cible primaire intégrée dès le cadrage et la Release 1 sur demande)
- **M. David Chen** (directeur d'établissement, cible secondaire B2B)

> 💡 Le parcours « Établissement » suit un cycle d'achat B2B et non un parcours utilisateur classique. Les 5 étapes sont adaptées en conséquence.

---

## 1. Parcours Étudiant — Camille Martin (cible primaire)

> **Rappel persona** : Camille, 21 ans, étudiante L3 Droit à Paris II Panthéon-Assas. Boursière échelon 3. Révise ~8h/semaine dont ~3h perdues à chercher des fiches. Partiels dans 3 semaines. Utilise ChatGPT de manière irrégulière, méfiance sur la fiabilité. Allergique aux installations complexes.

**Objectif du parcours** : Décrire comment Camille découvre, utilise et adopte (ou abandonne) EduTutor IA. Repérer le moment de décrochage potentiel.

**Format** : 5 étapes — Découverte → Inscription → 1ʳᵉ utilisation → Usage régulier → Recommandation.

### 1.1. Tableau de parcours

| Étape                  | Actions                                                                                                                                            | Pensées (au « je »)                                                                                                                                  | Émotion                   | Frictions / Opportunités                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Découverte**      | Voit une story Instagram d'une influenceuse étudiante mentionnant EduTutor IA. Clique sur le lien dans sa bio.                                     | _« Encore un outil IA qui promet la lune ? Mais bon, je révise pour mon partiel dans 2 semaines, ça vaut le coup d'essayer. »_                       | 😐 Curieuse, sceptique    | **Friction** : landing page trop technique, peu de preuve sociale. **Opportunité** : témoignages d'étudiants réels, mention explicite « gratuit, RGPD, aucune installation ».             |
| **2. Inscription**     | Crée un compte avec son email universitaire. Génère un mot de passe via Bitwarden. Valide le lien de confirmation reçu en 2 min.                   | _« Au moins ils ne demandent pas mon numéro de téléphone. RGPD respecté ? J'espère qu'ils ne vendent pas mes données. »_                             | 😐 Vigilante              | **Friction** : pas de SSO Google/Apple — saisie manuelle laborieuse sur smartphone. **Opportunité** : mention RGPD et « données hébergées localement » visible dès la page d'inscription. |
| **3. 1ʳᵉ utilisation** | Uploade son PDF de droit constitutionnel (340 pages). Sélectionne le chapitre 4. Génère un quiz de 10 QCM. Attend ~45 secondes sans retour visuel. | _« 340 pages, j'espère que ça va pas planter. Je vois pas la barre de progression... C'est long 45 secondes quand on sait pas ce qui se passe. »_    | 😟 Anxieuse → 😊 Soulagée | **Friction** : absence d'indicateur de progression pendant la génération (> 30 s). **Opportunité** : barre de progression + message rassurant (« Analyse du chapitre en cours... »).      |
| **4. Usage régulier**  | Génère 3 quiz / semaine sur 5 chapitres différents pendant 2 semaines avant les partiels. Consulte son historique de scores.                       | _« J'ai gagné au moins 2h/semaine. Je me sens bien plus prête. Mais j'aimerais réviser dans le RER sans connexion. »_                                | 😊 Confiante, satisfaite  | **Friction** : historique non consultable hors-ligne — pas de mode offline. **Opportunité** : mode hors-ligne pour les trajets RER (besoin identifié dans le profil persona).             |
| **5. Recommandation**  | Partage le lien à 3 amies de promo dans son groupe WhatsApp. Leur propose de faire des sessions de révision communes.                              | _« Si ça les aide aussi, on pourra faire des sessions de révision ensemble. Dommage qu'on puisse pas partager directement un quiz depuis l'appli. »_ | 😊 Enthousiaste           | **Friction** : pas de fonctionnalité de partage de quiz entre comptes. **Opportunité** : mode équipe / promo — lien de partage direct pour un quiz généré.                                |

### 1.2. Moment de décrochage potentiel

> **Étape 3 — 1ʳᵉ utilisation** : si la génération échoue silencieusement ou dépasse 60 secondes sans retour visuel, Camille referme l'onglet et ne revient pas. Seuil de tolérance identifié dans les critères de succès persona : _« Si ça plante 1 fois en bibliothèque devant mes amies, je n'y reviens jamais. »_

**Investissement produit prioritaire** : indicateur de progression visible dès le lancement de la génération + message rassurant contextualisé (ex. : _« Analyse de vos 340 pages en cours... »_).

---

## 2. Parcours Enseignant — Mme Sophie Lefèvre (cible primaire intégrée Release 1)

> **Rappel persona** : Sophie Lefèvre, 42 ans, professeure de Communication BTS, lycée privé sous contrat à Lyon 6e. 28 étudiants. Crée manuellement ~3 quiz/semaine (90 min chacun). DPO de l'établissement a bloqué ChatGPT. Exige des engagements RGPD écrits. Power user Word/Excel, allergique au CLI. Le PO demande explicitement de l'intégrer dès le cadrage et dans la Release 1.

**Objectif du parcours** : Décrire comment Mme Lefèvre découvre, évalue et adopte EduTutor IA dans un contexte professionnel contraint (conformité RGPD, 28 étudiants à charge, direction à convaincre, suivi de progression des étudiants).

**Format** : 5 étapes — Découverte → Inscription → 1ʳᵉ utilisation → Usage régulier → Recommandation à la direction.

### 2.1. Tableau de parcours

| Étape                                | Actions                                                                                                                                                                                                             | Pensées (au « je »)                                                                                                                                                                                              | Émotion                   | Frictions / Opportunités                                                                                                                                                                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Découverte**                    | Lit un article du Café Pédagogique sur les outils IA pour enseignants. Note le nom EduTutor IA. Cherche une démo vidéo sur YouTube.                                                                                 | _« Encore une promesse marketing ? Je veux des exemples concrets sur un cours BTS Communication, pas des captures génériques. »_                                                                                 | 😐 Curieuse, prudente     | **Friction** : absence d'exemples sectoriels (BTS, lycée, supérieur) sur la landing page. **Opportunité** : démos par niveau scolaire et par discipline.                                                                                |
| **2. Inscription**                   | Tente de créer un compte enseignant via le site. Ne trouve pas de formulaire dédié, envoie un email de contact. Attend 24 h une réponse.                                                                            | _« 24 h pour répondre en 2026 ? Si le SAV amont est aussi lent, comment sera-t-il quand j'aurai 28 étudiants bloqués en cours ? »_                                                                               | 😟 Impatiente, méfiante   | **Friction** : pas d'auto-inscription enseignant — dépendance à un process manuel (décrochage fort). **Opportunité** : compte enseignant gratuit auto-créé + onboarding guidé en 5 minutes.                                             |
| **3. 1ʳᵉ utilisation**               | Uploade un cours de Communication non-verbale (45 pages). Génère 1 quiz de 10 QCM pour tester avant de l'utiliser en classe. Vérifie chaque question une à une.                                                     | _« Si les questions sont mal formulées ou inventées, je ne peux pas ça donner à mes élèves. Je veux voir les questions AVANT qu'elles soient publiées. »_                                                        | 😐 Vigilante → 😊 Étonnée | **Friction** : pas d'aperçu rapide des questions avant envoi aux élèves. **Opportunité** : mode preview + validation question par question avant publication.                                                                           |
| **4. Usage régulier**                | Génère 3 quiz / semaine pour ses 28 étudiants. Consulte les scores, repère ceux qui décrochent, puis adapte le niveau de difficulté selon les retours de classe. Exporte en PDF pour impression en salle des profs. | _« C'est exactement l'outil qu'il me faut pour suivre la progression de mes 28 étudiants en révision d'examens. Je veux pouvoir voir leurs scores, repérer ceux qui décrochent, et leur envoyer des conseils. »_ | 😊 Satisfaite, productive | **Friction** : pas d'édition manuelle d'une question après génération. **Opportunité** : dashboard de progression, scores, décrocheurs et conseils + éditeur intégré pour correction ciblée d'une question sans re-génération complète. |
| **5. Recommandation à la direction** | Présente l'outil au conseil pédagogique avec un bilan chiffré : 4h/sem économisées, 28 élèves actifs, taux d'erreur < 3%. Demande un budget pour un compte établissement.                                           | _« Je veux prouver le ROI : 4h/sem × 30 sem × 5 profs = 600h/an économisées. Mais j'ai besoin d'un rapport exportable pour le présenter au CA. »_                                                                | 😊 Convaincue             | **Friction** : pas de dashboard de ROI exportable pour la direction. **Opportunité** : rapport mensuel automatique (usage, scores, gains de temps estimés) exportable PDF.                                                              |

### 2.2. Moment de décrochage potentiel

> **Étape 2 — Inscription** : si le délai de réponse dépasse 24 h, Mme Lefèvre ne recontacte pas. Les enseignants ont des emplois du temps contraints ; un blocage à l'entrée est rédhibitoire. Critère de succès persona : _« Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais. »_

**Investissement produit prioritaire** : self-service inscription enseignant + onboarding guidé en 5 minutes max, sans contact humain requis.

### 2.3. Besoin validé par le PO

> **Le PO demande explicitement d'intégrer Mme Sophie Lefèvre dans le cadrage et dans la Release 1, avec un focus sur le suivi de progression des 28 étudiants, l'affichage des scores, la détection des décrocheurs et l'envoi de conseils.**

---

## 3. Parcours Établissement — M. David Chen (cible secondaire B2B)

> **Rappel persona** : David Chen, 51 ans, directeur des études, lycée privé sous contrat, 1 200 élèves, Lyon 6e. Budget edtech ~12 000€/an. Cycle d'achat 6 mois minimum. DPO mutualisé très strict sur le RGPD. A signé 2 outils edtech qui ont fermé en cours d'année — méfiant sur la pérennité. Décide en concertation avec conseil pédagogique, DPO, gestionnaire financier.

**Objectif du parcours** : Décrire le cycle d'achat B2B en 5 étapes, du besoin identifié au renouvellement. Ce n'est pas un parcours utilisateur classique — mettre l'accent sur les contraintes RGPD, budgétaires et de gouvernance.

**Format** : 5 étapes B2B — Découverte du besoin → Évaluation → Décision → Onboarding équipe → Renouvellement.

### 3.1. Tableau de parcours

| Étape                       | Actions                                                                                                                                                                            | Pensées (au « je »)                                                                                                                                | Émotion                   | Frictions / Opportunités                                                                                                                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Découverte du besoin** | Le CA de l'établissement demande une stratégie IA pédagogique pour la rentrée. Mme Lefèvre lui présente EduTutor IA avec son bilan d'usage. Cherche des informations sur le site.  | _« Le CA pousse sur l'IA, mais pas question de signer avec un acteur qui utilise OpenAI ou qui envoie les données hors UE. »_                      | 😟 Prudent, sous pression | **Friction** : pas de garantie RGPD écrite et signée visible dès la page d'accueil. **Opportunité** : fiche RGPD synthétique (1 page) prête à l'emploi, rédigée en langage DPO.                                             |
| **2. Évaluation**           | Envoie les CGV au DPO mutualisé du réseau d'écoles pour validation juridique. Demande une démo live. Compare 3 outils edtech en parallèle (EduTutor, Wilgo, Quizlet Enterprise).   | _« Si le DPO valide les CGV en 30 min de lecture, c'est un signal très positif. Si ça lui prend 2 semaines, le projet meurt avant de commencer. »_ | 😐 Méticuleux, analytique | **Friction** : DPO mutualisé en congés 3 semaines — blocage externe non contrôlable. **Opportunité** : check-list RGPD pré-validée par un cabinet juridique partenaire, réduisant le temps d'analyse DPO.                   |
| **3. Décision**             | Signe le contrat annuel pour 1 200 élèves à 10 €/élève (12 000€ HT/an). Valide les modalités de déploiement avec le DSI mutualisé. Obtient la signature du gestionnaire financier. | _« Si dans 6 mois je dois reculer, ça va être politiquement coûteux. Mieux vaut sécuriser avec une période d'essai avant engagement annuel. »_     | 😐 Engagé, un peu anxieux | **Friction** : pas de clause d'essai de 3 mois avant engagement annuel complet. **Opportunité** : période pilote gratuite ou payante à tarif réduit (3 mois, 1 classe) avant signature annuelle.                            |
| **4. Onboarding équipe**    | Présente l'outil lors d'une réunion pédagogique aux 40 enseignants de l'établissement. Forme un noyau de 5 enseignants ambassadeurs. Distribue les comptes et accès.               | _« Si dès la 1ʳᵉ semaine les profs me disent que ça plante ou que c'est trop compliqué, j'ai perdu l'année entière. »_                             | 😐 Espérant → 😊 Soulagé  | **Friction** : pas de kit de formation clé en main (tutoriels, fiches pratiques, FAQ profs). **Opportunité** : kit de déploiement avec slides de présentation, tutoriels vidéo et FAQ prêts à l'emploi.                     |
| **5. Renouvellement**       | Mesure l'adoption en fin d'année 1 : 35% des profs actifs, 80% des élèves ont utilisé au moins 1 fois. Présente les résultats au CA. Signe le renouvellement annuel.               | _« 35% d'adoption profs, c'est au-dessus du seuil de 30% que je m'étais fixé. Je peux dire au CA qu'on est en avance sur l'IA sans mentir. »_      | 😊 Confiant, fier         | **Friction** : pas de comparaison anonymisée avec d'autres établissements du même réseau. **Opportunité** : benchmark sectoriel (taux d'adoption moyen par type d'établissement) pour valoriser les résultats devant le CA. |

### 3.2. Moment de décrochage potentiel

> **Étape 2 — Évaluation** : si le dossier RGPD n'est pas prêt à l'emploi, le DPO refuse d'instruire le dossier tant que les transferts hors UE ne sont pas garantis par écrit. Le cycle d'achat de 6 mois se transforme en 12 mois, et le projet tombe à la rentrée suivante. Critère de succès persona : _« Si le DPO valide les CGV en 30 min de lecture, c'est un signal positif. »_

**Investissement produit prioritaire** : fiche RGPD pré-rédigée par un cabinet juridique partenaire + clause d'essai de 3 mois pour dérisquer la décision initiale.

---

## 4. Synthèse émotionnelle des 3 parcours

> **Objectif** : Visualiser d'un coup d'œil où les 3 personas vivent leurs pics et creux émotionnels. Permet de prioriser les investissements produit par effet de levier.

| Étape                                  | Camille (étudiante)         | Mme Lefèvre (enseignante)           | M. David Chen (établissement) |
| -------------------------------------- | --------------------------- | ----------------------------------- | ----------------------------- |
| **1. Découverte / Besoin**             | 😐 Curieuse, sceptique      | 😐 Curieuse, prudente               | 😟 Prudent, sous pression     |
| **2. Inscription / Évaluation**        | 😐 Vigilante                | 😟 **Impatiente (décrochage fort)** | 😐 Méticuleux, analytique     |
| **3. 1ʳᵉ utilisation / Décision**      | 😟 → 😊 Anxieuse → Soulagée | 😐 → 😊 Vigilante → Étonnée         | 😐 Engagé, un peu anxieux     |
| **4. Usage régulier / Onboarding**     | 😊 Confiante, satisfaite    | 😊 Satisfaite, productive           | 😐 → 😊 Espérant → Soulagé    |
| **5. Recommandation / Renouvellement** | 😊 Enthousiaste             | 😊 Convaincue, militante            | 😊 Confiant, fier             |

### 4.1. Analyse des points de levier

**L'étape 2 cumule les frictions les plus fortes sur les 3 personas** :

- Camille : vigilante sur les données personnelles → besoin d'une mention RGPD immédiate.
- Mme Lefèvre : impatiente et menacée de décrochage → besoin d'un self-service inscription enseignant.
- M. David Chen : méticuleux et bloqué par son DPO → besoin d'un dossier RGPD prêt à l'emploi.

> 🎯 **Investissement produit maximal** : améliorer l'étape 2 (Inscription / Évaluation) pour les 3 profils simultanément = effet de levier produit le plus fort.

### 4.2. Récapitulatif des investissements produit prioritaires

| Priorité | Parcours concerné     | Investissement recommandé                                           | Étape   |
| -------- | --------------------- | ------------------------------------------------------------------- | ------- |
| 🔴 P0    | Enseignant            | Self-service inscription enseignant + onboarding 5 min              | Étape 2 |
| 🔴 P0    | Enseignant            | Dashboard progression + scores + détection décrocheurs + conseils   | Étape 4 |
| 🔴 P0    | Établissement         | Fiche RGPD pré-rédigée + clause d'essai 3 mois                      | Étape 2 |
| 🟠 P1    | Étudiant              | Indicateur de progression + message rassurant pendant la génération | Étape 3 |
| 🟠 P1    | Enseignant            | Mode preview + validation question par question avant publication   | Étape 3 |
| 🟡 P2    | Étudiant              | Mode hors-ligne pour révision sans connexion (RER)                  | Étape 4 |
| 🟡 P2    | Enseignant            | Éditeur intégré pour corriger une question sans re-génération       | Étape 4 |
| 🟢 P3    | Établissement         | Kit de déploiement clé en main (slides, tutoriels, FAQ)             | Étape 4 |
| 🟢 P3    | Étudiant / Enseignant | Mode partage de quiz + rapport ROI exportable PDF                   | Étape 5 |

---

## ✅ Grille d'auto-évaluation

| Critère qualité                                                                       | Auto-évaluation | Commentaire / preuve                                                                                                     |
| ------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Les 3 parcours sont décrits sur les 5 étapes complètes                                | ✅ Oui          | Camille : Découverte → Recommandation / Lefèvre : Découverte → Recommandation direction / Chen : Besoin → Renouvellement |
| Chaque cellule « Actions » contient une action concrète et observable                 | ✅ Oui          | Ex. : « Uploade son PDF de droit constitutionnel (340 pages) » — observable et testable                                  |
| Chaque cellule « Pensées » est formulée au « je », entre guillemets                   | ✅ Oui          | Toutes les pensées en italique, au « je », entre guillemets doubles                                                      |
| Chaque cellule « Émotion » utilise l'échelle 😟 → 😐 → 😊                             | ✅ Oui          | Au moins 1 transition émotionnelle par parcours                                                                          |
| Chaque cellule « Frictions / Opportunités » identifie ≥ 1 friction ET ≥ 1 opportunité | ✅ Oui          | Toutes les cellules contiennent friction + opportunité distinctes et actionnables                                        |
| Le moment de décrochage est explicitement identifié pour chaque parcours              | ✅ Oui          | Sections 1.2, 2.2, 3.2 : décrochage explicite + investissement prioritaire associé                                       |
| La synthèse émotionnelle identifie le bon point de levier produit                     | ✅ Oui          | Section 4.1 : étape 2 identifiée comme levier maximal avec justification par parcours                                    |
| Le parcours Établissement reflète un cycle d'achat B2B (et pas un usage)              | ✅ Oui          | 5 étapes B2B : Besoin → Évaluation → Décision → Onboarding → Renouvellement                                              |
| Les fonctionnalités référencées correspondent au MVP (F1-F6) du Product Vision Board  | ✅ Oui          | Upload PDF (F2), génération QCM (F3), correction (F4), score (F5), historique (F6) tous présents                         |
| Le document a été relu et validé par le PO                                            | ☐ Partiel       | Révision PO intégrée ; validation finale à confirmer                                                                     |

---

## 📚 Références et conventions

- Cours Agile/Scrum (Mohamed EL AFRIT) : mohamedelafrit.com/teaching/Master_Classe_Agile/cours.html
- Scrum Guide officiel FR : scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-French.pdf
- Site APOCAL'IPSSI : mohamedelafrit.com/teaching/APOCALIPSSI
- Nielsen Norman Group, Customer Journey Maps guide : https://www.nngroup.com/articles/customer-journey-mapping/
- Smaply, Journey Mapping toolkit : https://www.smaply.com/journey-mapping
- Roman Pichler, Customer journey vs Product journey : https://www.romanpichler.com/blog/persona-template-product-managers/
- Article, AARRR framework pour produits : https://www.product-frameworks.com/AARRR-Framework.html

### Convention de versionnement

- `v1.1` — révision après retour PO
- `v1.0` — version initiale produite lors du cadrage matinal
- `v1.2`, `v1.3` — révisions mineures après revue PO
- `v2.0` — révision majeure suite à une perturbation (changement de scope)
- Chaque version est commitée séparément avec message Git explicite
- Le statut « Validé PO » nécessite une trace écrite (commentaire, mail, Teams)
