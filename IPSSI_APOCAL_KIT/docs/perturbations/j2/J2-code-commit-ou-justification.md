# J2 — Code commité ou justification de non-bascule (temporaire)

## Projet

EduTutor IA — Groupe 21

## Contexte

Lors du bêta-test du 30/06/2026, un utilisateur a signalé un temps d’attente perçu comme trop élevé lors de la génération d’un quiz :

> « J'ai attendu 45 secondes pour avoir 10 questions. J'ai cru que le site était cassé. »

L’objectif fixé par le Product Owner est d’obtenir un temps de génération cible ≤ 15 secondes sur le cours de référence.

Une phase de benchmark a été lancée afin de comparer le modèle actuellement utilisé avec deux alternatives.

---

## Décision actuelle

Aucune bascule technique n’a été intégrée dans le code à ce stade.

Le groupe a choisi de :

1. Mesurer avant d’optimiser.
2. Produire un benchmark reproductible.
3. Valider la décision via ADR avant toute modification de l’architecture.

Cette décision évite :

* une régression fonctionnelle du MVP ;
* une intégration précipitée sans mesure ;
* un coût technique inutile.

---

## Travaux réalisés

### Investigation

* Définition du protocole de benchmark.
* Sélection de 3 modèles candidats.
* Mesure des performances sur le même cours de référence.
* Préparation de l’ADR de décision.

### Backlog mis à jour

Ajout des tâches :

* TECH-01 — Benchmark LLM (3 modèles)
* TECH-02 — Mesure latence p50 / p95
* TECH-03 — Évaluation qualité subjective
* TECH-04 — ADR décision modèle
* TECH-05 — Intégration si validation

---

## Condition de bascule

Une intégration sera réalisée uniquement si :

* temps médian ≤ 15 s ;
* qualité perçue ≥ 3/5 ;
* consommation mémoire compatible environnement cible ;
* impact acceptable sur les stories du Sprint.

---

## Trace Git

Aucun commit d’intégration modèle.

Les commits réalisés concernent uniquement :

* documentation benchmark ;
* ADR ;
* mise à jour Sprint Backlog.

La décision finale sera appliquée après validation du benchmark.

Statut : VALIDÉ POUR J2 (documentation uniquement)
