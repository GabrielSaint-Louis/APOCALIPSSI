# Fiches Personas — EduTutor IA
> CADRAGE MATINAL · ARTEFACT 2 SUR 7 · Mise à jour post-perturbation J4  
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum  
> Auteur original : Mohamed Amine EL AFRIT · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|---|---|
| **Équipe n°** | 21 |
| **Membres** | Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS |
| **Sprint concerné** | Perturbation J4 |
| **Version** | v3.0 (post-perturbation J4 — ajout persona internationale & accessibilité) |
| **Date de remise** | 02/07/2026 |
| **Statut** | Draft |

> 💡 Convention de nommage : `equipe-21-persona-v3.0.md`

---

## PRÉAMBULE — Évolution du document

| Version | Date | Changement |
|---|---|---|
| v1.0 | 29/06/2026 matin | Version initiale cadrage (étudiant primaire, enseignant secondaire, établissement tertiaire) |
| v2.0 | 29/06/2026 14h | Perturbation J1 — étudiant et enseignant reclassés primaires, établissement reclassé secondaire |
| **v3.0** | **02/07/2026** | **Perturbation J4 — ajout persona Lucia (cible internationale & accessibilité RGAA/i18n)** |

---

## 1. Persona primaire A — Camille Martin, Étudiante

### 1.1. Identité

| Champ | Valeur |
|---|---|
| **Nom / Prénom** | Camille Martin (fictif) |
| **Âge** | 21 ans |
| **Profession / Études** | Étudiante en L3 Droit, Paris II Panthéon-Assas |
| **Localisation** | Paris 5e · trajet quotidien RER B 35 min |
| **Situation** | Boursière échelon 3, colocation 2 personnes |
| **Photo / avatar** | [ Insérer image ou avatar fictif ] |

### 1.2. Contexte d'usage

- Smartphone Android personnel (Samsung A53), wifi domestique fluide, 4G dans le RER
- Laptop personnel (Windows, 8 Go RAM), révise principalement en soirée 19h-22h et le dimanche
- Révise **~8h/semaine** dont **~3h perdues** à chercher des fiches alignées sur son cours réel
- Utilise ChatGPT pour résumer ses cours, mais perd confiance quand les réponses semblent inexactes
- A des partiels dans 3 semaines, accumule des PDFs de cours sans plan de révision structuré

### 1.3. Compétences numériques

- Power user smartphone (Instagram, TikTok, BlaBlaCar, ENT université)
- Autonome sur Moodle, importe fichiers PDF/Word sans souci
- A utilisé ChatGPT 4-5 fois pour des résumés — usage irrégulier, méfiance sur la fiabilité
- Allergique aux installations CLI ou paramétrages techniques avancés
- Sensible à la confidentialité des données depuis le scandale Cambridge Analytica

### 1.4. Frustrations / pain points (chiffrés)

- Perd **~3h/semaine** à chercher des fiches de révision sur internet, qualité aléatoire
- **100 % des quiz génériques** ne correspondent pas à son cours (chaque promo a un cours différent)
- Se sent surchargée à **3 semaines** des partiels, sans plan de révision personnalisé
- Ne sait pas mesurer si elle "connaît" un chapitre ou si elle "croit" le connaître
- Peur de perdre ses données personnelles et ses cours sur des apps américaines non conformes RGPD

### 1.5. Objectifs (jobs-to-be-done, SMART)

