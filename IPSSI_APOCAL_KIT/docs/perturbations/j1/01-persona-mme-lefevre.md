# Persona Mme Lefèvre — EduTutor IA

> Perturbation J1 · 29/06/2026 · Dépôt : /docs/perturbations/j1/
> Membres : Nicolas CATALUNA, Celia MERABET, Monica RADIFERA RASAMOELIJAONA, Nolan LEFEBVRE, Ilham KADRI, Gabriel SAINT-LOUIS
> Version : v2.0 (post-perturbation J1)  
> Statut : Draft

---

## Contexte de la perturbation

Le sponsor a présenté EduTutor IA à Mme Sophie Lefèvre, 42 ans, enseignante en BTS Communication à Lyon. Sa réaction :

> *« C'est exactement l'outil qu'il me faut pour suivre la progression de mes 28 étudiants en révision d'examens. Je veux pouvoir voir leurs scores, repérer ceux qui décrochent, et leur envoyer des conseils. »*

Cette persona secondaire est désormais à intégrer dans le cadrage. Les artefacts existants (persona Léa Martin, journey étudiant) sont **conservés et non écrasés**.

---

## 1. Identité

| Attribut | Valeur |
|---|---|
| Nom / Prénom | Mme Sophie Lefèvre |
| Âge | 42 ans |
| Profession | Professeure de Communication, BTS 1ère année, lycée privé sous contrat |
| Localisation | Lyon 6ᵉ · trajet voiture 25 min |
| Situation familiale | Mariée, 2 enfants (12 et 15 ans) |
| Salaire | ~2 700 € net/mois |
| Classe | 28 étudiants BTS Communication 1ère année |

---

## 2. Contexte d'usage

- **Charge hebdomadaire :** 6h de cours + ~3h de préparation + ~3h de correction = ~12h/semaine hors cours
- **Équipement perso :** laptop Windows 11, smartphone Android (Samsung Galaxy A54)
- **Équipement établissement :** salle informatique disponible mais réseau lent (4G partagée) ; vidéoprojecteur fixe en classe
- **Étudiants :** smartphones Android personnels (mix modèles 2018–2023), accès ENT via navigateur
- **Contrainte légale :** DPO de l'établissement refuse tout outil utilisant OpenAI ou des serveurs hors UE — exige une conformité RGPD documentée avant déploiement
- **Rythme de préparation :** crée 1 quiz par chapitre, ~3 chapitres/mois soit ~9 quiz/mois à concevoir et corriger

---

## 3. Compétences numériques

- **Power user :** Word + Excel (mise en forme avancée), Moodle (dépôt de cours, quiz basique), Pronote (notes, absences)
- **Autonome :** ENT scolaire, envoi de fichiers, visioconférence (Teams)
- **Limite :** pas développeuse, allergique aux installations en ligne de commande (CLI), ne comprend pas les notions d'API ou de Docker
- **IA :** a testé ChatGPT 2 fois pour reformuler des consignes, reste méfiante sur la fiabilité factuelle
- **Veille :** suit l'actualité edtech via Twitter/X et la newsletter Café Pédagogique ; sensible aux retours d'expérience de collègues

---

## 4. Frustrations / pain points (chiffrés)

- **~90 min** pour créer 1 quiz cohérent et varié depuis zéro (soit ~13h30/mois perdu en conception)
- **28 copies × 3 quiz/semaine** à corriger = ~12h de correction/mois pour des QCM qu'une machine pourrait corriger
- Les étudiants **se repassent les réponses** entre promotions : les mêmes questions d'une année sur l'autre perdent leur intérêt pédagogique
- Les outils IA existants (ChatGPT, Quizlet) **bloqués par le DPO** de l'établissement — elle a déjà été rappelée à l'ordre pour avoir utilisé un outil non validé
- Peur de l'**hallucination factuelle** : *« Si l'outil invente une erreur de SVT ou de droit, je la donne à mes 28 élèves. »*
- Pas de **tableau de bord** : elle ne sait pas qui décroche avant qu'il soit trop tard (résultats partiels = découverte tardive)

---

## 5. Objectifs (jobs-to-be-done, SMART)

- **Gagner du temps :** générer 1 quiz personnalisé en moins de 5 minutes sur n'importe quel chapitre de son propre support (vs 90 min aujourd'hui)
- **Fiabilité :** obtenir des questions ancrées dans son cours fourni, vérifiables et traçables à une source
- **Suivi :** visualiser les scores de ses 28 étudiants, identifier ceux qui décrochent en 3 clics maximum
- **Conformité :** utiliser un outil validé par le DPO (conformité RGPD documentée, données hébergées en France)
- **Export :** exporter le quiz en Word ou PDF pour impression en salle des profs ou dépôt sur Moodle

---

## 6. Critères de succès personnels

> *« Si je gagne 1h/semaine sur ma préparation, j'adopte définitivement. »*  
> *« Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais. »*  
> *« Si je peux exporter en Word pour l'imprimer en salle des profs, c'est parfait. »*  
> *« Si le DPO valide l'outil sans que j'aie à lui organiser 3 réunions de justification, c'est gagné. »*  
> *« Si je vois en un coup d'œil quels étudiants décrochent, ça change tout à mon suivi. »*

---

## 7. Différence clé avec le persona Léa (étudiant)

| Dimension | Léa (étudiant) | Mme Lefèvre (enseignant) |
|---|---|---|
| Motif d'usage | Réviser son propre cours | Générer des évaluations pour sa classe |
| Fréquence | 2–3 fois/semaine | 1–2 fois/mois par séquence |
| Critère bloquant | Qualité des questions / confidentialité | Conformité RGPD / fiabilité factuelle |
| Adoption | Individuelle, rapide | Institutionnelle, cycle long (DPO + direction) |
| Feature clé | Quiz + historique perso | Dashboard classe + export |
