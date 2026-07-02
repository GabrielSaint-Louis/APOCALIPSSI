# ADR-0002 — Passage d’une stack locale fonctionnelle à une architecture scalable et autoscalable

> PERTURBATION J4 · ADR TECHNIQUE
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum
> Auteur : Monica RADIFERA · Licence CC BY-NC-SA 4.0

---

## IDENTIFICATION DU DOCUMENT

| Champ          | Valeur                                                                               |
| -------------- | ------------------------------------------------------------------------------------ |
| **Numéro ADR** | ADR-0002                                                                             |
| **Titre**      | Passage d’une stack locale fonctionnelle à une architecture scalable et autoscalable |
| **Statut**     | ☑ Accepté                                                                            |
| **Date**       | 02/07/2026 12h03                                                                     |
| **Auteurs**    | Monica RADIFERA + équipe                                                             |
| **Version**    | v1.0                                                                                 |
| **Supersedes** | Aucun                                                                                |

> 💡 Convention : un ADR doit tenir en 1 à 2 pages maximum.

---

## 1. Contexte

EduTutor IA doit passer d’une stack locale fonctionnelle à une architecture capable de supporter une montée en charge forte, avec une cible d’évolution de type 10 utilisateurs/jour vers 15 000 utilisateurs/jour. Le projet dispose désormais d’un budget supérieur, ce qui permet de viser une infrastructure plus robuste, une meilleure répartition des responsabilités et une vraie stratégie de montée en charge.

La stack de départ repose sur Django, React Vite, PostgreSQL via Docker, Llama 3.1 8B via Ollama par défaut, pypdf et `docker compose up`. Ces briques restent pertinentes, mais elles ne suffisent pas seules à absorber une forte croissance de trafic si elles restent exécutées comme une simple application locale. La décision doit donc porter sur le mode d’exécution, l’orchestration et la capacité à répliquer les composants.

---

## 2. Objectif technique

L’objectif n’est pas de changer les briques principales, mais de les faire fonctionner dans une architecture capable de :

- répliquer les services web ;
- isoler les traitements lourds ;
- protéger le LLM local contre les pics de charge ;
- absorber les écritures et lectures de façon stable ;
- maintenir un démarrage local simple ;
- préparer une montée en charge progressive sans refonte globale.

---

## 3. Décision

**Décision : conserver les briques imposées, mais changer le mode d’exécution en visant une architecture conteneurisée, orchestrée et autoscalable.**

### Architecture cible

- **Django** devient le point d’entrée métier et l’orchestrateur fonctionnel.
- **React Vite** reste le front stateless et réplicable.
- **PostgreSQL** reste la base centrale.
- **pypdf** reste le moteur d’extraction de contenu.
- **Ollama / Llama 3.1 8B** reste le LLM par défaut, mais isolé comme ressource limitée.
- **Docker** reste la couche de conteneurisation.
- **Docker Compose** reste le mode local, mais l’architecture doit être directement transposable vers une orchestration plus robuste.
- **Kubernetes** devient la cible d’exécution pour la production scalable.
- **HPA** est retenu pour la montée en charge horizontale des services stateless.
- **Cluster Autoscaler** est retenu pour l’augmentation ou la réduction automatique des ressources du cluster selon la demande.

---

## 4. Pourquoi ce choix

### 4.1 Garder les briques existantes

Les briques actuelles sont cohérentes avec le produit et déjà adaptées au besoin métier. Les remplacer n’apporterait pas un gain proportionnel au coût de migration. Le point faible n’est pas la stack elle-même, mais son mode d’exécution actuel.

### 4.2 Passer à une orchestration réelle

Pour passer à une vraie montée en charge, il faut que les composants soient :

- **stateless quand c’est possible** ;
- **réplicables** ;
- **séparés par responsabilité** ;
- **pilotés par des mécanismes d’autoscaling**.

L’orchestration n’est donc pas décorative : elle garantit que la charge ne repose pas sur une seule instance Django ou sur une seule machine exécutant le LLM.

### 4.3 Django comme chef d’orchestre

Django garde le rôle de coordination métier, mais n’exécute plus tout de manière couplée. Le flux devient :

1. réception de la demande ;
2. extraction du contenu ;
3. préparation des données ;
4. appel au LLM local ;
5. validation de la sortie ;
6. persistance en base ;
7. restitution au front.

Ce découpage permet de mesurer chaque étape, de l’isoler et de la faire évoluer indépendamment.

### 4.4 Scaler ce qui peut l’être

Le front, l’API et les workers doivent pouvoir être répliqués horizontalement. PostgreSQL reste central mais doit être préparé pour la montée en charge via indexation, supervision et éventuellement séparation des lectures selon l’évolution de la charge. Le LLM local ne doit pas devenir le point de blocage : il doit être encapsulé et protégé par l’orchestration.

---

## 5. Ce qui change

### 5.1 Avant

- Exécution locale principalement pensée pour fonctionner.
- Démarrage unifié via `docker compose up`.
- Charge potentiellement supportée par une seule instance logique.
- LLM local utilisé comme ressource centrale sans mécanisme de protection de charge.

### 5.2 Après

