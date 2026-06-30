# Fiches Personas — EduTutor IA
> CADRAGE MATINAL · ARTEFACT 2 SUR 7 · Mise à jour post-perturbation J1  
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum  
> Auteur original : Mohamed Amine EL AFRIT · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|---|---|
| **Équipe n°** | 21 |
| **Membres** | Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS |
| **Sprint concerné** | Cadrage / Perturbation J1 |
| **Version** | v2.0 (post-perturbation J1 — fusion des cibles primaires) |
| **Date de remise** | 29/06/2026 |
| **Statut** | Draft |

> 💡 Convention de nommage : `equipe-21-persona-v2.0.md`

---

## PRÉAMBULE — Pourquoi cet artefact ?

Une persona représente un utilisateur type, construit à partir de données réelles et non d'intuitions. Elle sert à trancher les arbitrages produit : « est-ce que Camille utiliserait vraiment cette fonctionnalité ? » remplace « est-ce que c'est bien ? ».

**Évolution post-perturbation J1 :** suite au retour très positif de Mme Lefèvre (enseignante) sur la démo de cadrage, le sponsor a demandé l'intégration de cette cible dans le périmètre direct du produit. L'équipe reclasse donc ses 3 cibles :

- **Cible primaire (×2)** : l'étudiant·e (utilisateur direct, usage individuel) et l'enseignant·e (utilisateur direct, usage classe) — deux utilisateurs finaux du produit, avec des parcours différents mais un statut équivalent en priorité.
- **Cible secondaire** : l'établissement scolaire, acheteur B2B qui ne touche pas directement l'outil mais conditionne son adoption institutionnelle.

> 💡 Travaillez en binôme minimum, jamais en solo (biais de projection).

---

## 1. Persona primaire A — Étudiant·e du supérieur

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

> Intégrée en cible **primaire** suite à la perturbation J1 (29/06, 14h00) : retour sponsor très positif, demande explicite d'intégration au périmètre direct du produit.

### Contexte de la perturbation

> *« C'est exactement l'outil qu'il me faut pour suivre la progression de mes 28 étudiants en révision d'examens. Je veux pouvoir voir leurs scores, repérer ceux qui décrochent, et leur envoyer des conseils. »* — Mme Lefèvre, retour sponsor du 29/06

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
- **Étudiants :** smartphones Android personnels (mix modèles 2018-2023), accès ENT via navigateur
- **Contrainte légale :** DPO de l'établissement refuse tout outil utilisant OpenAI ou des serveurs hors UE — a déjà bloqué ChatGPT
- **Rythme de préparation :** crée 1 quiz par chapitre, ~3 chapitres/mois soit ~9 quiz/mois à concevoir et corriger

### 2.3. Compétences numériques

- **Power user :** Word + Excel (mise en forme avancée), Moodle (dépôt de cours, quiz basique), Pronote (notes, absences)
- **Autonome :** ENT scolaire, envoi de fichiers, visioconférence (Teams)
- **Limite :** pas développeuse, allergique aux installations en ligne de commande (CLI), ne comprend pas les notions d'API ou de Docker
- **IA :** a testé ChatGPT 2 fois, impressionnée par la rapidité mais méfiante sur la fiabilité factuelle et la conformité légale
- **Veille :** suit l'actualité edtech via Twitter/X et la newsletter Café Pédagogique

### 2.4. Frustrations / pain points (chiffrés)

- **~90 min** pour créer 1 quiz cohérent et varié depuis zéro (soit ~13h30/mois en conception)
- **28 copies × 3 quiz/semaine** à corriger = **~12h de correction/mois** pour des QCM qu'une machine pourrait corriger
- Les étudiants **se repassent les réponses** entre promotions : les mêmes questions perdent leur intérêt pédagogique
- Les outils IA existants (ChatGPT, Quizlet) **bloqués par le DPO** de l'établissement
- Peur de l'**hallucination factuelle** : *« Si l'outil invente une erreur de SVT ou de droit, je la donne à mes 28 élèves. »*
- Pas de **tableau de bord** : elle ne sait pas qui décroche avant qu'il soit trop tard

### 2.5. Objectifs (jobs-to-be-done, SMART)

