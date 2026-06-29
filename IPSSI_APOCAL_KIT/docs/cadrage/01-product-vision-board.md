# Product Vision Board — EduTutor IA

> Artefact de cadrage · Release 1 · 29/06/2026

---

## 1. Vision

**Pour** les étudiant·e·s du supérieur  
**Qui** veulent réviser efficacement à partir de leurs propres cours  
**EduTutor IA** est une application web de génération de quiz  
**Qui** transforme automatiquement un PDF ou un texte en QCM corrigés instantanément  
**Contrairement à** Quizlet AI ou Wilgo  
**Notre produit** s'appuie sur un LLM local (Ollama), garantit la souveraineté des données et respecte le RGPD sans compromis

---

## 2. Cible

| Segment | Description |
|---|---|
| **Primaire** | Étudiant·e du supérieur (L1–M2), révise seul·e, utilise ses propres cours |
| **Secondaire (Release 2)** | Enseignant·e du supérieur / lycée, veut générer des supports d'évaluation |

---

## 3. Besoins utilisateurs

- Transformer un cours (PDF ou texte) en quiz sans effort
- Obtenir une correction immédiate et un score
- Retrouver l'historique de ses révisions
- Avoir confiance dans la confidentialité de ses données

---

## 4. Proposition de valeur

| Axe | Valeur |
|---|---|
| **Rapidité** | Quiz généré en moins de 60 secondes |
| **Pertinence** | Questions ancrées dans le contenu fourni, pas génériques |
| **Souveraineté** | LLM local Ollama — aucune donnée ne quitte le serveur |
| **RGPD** | Conformité native, cible B2B éducation française |

---

## 5. Fonctionnalités clés (Release 1 — MVP)

| ID | Fonctionnalité |
|---|---|
| F1 | Inscription / connexion email, validation, reset mot de passe, profil |
| F2 | Saisie d'un cours : upload PDF ≤ 5 Mo ou texte ≥ 200 caractères |
| F3 | Génération automatique de 10 QCM via LLM local |
| F4 | Soumission et correction automatique |
| F5 | Affichage score /10 + détail bonnes/mauvaises réponses |
| F6 | Historique persisté des quizz (date, cours, score) |

---

## 6. Objectifs business

- Livrer un MVP démontrable d'ici mercredi 01/07 17h45
- Valider la faisabilité technique Ollama local en conditions réelles
- Préparer 2–3 pistes Release 2 différenciantes (RAG, mode enseignant, etc.)

---

## 7. Contraintes & risques

| Contrainte | Impact |
|---|---|
| LLM local Ollama imposé | Latence potentielle — benchmark J2 obligatoire |
| RGPD / données UE | Pages légales à compléter, endpoint SAR à implémenter |
| Base brownfield inégale | Audit de l'existant avant tout développement |
| Deadline stricte 17h45 mer. | Priorisation MoSCoW non négociable |