- Architecture conteneurisée prête pour l’orchestration.
- Front et API réplicables.
- Traitements lourds isolés.
- LLM local encapsulé comme composant limité et surveillé.
- Base de données conservée comme socle transactionnel.
- Possibilité d’augmenter les pods/instances selon la charge.

---

## 6. Choix techniques détaillés

### 6.1 Frontend

React Vite reste stateless afin de pouvoir être répliqué sans contrainte fonctionnelle. Cela permet de multiplier les instances front sans impact sur les données métier.

### 6.2 Backend

Django reste le cœur métier, mais il doit être organisé pour être déployé en plusieurs instances derrière un service stable. Il ne doit pas conserver d’état de session local bloquant la réplication.

### 6.3 Données

PostgreSQL reste la base de référence. Pour absorber la charge, il doit être dimensionné correctement, indexé, supervisé, et intégré à une stratégie de sauvegarde et de reprise.

### 6.4 Extraction et génération

pypdf et le LLM ne doivent pas rester dans le chemin critique d’un traitement monolithique. L’extraction et la génération doivent pouvoir être pilotées comme des étapes distinctes, et idéalement déplacées vers un mécanisme de traitement différé si la charge augmente.

### 6.5 Orchestration

Kubernetes est retenu pour la production scalable car il permet :

- la réplication des déploiements ;
- le redémarrage automatique des composants ;
- l’autoscaling horizontal avec HPA ;
- l’augmentation des ressources du cluster avec Cluster Autoscaler ;
- la séparation claire entre local de développement et exécution de production.

---

## 7. Mécanisme de montée en charge

La montée en charge est gérée à trois niveaux :

### 7.1 Niveau applicatif

- Réplication du backend Django.
- Réplication du front React.
- Maintien d’un flux métier sans état local bloquant.

### 7.2 Niveau orchestration

- HPA ajuste le nombre de pods selon la charge CPU/mémoire ou métriques adaptées.
- Les composants stateless montent ou descendent en nombre selon le trafic.
- Les services exposés restent stables via des Services Kubernetes.

### 7.3 Niveau cluster

- Cluster Autoscaler ajuste le nombre de nœuds selon la demande réelle.
- Cela permet d’absorber des pics de charge sans surdimensionner en permanence.
- Le coût reste plus contrôlé que surdimensionner l’infrastructure à l’avance.

---

## 8. Alternatives rejetées

| Option                                               | Raison du rejet                                                                                          |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Rester uniquement sur Docker Compose**             | Suffisant pour le local, insuffisant pour une vraie montée en charge.                                    |
| **Changer toute la stack**                           | Trop coûteux, trop risqué, pas nécessaire.                                                               |
| **Garder une seule instance de chaque composant**    | Crée des goulots d’étranglement et limite la disponibilité.                                              |
| **Déporter immédiatement tout le LLM vers le cloud** | Réduit la maîtrise locale, ajoute une dépendance externe et n’est pas nécessaire pour le besoin de base. |

---

## 9. Conséquences

### Positives

- montée en charge horizontale possible ;
- meilleure disponibilité ;
- meilleure isolation des composants ;
- limite les effets domino ;
- préparation à un trafic fortement accru ;
- architecture plus crédible pour un passage à l’échelle.

### Négatives

- complexité de déploiement plus élevée ;
- besoin de surveillance et de métriques ;
- surcoût d’exploitation ;
- nécessité d’une vraie discipline d’orchestration ;
- plus de rigueur sur les interfaces entre briques.

### Mesures de maîtrise

- journaliser les étapes critiques ;
- exposer des métriques de charge ;
- surveiller la saturation CPU, mémoire et requêtes ;
- garder la possibilité de démarrer en local via Compose ;
- documenter toute évolution majeure par ADR.

---

## 10. À surveiller

| KPI                          | Seuil cible                           | Seuil d’alerte          | Action si dépassement                        |
| ---------------------------- | ------------------------------------- | ----------------------- | -------------------------------------------- |
| Temps de génération du quiz  | < 60 s                                | > 60 s                  | Déclencher optimisation / traitement différé |
| Temps de réponse API         | < 500 ms sur charge nominale          | > 1 s                   | Augmenter les réplicas ou optimiser Django   |
| Utilisation mémoire          | Stable sur 16 Go en local             | Dépassement fréquent    | Réduire la charge ou isoler davantage        |
| Disponibilité service        | > 99 %                                | < 97 %                  | Corriger l’orchestration                     |
| Capacité de montée en charge | Réplicas augmentables automatiquement | Saturation sans scaling | Revoir HPA / métriques / architecture        |

---

## 11. Revue de la décision

Cette décision devra être revue après tests de charge réels et après mesure de la capacité à supporter une charge nettement supérieure au niveau de départ. Toute modification du fournisseur LLM, du mode de traitement IA ou du socle d’orchestration devra faire l’objet d’un ADR supplémentaire.

---

## 12. Références

- Contraintes de fonctionnement du projet.
- Exigences de performance et de compatibilité mémoire.
- Gouvernance des changements LLM par ADR.
- Principes d’orchestration et d’autoscaling des workloads.