- **Gagner du temps :** générer 1 quiz personnalisé en **moins de 5 minutes** sur n'importe quel chapitre (vs 90 min aujourd'hui)
- **Fiabilité :** obtenir des questions ancrées dans son cours fourni, vérifiables et traçables à une source
- **Suivi :** visualiser les scores de ses 28 étudiants, identifier ceux qui décrochent en **3 clics maximum**
- **Conformité :** utiliser un outil validé par le DPO (conformité RGPD documentée, données hébergées en France)
- **Export :** exporter le quiz en Word ou PDF pour impression en salle des profs ou dépôt sur Moodle

### 2.6. Critères de succès personnels

> *« Si je gagne 1h/semaine sur ma préparation, j'adopte définitivement et j'en parle à mes collègues. »*

> *« Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais. »*

> *« Si l'outil invente des erreurs factuelles, je ne peux pas le donner à mes élèves. »*

> *« Si je peux exporter en Word pour l'imprimer en salle des profs, c'est parfait. »*

> *« Si je vois en un coup d'œil quels étudiants décrochent, ça change tout à mon suivi. »*

---

## 3. Comparatif des deux personas primaires

| Dimension | Camille (étudiant) | Mme Lefèvre (enseignant) |
|---|---|---|
| Motif d'usage | Réviser son propre cours | Générer des évaluations pour sa classe |
| Fréquence d'usage | 2-3 fois/semaine | 1-2 fois/mois par séquence |
| Volume par session | 1 quiz, usage solo | 1 quiz pour 28 étudiants |
| Critère bloquant | Qualité des questions / confidentialité | Conformité RGPD / fiabilité factuelle |
| Cycle d'adoption | Individuelle, immédiate | Plus lente : validation DPO en amont |
| Feature clé attendue | Quiz + historique perso | Quiz + dashboard classe + export Word/PDF |
| Volume marché FR | ~2,7M étudiants du supérieur (MESR 2024) | ~770 000 enseignants (Éducation nationale 2024) |

> Ces deux personas partagent le même besoin racine — générer un quiz fiable à partir d'un cours fourni — mais avec des contextes d'usage, des fréquences et des critères de succès différents. Le MVP (F1-F6) sert en priorité Camille ; les features dashboard/export pour Mme Lefèvre sont à arbitrer en MoSCoW (cf. note de décision J1).

---

## 4. Persona secondaire — Établissement scolaire (acheteur B2B)

> Reclassée de tertiaire à **secondaire** : l'établissement ne touche pas l'outil au quotidien, mais conditionne l'adoption institutionnelle de Mme Lefèvre et de ses collègues — son rôle de décideur/payeur reste central pour la stratégie B2B.

### 4.1. Identité

| Champ | Valeur |
|---|---|
| **Nom / Prénom** | M. David Chen (fictif) |
| **Âge** | 51 ans |
| **Profession** | Directeur des études d'un lycée privé sous contrat (1 200 élèves) |
| **Localisation** | Lyon 6e · même établissement que Mme Lefèvre |
| **Situation** | Marié, enfants grands, 25 ans d'expérience enseignement |
| **Photo / avatar** | [ Insérer image ou avatar fictif ] |

### 4.2. Contexte d'achat

- Budget edtech **~12 000€/an** pour l'ensemble du lycée (10€/élève × 1 200)
- **Cycle d'achat : 6 mois minimum** (validation pédagogique + DPO + comptabilité)
- Décide en concertation avec 3 acteurs : conseil pédagogique, DPO, gestionnaire financier
- Choisit les outils edtech **1 fois/an**, en mai/juin pour la rentrée de septembre
- A déjà signé pour 2 outils edtech qui ont fermé en cours d'année — méfiant sur la pérennité

### 4.3. Compétences numériques

- Utilisateur courant ENT/Pronote, gère les comptes profs et élèves
- Pas technique, fait confiance au DSI mutualisé du réseau d'établissements
- Lit les CGV/CGU, **exige des engagements RGPD écrits et signés** avant tout déploiement
- Suit les recommandations de la CNIL et de son DPO à la lettre

### 4.4. Frustrations / pain points (chiffrés)

- DPO refuse **systématiquement** les outils utilisant OpenAI ou des LLM US (transferts hors UE)
- Pression du conseil d'administration pour démontrer une **"stratégie IA pédagogique"** sans budget supplémentaire
- **2 outils edtech sur les 5 derniers** ont fermé en cours d'année — pertes sèches
- Profs râlent quand on impose un nouvel outil sans adhésion préalable — taux d'adoption < 20 % sur le dernier outil

### 4.5. Objectifs (jobs-to-be-done)

