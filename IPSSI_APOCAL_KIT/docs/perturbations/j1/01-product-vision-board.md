# Product Vision Board — EduTutor IA
> CADRAGE MATINAL · ARTEFACT 1 SUR 7  
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum  
> Auteur : Mohamed Amine EL AFRIT · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|---|---|
| **Équipe n°** | 21 |
| **Membres** | Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS |
| **Sprint concerné** | Cadrage |
| **Version** | v3(aprés perturbation J4) |
| **Date de remise** | 02/07/2026 |
| **Statut** | Draft |

> 💡 Convention de nommage : `equipe-21-vision-board-v1.1.md`

---

## PRÉAMBULE — Pourquoi cet artefact ?

Le Product Vision Board, formalisé par Roman Pichler, condense en une seule page la direction stratégique du produit. Il répond à cinq questions : quelle est l'ambition long terme (Vision) ? pour qui (Target Group) ? pour quels besoins (Needs) ? avec quel produit (Product) ? et comment saurons-nous que c'est un succès (Business Goals) ?

> 💡 Ce document évolue au fil de la semaine. Recommitter à chaque révision majeure (perturbation J1, J3, J4) avec un nouveau numéro de version.

---

## 1. Vision

**Pour** les étudiant·e·s du supérieur Et enseignants
**Qui** veulent réviser ou évaluer efficacement à partir de leurs propres cours  
**EduTutor IA** est une application web de génération automatique de quiz QCM  
**Qui** transforme n'importe quel PDF ou texte en quiz corrigé instantanément, sans que les données ne quittent le serveur  
**Contrairement à** Quizlet AI, Wilgo ou Khanmigo  
**Notre produit** s'appuie sur un LLM local (Ollama), garantit la souveraineté des données, respecte le RGPD sans compromis, et propose des prompts métier pensés pour les enseignants

> **Notre vision finalisée :** "Permettre à chaque étudiant·e du supérieur — en France et à l'international — de transformer n'importe quel cours en quiz personnalisé en moins de 60 secondes, dans sa langue, accessible à tous y compris en situation de handicap, avec une IA locale qui ne transmet aucune donnée hors du territoire UE."

---

## 2. Target Group (cibles utilisateurs)

### 2.1. Cible primaire — Étudiant·e du supérieur

| Champ | Détail |
|---|---|
| **Profil** | 18-25 ans · L1-M2 (Bac+1 à Bac+5) · usage smartphone et laptop quotidien |
| **Volume FR** | ~2,7 millions d'étudiants dans le supérieur (chiffres MESR 2024) |
| **Pain point** | ~3h/semaine perdues à chercher des fiches de révision alignées sur leur cours réel |
| **Critère clé** | Rapidité de génération (< 60s), gratuité, confidentialité des données, interface simple sans installation |

### 2.2. Cible primaire — Enseignant·e 

| Champ | Détail |
|---|---|
| **Profil** | 35-55 ans · lycée privé sous contrat / BTS / supérieur · maîtrise modérée du numérique |
| **Volume FR** | ~770 000 enseignants tous niveaux (Éducation nationale 2024) |
| **Pain point** | ~12h/mois en correction + 90 min pour créer un seul quiz manuellement |
| **Critère clé** | Interface simple, conformité RGPD non négociable, export Word/PDF pour impression |

### 2.3. Cible secondaire — Établissement scolaire (acheteur B2B)
s
| Champ | Détail |
|---|---|
| **Profil** | Direction de lycée privé · ENT scolaire · responsable pédagogique d'école supérieure |
| **Volume FR** | ~7 500 lycées + ~3 500 établissements supérieurs |
| **Pain point** | Budget edtech contraint (< 5€/élève/an) + obligation RGPD non négociable + cycle d'achat 6 mois |
| **Critère clé** | Conformité RGPD signée, tarification prévisible par élève/an, adhésion des enseignants préalable |

### 2.4. Cible tertiaire — Étudiant·e international·e / Erasmus

| Champ | Détail |
|---|---|
| **Profil** | 18-25 ans · L1-M2 (Bac+1 à Bac+5) · usage smartphone et laptop quotidien |
| **Volume FR** | ~2,7 millions d'étudiants dans le supérieur (chiffres MESR 2024) |
| **Pain point** | ~3h/semaine perdues à chercher des fiches de révision alignées sur leur cours réel |
| **Critère clé** | Rapidité de génération (< 60s), gratuité, confidentialité des données, interface simple sans installation |
---