- Générer un quiz sur n'importe quel chapitre de son cours en **moins de 5 minutes**
- Identifier ses lacunes par chapitre **2 semaines avant les partiels** (vs 3 jours avant aujourd'hui)
- Gagner **~2h/semaine** sur la recherche de supports de révision
- Utiliser un outil **gratuit**, sans abonnement, sans que ses données quittent son poste

### 1.6. Critères de succès personnels

> *"Je veux réviser MON cours, pas un résumé générique trouvé sur internet."*

> *"Si je gagne au moins 1h/semaine sur ma préparation, j'adopte définitivement."*

> *"Si ça plante 1 fois en bibliothèque devant mes amies, je n'y reviens jamais."*

> *"Si les questions sont vraiment basées sur mon cours et pas inventées, j'arrête ChatGPT pour la révision."*

---

## 2. Persona primaire B — Mme Sophie Lefèvre, Enseignante

> Intégrée en cible **primaire** suite à la perturbation J1 (29/06, 14h00).

### 2.1. Identité

| Champ | Valeur |
|---|---|
| **Nom / Prénom** | Mme Sophie Lefèvre |
| **Âge** | 42 ans |
| **Profession** | Professeure de Communication, BTS 1ère année, lycée privé sous contrat |
| **Localisation** | Lyon 6e · trajet voiture 25 min |
| **Situation** | Mariée, 2 enfants (12 et 15 ans), salaire ~2 700€ net/mois |
| **Classe** | 28 étudiants BTS Communication 1ère année |
| **Photo / avatar** | [ Insérer image ou avatar fictif ] |

### 2.2. Contexte d'usage

- **Charge hebdomadaire :** 6h de cours + ~3h de préparation + ~3h de correction = **~12h/semaine** hors cours
- **Équipement perso :** laptop Windows 11, smartphone Android (Samsung Galaxy A54)
- **Équipement établissement :** salle informatique disponible mais réseau lent (4G partagée) ; vidéoprojecteur fixe en classe
- **Contrainte légale :** DPO de l'établissement refuse tout outil utilisant OpenAI ou des serveurs hors UE
- **Rythme :** ~9 quiz/mois à concevoir et corriger (~3 chapitres/mois)

### 2.3. Compétences numériques

- Power user : Word + Excel, Moodle, Pronote
- Pas développeuse, allergique aux installations CLI
- A testé ChatGPT 2 fois — impressionnée mais méfiante sur la fiabilité factuelle et la conformité légale
- Suit l'actualité edtech via Twitter/X et la newsletter Café Pédagogique

### 2.4. Frustrations / pain points (chiffrés)

- **~90 min** pour créer 1 quiz cohérent depuis zéro (soit ~13h30/mois en conception)
- **28 copies × 3 quiz/semaine** à corriger = **~12h de correction/mois**
- Les outils IA existants (ChatGPT, Quizlet) **bloqués par le DPO**
- Peur de l'hallucination factuelle : *"Si l'outil invente une erreur, je la donne à mes 28 élèves."*
- Pas de tableau de bord : ne sait pas qui décroche avant qu'il soit trop tard

### 2.5. Objectifs (jobs-to-be-done, SMART)

- Générer 1 quiz personnalisé en **moins de 5 minutes** (vs 90 min aujourd'hui)
- Visualiser les scores de ses 28 étudiants, identifier ceux qui décrochent en **3 clics maximum**
- Utiliser un outil validé par le DPO (conformité RGPD documentée, données hébergées en France)
- Exporter le quiz en Word ou PDF pour impression ou dépôt sur Moodle

### 2.6. Critères de succès personnels

> *"Si je gagne 1h/semaine sur ma préparation, j'adopte définitivement."*

> *"Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais."*

> *"Si l'outil invente des erreurs factuelles, je ne peux pas le donner à mes élèves."*

> *"Si je vois en un coup d'œil quels étudiants décrochent, ça change tout à mon suivi."*

---

## 3. ⚡ Persona primaire C — Lucia Martínez, Lycéenne internationale malvoyante

> **Ajoutée en v3.0 suite à la perturbation J4 (02/07/2026).**  
> L'adoption nationale par l'État et la levée de fonds ouvrent deux axes non négociables : **accessibilité RGAA** et **internationalisation (i18n)**. Lucia est la persona de référence pour valider ces deux axes.

### 3.1. Identité

| Champ | Valeur |
|---|---|
| **Nom / Prénom** | Lucia Martínez (fictif) |
| **Âge** | 17 ans |
| **Profession / Études** | Lycéenne en Terminale ES, Séville (Espagne) |
| **Localisation** | Séville, Espagne · fuseau horaire Europe/Madrid |
| **Situation de handicap** | Malvoyante (acuité visuelle réduite à 10%) — utilise NVDA (lecteur d'écran) et ZoomText (loupe logicielle) |
| **Situation** | Vit chez ses parents, bourse d'études espagnole |
| **Photo / avatar** | [ Insérer image ou avatar fictif ] |

### 3.2. Contexte d'usage

- Smartphone Android (Samsung A52) + laptop Windows 11 avec NVDA activé en permanence
- Connexion wifi domestique stable, 4G en déplacement
- Révise principalement en soirée 18h-22h, **navigateur Firefox + NVDA** comme environnement de travail principal
- Suit les cours **en espagnol**, apprend le français comme LV2 mais ne le maîtrise pas suffisamment pour utiliser une interface FR
- Ses PDFs de cours sont en espagnol, parfois scannés (qualité OCR variable)
- Volume de révision : **10-15h/semaine** en période d'examens (Selectividad)
- Accès à un ENT scolaire espagnol (Moodle en español)

### 3.3. Compétences numériques

- Power user lecteur d'écran (NVDA + Firefox) : navigue **intégralement au clavier**, sans souris
- À l'aise avec les outils numériques accessibles (ENT, Moodle, Google Docs)
- Utilise déjà Quizlet en espagnol mais frustration : interface partiellement inaccessible
- A testé ChatGPT en español mais inquiète pour ses données (pas de RGPD clair)
- **Allergique** aux interfaces avec drag & drop ou interactions souris-only

### 3.4. Frustrations / pain points (chiffrés)

- **70 % des outils edtech** qu'elle teste ne sont pas navigables au clavier → abandon après 2 min
- Interface EduTutor en français uniquement → **incompréhensible**, impossible à utiliser
- Interfaces avec texte gris clair sur fond blanc → **illisible** même avec ZoomText (contraste insuffisant)
- Images et icônes sans texte alternatif → **désorientation** dans la navigation vocale
- Perd **~4h/semaine** sur des outils qui promettent l'accessibilité sans la tenir
- PDFs scannés mal OCérisés → pénalisation supplémentaire par rapport aux autres étudiants

### 3.5. Objectifs (jobs-to-be-done, SMART)

- Générer un quiz de révision **en espagnol** sur n'importe quel chapitre en **moins de 5 minutes**
- Naviguer sur l'intégralité de l'app **au clavier sans souris** (tab order complet, focus visible)
- Utiliser une interface conforme **WCAG 2.1 AA** (équivalent européen du RGAA français)
- Identifier ses lacunes par chapitre **2 semaines avant la Selectividad**

### 3.6. Critères de succès personnels

> *"Si je peux naviguer sur toute l'app sans toucher la souris, je l'adopte."*

> *"Si les quiz sont générés en español à partir de mes cours espagnols, c'est parfait."*

> *"Si mon lecteur d'écran lit correctement chaque question et chaque option, c'est gagné."*

> *"Si l'entreprise est européenne et respecte le RGPD, mes parents me laisseront l'utiliser."*

### 3.7. Impact sur les artefacts

| Artefact | Impact J4 |
|---|---|
| Story Map | Nouvelle colonne "Accessibilité & i18n" |
| Product Backlog | +5 stories taguées [a11y] et [i18n] |
| DoD | Ajout : "navigable au clavier + textes alternatifs + contraste ≥ 4.5:1" |
| Release Planning | Release 3 dédiée RGAA + i18n |

---

## 4. Persona secondaire — M. David Chen, Établissement scolaire B2B

> Reclassé de tertiaire à **secondaire** en v2.0 (J1). Inchangé en v3.0.

### 4.1. Identité

| Champ | Valeur |
|---|---|
| **Nom / Prénom** | M. David Chen (fictif) |
| **Âge** | 51 ans |
| **Profession** | Directeur des études d'un lycée privé sous contrat (1 200 élèves) |
| **Localisation** | Lyon 6e · même établissement que Mme Lefèvre |
| **Situation** | Marié, enfants grands, 25 ans d'expérience enseignement |

### 4.2. Contexte d'achat

- Budget edtech **~12 000€/an** pour l'ensemble du lycée (10€/élève × 1 200)
- **Cycle d'achat : 6 mois minimum** (validation pédagogique + DPO + comptabilité)
- Choisit les outils edtech **1 fois/an**, en mai/juin pour la rentrée de septembre
- A déjà signé pour 2 outils edtech qui ont fermé en cours d'année — méfiant sur la pérennité

### 4.3. Compétences numériques

- Utilisateur courant ENT/Pronote, gère les comptes profs et élèves
- Pas technique, fait confiance au DSI mutualisé
- Lit les CGV/CGU, **exige des engagements RGPD écrits et signés**

### 4.4. Frustrations / pain points

- DPO refuse **systématiquement** les outils utilisant OpenAI ou LLM US
- **2 outils edtech sur les 5 derniers** ont fermé en cours d'année
- Taux d'adoption < 20 % sur le dernier outil imposé sans adhésion préalable

### 4.5. Objectifs

- Outil RGPD conforme, signable sans risque juridique pour le DPO
- Tarification prévisible par élève / par an
- Adhésion d'au moins **30 % des profs** dès la première année

### 4.6. Critères de succès personnels

> *"Si le DPO valide les CGV en 30 min de lecture, c'est un signal positif."*

> *"Si 5 profs me demandent spontanément d'élargir l'usage, je signe le renouvellement."*

> *"Si je peux dire au CA 'on est en avance sur l'IA' sans mentir, c'est gagné."*

---

## 5. Comparatif des trois personas primaires

| Dimension | Camille (étudiante) | Mme Lefèvre (enseignante) | Lucia (lycéenne ES, malvoyante) |
|---|---|---|---|
| Motif d'usage | Réviser son propre cours | Générer des évaluations pour sa classe | Réviser en espagnol, accessible au clavier |
| Fréquence | 2-3 fois/semaine | 1-2 fois/mois par séquence | 3-4 fois/semaine (examen Selectividad) |
| Critère bloquant | Qualité / confidentialité | RGPD / fiabilité factuelle | Accessibilité RGAA + langue espagnole |
| Feature clé | Quiz + historique perso | Quiz + dashboard classe + export | Interface ES + navigation clavier + contrastes |
| Axe produit couvert | MVP F1-F6 | Release 2 (dashboard, export) | **Release 3 (RGAA + i18n)** |
| Volume marché | ~2,7M étudiants FR | ~770K enseignants FR | ~45M lycéens EU |

---

## 6. Anti-personas

### 6.1. Anti-persona Étudiant
Élève de primaire ou collège (< 15 ans). Autonomie insuffisante pour uploader, contextualiser et interpréter les résultats. Ne pas chercher à les attirer.

### 6.2. Anti-persona Enseignant
Enseignant·e du primaire ou retraité·e en autoformation. Le besoin de supports d'évaluation à grande échelle n'existe pas dans ces contextes.

### 6.3. Anti-persona Établissement
École internationale valorisant un partenariat OpenAI sans contrainte RGPD. Notre différenciation local-first est précisément ce qu'ils rejettent.

### 6.4. ⚡ Anti-persona J4 — Utilisateur sans contrainte d'accessibilité ni de langue
Étudiant francophone sans handicap visuel, utilisant uniquement la souris. Ne justifie pas à lui seul les investissements RGAA/i18n. L'accessibilité profite à tous (navigation clavier = power users, sous-titres = environnements bruyants), mais **Lucia est le cas test de référence** pour valider chaque critère RGAA avant livraison.

---

## ✅ Grille d'auto-évaluation v3.0

| Critère qualité | Auto-évaluation | Commentaire |
|---|---|---|
| Les personas sont nommés concrètement (prénom + nom + âge précis) | ✅ Oui | Camille 21 ans / Mme Lefèvre 42 ans / Lucia 17 ans / M. Chen 51 ans |
| Chaque persona comporte les 6 dimensions complétées | ✅ Oui | Toutes présentes pour les 4 personas |
| Le contexte précise volume horaire et environnement physique | ✅ Oui | Chaque persona a son contexte chiffré |
| Les frustrations sont chiffrées au moins 3 fois sur 5 | ✅ Oui | Camille, Lefèvre, Lucia : toutes chiffrées |
| Les objectifs respectent le format SMART | ✅ Oui | Chiffres + délais présents |
| Les critères de succès sont formulés au "je" entre guillemets | ✅ Oui | 4-5 citations par persona |
| Les anti-personas sont décrits avec justification | ✅ Oui | Section 6, 4 anti-personas |
| ⚡ La persona J4 couvre accessibilité ET i18n | ✅ Oui | Lucia : malvoyante + espagnophone |
| ⚡ L'évolution de version est tracée | ✅ Oui | Tableau v1.0 → v2.0 → v3.0 |
| Le document a été relu et validé par l'équipe complète | ☐ Partiel | À valider collectivement avant dépôt |