- Disposer d'un outil edtech **RGPD conforme**, signable sans risque juridique pour le DPO
- **Tarification prévisible par élève / par an**, sans surprise au renouvellement
- Adhésion d'au moins **30 % des profs** dès la première année (sinon échec budgétaire)
- Pouvoir dire au CA **"on est en avance sur l'IA"** avec des preuves concrètes d'usage

### 4.6. Critères de succès personnels

> *"Si le DPO valide les CGV en 30 min de lecture, c'est un signal positif."*

> *"Si 5 profs me demandent spontanément d'élargir l'usage, je signe le renouvellement."*

> *"Si je peux dire au CA 'on est en avance sur l'IA' sans mentir, c'est gagné."*

> *"Si le coût reste sous 8€/élève/an tout compris, le budget passe sans discussion."*

---

## 5. Anti-personas (qui n'est PAS la cible)

### 5.1. Anti-persona du persona Étudiant
Élève de primaire ou collège (< 15 ans). EduTutor exige un cours fourni au format PDF ou texte de niveau supérieur. L'autonomie nécessaire (uploader, contextualiser, interpréter les résultats) n'est pas alignée avec ce profil. Ne pas chercher à les attirer.

### 5.2. Anti-persona du persona Enseignant
Enseignant·e du primaire ou retraité·e en autoformation. Le besoin de générer des supports d'évaluation à grande échelle (28 étudiants × 3 quiz/semaine) n'existe pas dans ces contextes. Ne pas chercher à élargir l'offre vers ces profils.

### 5.3. Anti-persona du persona Établissement
École internationale tournée vers OpenAI/Anthropic, sans contrainte RGPD. Notre différenciation est précisément le local-first et la souveraineté des données. Une école qui valorise un partenariat OpenAI n'achètera jamais EduTutor — et inversement, ce n'est pas un marché à courir.

---

## ✅ Grille d'auto-évaluation

| Critère qualité | Auto-évaluation | Commentaire / preuve |
|---|---|---|
| Les personas sont nommés concrètement (prénom + nom + âge précis) | ✅ Oui | Camille Martin 21 ans / Mme Sophie Lefèvre 42 ans / M. David Chen 51 ans |
| Chaque persona comporte les 6 dimensions complétées | ✅ Oui | Identité, contexte, compétences, frustrations, objectifs, critères — présents pour les 3 |
| Le contexte précise un volume horaire et un environnement physique | ✅ Oui | Camille : 8h/sem, soirée, BU / Lefèvre : 12h/sem, salle info réseau lent |
| Les compétences numériques sont nuancées | ✅ Oui | 5 points par persona avec niveaux différenciés et exemples concrets |
| Les frustrations sont chiffrées au moins 3 fois sur 5 par persona | ✅ Oui | Camille : 3h/sem, 100%, 3 semaines / Lefèvre : 12h/mois, 90 min, 28 copies / Chen : 2/5 outils, 20% adoption |
| Les objectifs respectent au moins partiellement le format SMART | ✅ Oui | Chaque objectif a un chiffre et un délai |
| Les critères de succès sont formulés au "je", entre guillemets | ✅ Oui | 4-5 citations au "je" par persona |
| Les 3 anti-personas sont décrits avec justification | ✅ Oui | Section 5 |
| Le reclassement primaire/secondaire est justifié et tracé | ✅ Oui | Section 3 (comparatif) + mention explicite perturbation J1 |
| Le document a été relu et validé par l'équipe complète | ☐ Partiel | À valider collectivement avant dépôt |

---

## 📚 Références et conventions

- Cours Agile/Scrum (Mohamed EL AFRIT) : mohamedelafrit.com/teaching/Master_Classe_Agile/cours.html
- Roman Pichler, Pragmatic Personas : https://www.romanpichler.com/blog/pragmatic-personas-and-personas-in-a-nutshell/
- Nielsen Norman Group, Personas guide : https://www.nngroup.com/articles/persona/
- Scrum Guide officiel FR : scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-French.pdf
- Site APOCAL'IPSSI : mohamedelafrit.com/teaching/APOCALIPSSI

### Convention de versionnement

- v1.0 : version initiale, cadrage matinal (étudiant primaire, enseignant secondaire/Release 2, établissement tertiaire)
- **v2.0 : révision post-perturbation J1** — étudiant et enseignant reclassés primaires, établissement reclassé secondaire
- Chaque version est commitée séparément avec message Git explicite (`docs(personas): reclassement primaire suite perturbation J1`)