## 3. Needs (besoins résolus)

### 3.1. Besoins de la cible primaire (Étudiant)

- Générer en moins de 60 sec un quiz de révision sur n'importe quel chapitre d'un cours fourni (PDF ou texte)
- Identifier ses lacunes par chapitre **2 semaines avant les partiels** (vs 3 jours avant aujourd'hui)
- Gagner **~2h/semaine** sur la recherche de supports (vs ~3h perdues aujourd'hui)
- Utiliser un outil gratuit, sans abonnement, sans que ses données de cours quittent son poste
- Consulter l'historique de ses quiz pour piloter sa progression dans le temps

### 3.2. Besoins de la cible secondaire (Enseignant)

- Préparer des supports d'évaluation QCM alignés sur son programme en **moins de 5 minutes** (vs 90 min manuellement)
- Garantir que les contenus de ses cours ne quittent jamais un serveur tiers (conformité RGPD établissement)
- Exporter les quiz générés en Word/PDF pour impression directe en salle des profs
- Suivre l'engagement de sa classe (qui a répondu, score moyen, lacunes communes)

### 3.3. Besoins de la cible tertiaire (Établissement)

- Disposer d'un outil edtech RGPD conforme, sans transfert de données hors UE, signable sans risque juridique
- Tarification prévisible **par élève / par an**, sans surprise au renouvellement
- Adhésion d'au moins **30 % des profs** dès la première année pour justifier le budget

---

## 4. Product (caractéristiques signature)

- **Génération rapide** : 10 QCM en moins de 60 sec à partir d'un cours fourni (PDF ou texte)
- **100 % local** : IA via Ollama (Llama 3.1 8B / Phi-3-mini) — aucune donnée ne quitte le serveur
- **Parcours en 3 clics** : déposer son cours → générer → répondre → voir son score
- **Architecture réversible** : multi-fournisseurs LLM (Ollama par défaut, bascule cloud via ADR documenté)
- **Ancrage pédagogique** : prompts métier pensés pour les enseignants, pas des résumés génériques

### 4.1. MVP must-have (Release 1) 

| ID | Fonctionnalité |
|---|---|
| **F1** | Inscription / connexion email, validation par lien, reset mot de passe, page profil |
| **F2** | Saisie d'un cours : upload PDF ≤ 5 Mo ou texte ≥ 200 caractères |
| **F3** | Génération automatique de 10 QCM via LLM local (Ollama) en moins de 60 secondes |
| **F4** | Soumission et correction automatique (une bonne réponse par QCM) |
| **F5** | Affichage score /10 + détail bonnes/mauvaises réponses question par question |
| **F6** | Historique persisté des quiz par utilisateur (date, cours, score) |

### 4.2. Pistes Release 2 

- **Bouton "Signaler une erreur"** → boucle de feedback utilisateur directe, lié perturbation J4
- **Export RGPD (endpoint SAR Art. 15)** → droit d'accès utilisateur, lié perturbation J3-bis
- **Garantir que les données de des cours** → visualisation des cours et gestion des QCM, valeur pour Mme Lefèvre
- **Dashboard de progression** → visualisation taux de réussite par thème, valeur pour Mme Lefèvre

---

## 5. Business Goals (objectifs de succès)

### 5.1. Objectifs d'adoption

| KPI | Cible | Délai |
|---|---|---|
| Utilisateurs actifs hebdomadaires (WAU) | 500 | T+3 mois |
| Utilisateurs actifs hebdomadaires (WAU) | 2 000 | T+6 mois |
| Taux de rétention semaine J+1 | ≥ 40 % | T+3 mois |
| Viralité (1 user recommande à 1 autre) | 1 sur 5 | T+6 mois |

### 5.2. Objectifs de satisfaction

| KPI | Cible | Délai |
|---|---|---|
| NPS | > 30 | T+9 mois |
| Taux de quiz signalés "erreur factuelle" | < 5 % | T+3 mois |
| Quiz générés en moins de 60 secondes | ≥ 95 % | Dès le MVP |

### 5.3. Objectifs business (long terme)

| KPI | Cible | Délai |
|---|---|---|
| Établissements scolaires sous contrat | ≥ 3 | T+12 mois |
| Coût d'acquisition (CAC) | < 5 € / utilisateur converti | T+6 mois |
| Modèle économique | Socle gratuit open source + option B2B établissements | T+12 mois |

---

## 6. Différenciateurs vs concurrents

### 6.1. Cartographie des concurrents

| Concurrent | Positionnement | Limite identifiée |
|---|---|---|
| **Wilgo.ai** | Compagnon IA français pour étudiants | Cloud, dépendance OpenAI, données hors UE |
| **Leo (iamleo.ai)** | Tuteur IA Bac/sup ancré sur programmes français | Cible étudiants uniquement, pas d'angle enseignant |
| **Quizlet AI** | Cartes mémoire et quiz IA, pionnier US | Pas d'ancrage cours fourni, données hors UE |
| **Khanmigo** | Tuteur IA Khan Academy, lancé 2023 | US-first, conformité RGPD UE floue, pas de version FR |

### 6.2. Nos 3 différenciateurs argumentés

**01 — Prompts métier pour enseignants**  
Les concurrents sont étudiant-first : l'élève cherche un cours, l'IA résume. EduTutor inverse : l'enseignant fournit son programme, l'IA produit des supports d'évaluation prêts à utiliser en classe. Résultat : des QCM pédagogiquement défendables, pas des résumés génériques.

**02 — Pédagogie ancrée, pas hallucinée**  
Les LLM bruts hallucinent sur les chiffres et les dates. EduTutor génère à partir du cours fourni par l'étudiant ou l'enseignant, pas d'une base de connaissance générale. Chaque question est traçable à une source : vérifiable, fiable, défendable. Release 2 : RAG sur manuel scolaire.

**03 — RGPD, local-first**  
Les concurrents utilisent OpenAI ou Anthropic : les données quittent l'UE, conformité RGPD floue (décisions CNIL 2024). EduTutor tourne sur Ollama local par défaut : aucune donnée ne quitte le serveur. Prérequis contractuel non négociable pour la cible B2B éducation française.

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-évaluation | Commentaire / preuve |
|---|---|---|
| La Vision tient en 1 phrase mémorable et survit aux releases | ✅ Oui | Section 1 : format Roman Pichler complet "Pour / Qui / Contrairement à" |
| Les 3 niveaux de cibles sont décrits avec profil + volume + pain point | ✅ Oui | Sections 2.1, 2.2, 2.3 : primaire + secondaire + tertiaire avec volume FR chiffré |
| Au moins 3 besoins par cible sont formulés en verbes d'action mesurables | ✅ Oui | Section 3 : 5 besoins étudiant, 4 enseignant, 3 établissement — tous chiffrés |
| Le produit est décrit en 3 à 5 caractéristiques signature | ✅ Oui | Section 4 : 5 caractéristiques orientées bénéfice perçu, aucune liste technique |
| Les 6 features F1-F6 du MVP sont rappelées et 2-3 pistes Release 2 identifiées | ✅ Oui | Sections 4.1 et 4.2 : F1-F6 en tableau + 3 pistes Release 2 justifiées |
| Les Business Goals comportent au moins 3 KPI chiffrés et datés | ✅ Oui | Section 5 : 8 KPI avec cibles chiffrées et délais T+3/T+6/T+9/T+12 mois |
| Les 4 concurrents sont cartographiés avec positionnement + limite identifiée | ✅ Oui | Section 6.1 : Wilgo, Leo, Quizlet AI, Khanmigo avec limite argumentée |
| Les 3 différenciateurs EduTutor IA sont argumentés au-delà du slogan | ✅ Oui | Section 6.2 : 3 différenciateurs en paragraphes complets, pas des slogans |
| Le document a été relu et validé par l'équipe complète | ☐ Partiel | À valider collectivement avant 13h — sections [ À compléter ] à finaliser |

---

## 📚 Références

- Cours Agile/Scrum (Mohamed EL AFRIT) : mohamedelafrit.com/teaching/Master_Classe_Agile/cours.html
- Roman Pichler, Product Vision Board : https://www.romanpichler.com/tools/product-vision-board/
- Scrum Guide officiel FR : scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-French.pdf
- Site APOCAL'IPSSI : mohamedelafrit.com/teaching/APOCALIPSSI


