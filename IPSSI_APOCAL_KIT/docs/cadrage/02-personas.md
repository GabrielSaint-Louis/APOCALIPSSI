# Personas — EduTutor IA

> Artefact de cadrage · Release 1 · 29/06/2026

---

## Persona 1 — Étudiant·e (cible primaire)

**Prénom fictif :** Camille  
**Âge :** 21 ans  
**Profil :** Étudiante en L3 Droit à Paris II, révise seule, charge de cours dense

### Contexte
Camille a des partiels dans 3 semaines. Elle accumule des PDFs de cours mais ne sait pas par où commencer pour réviser. Elle utilise déjà ChatGPT pour résumer ses cours, mais perd confiance quand les réponses semblent inexactes.

### Objectifs
- Tester ses connaissances rapidement sur un chapitre précis
- Identifier ses lacunes avant l'exam
- Gagner du temps : pas de fiche à créer manuellement

### Frustrations
- Les quiz génériques ne correspondent pas à son cours
- Elle ne sait pas si l'IA a "inventé" des questions
- Peur de perdre ses données personnelles sur des apps US

### Citation
> *"Je veux réviser MON cours, pas un résumé générique trouvé sur internet."*

### Usage attendu
- Upload son PDF de cours → génère un quiz → vérifie son score → recommence sur un autre chapitre
- Session type : 15–20 min, 2–3 fois par semaine

---

## Persona 2 — Mme Lefèvre (cible secondaire, Release 2)

**Prénom fictif :** Isabelle Lefèvre  
**Âge :** 44 ans  
**Profil :** Professeure de SVT en lycée, 15 ans d'expérience, peu à l'aise avec les outils numériques avancés

### Contexte
Isabelle passe des heures à préparer des évaluations. Elle a entendu parler des outils IA mais se méfie des hallucinations et de la conformité légale. Son établissement lui demande de rester sur des outils conformes RGPD.

### Objectifs
- Générer rapidement des questions d'évaluation à partir de ses propres supports
- Avoir des questions fiables, traçables à une source
- Ne pas exposer les données de ses élèves

### Frustrations
- Les outils US (ChatGPT, Quizlet) ne sont pas conformes RGPD
- Elle ne veut pas réécrire toutes ses questions depuis zéro
- Manque de temps pour apprendre un nouvel outil complexe

### Citation
> *"Si l'outil invente des erreurs factuelles, je ne peux pas le donner à mes élèves."*

### Usage attendu
- Upload support pédagogique → génère 10 questions → exporte ou copie pour son évaluation
- Utilisation ponctuelle (1–2 fois par mois par séquence)

---

## Persona 3 — Administrateur EduTutor

**Prénom fictif :** Thomas  
**Âge :** 32 ans  
**Profil :** Développeur / ops interne, gère la plateforme

### Objectifs
- Configurer le LLM (modèle, provider) via le back-office
- Gérer les utilisateurs (suspension, suppression)
- Monitorer la qualité des générations

### Usage attendu
- Accès back-office admin
- Seed / reset de la base en dev
- Configuration Ollama / Brevo
