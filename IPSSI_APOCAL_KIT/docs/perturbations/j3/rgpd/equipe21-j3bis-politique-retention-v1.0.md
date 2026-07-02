# Politique de rétention des données — EduTutor IA

**Document :** equipe21-j3bis-politique-retention-v1.0.md

**Projet :** EduTutor IA

**Équipe :** Groupe 21

**Version :** v1.0

**Date :** 01/07/2026

**Statut :** Livrable J3-bis — RGPD

---

# 1. Objectif du document

Cette politique définit les règles de conservation, d’archivage et de suppression des données personnelles collectées dans le cadre du fonctionnement de la plateforme EduTutor IA.

L’objectif est de garantir :

* le respect du Règlement Général sur la Protection des Données (RGPD) ;
* la limitation de conservation des données ;
* la transparence vis-à-vis des utilisateurs ;
* la mise en œuvre du droit d’accès (Art. 15), du droit à l’effacement (Art. 17) et du droit à la portabilité (Art. 20).

Cette politique s’applique à tous les utilisateurs de la plateforme :

* Étudiant·e·s ;
* Enseignant·e·s ;
* Administrateurs internes.

---

# 2. Principes de conservation

EduTutor IA applique les principes suivants :

## Minimisation

Seules les données nécessaires au fonctionnement du service sont collectées.

## Limitation temporelle

Chaque catégorie de données possède une durée de conservation définie.

## Sécurité

Les données sont stockées dans des environnements protégés avec contrôle d’accès.

## Suppression automatique

Les données expirées sont supprimées automatiquement selon une politique planifiée.

## Traçabilité

Chaque demande d’export ou suppression est enregistrée dans un journal d’audit.

---

# 3. Durées de conservation par type de donnée

| Catégorie              | Données concernées                                  |                        Durée | Déclencheur        |
| ---------------------- | --------------------------------------------------- | ---------------------------: | ------------------ |
| Compte utilisateur     | Email, identifiant, date d’inscription, préférences | Tant que le compte est actif | Suppression compte |
| Authentification       | Hash mot de passe, sessions                         |    Session active + 90 jours | Expiration         |
| Cours importés         | PDF, texte collé, métadonnées                       |  12 mois après dernier accès | Inactivité         |
| Quizz générés          | Questions, réponses attendues                       |                      24 mois | Date génération    |
| Réponses utilisateur   | Réponses, score, temps                              |                      24 mois | Date tentative     |
| Historique progression | Statistiques, tableaux                              |                      24 mois | Dernière activité  |
| Logs techniques        | Connexions, erreurs, traces API                     |                      12 mois | Date création      |
| Journaux sécurité      | Tentatives suspectes                                |                      12 mois | Date création      |
| Signalements           | Feedback, anomalies                                 |                      36 mois | Clôture dossier    |
| Exports RGPD           | Fichier généré                                      |                     30 jours | Génération export  |
| Audit SAR              | Historique demandes RGPD                            |                      36 mois | Clôture demande    |
| Sauvegardes            | Backups techniques                                  |            Rotation 90 jours | Remplacement       |

---

# 4. Bases légales du traitement (RGPD Article 6)

Chaque traitement repose sur une base juridique explicite.

| Traitement                | Finalité                | Base légale          |
| ------------------------- | ----------------------- | -------------------- |
| Création de compte        | Fournir le service      | Exécution du contrat |
| Connexion                 | Sécurité du compte      | Intérêt légitime     |
| Upload de cours           | Génération de quizz     | Exécution du contrat |
| Historique de progression | Suivi pédagogique       | Exécution du contrat |
| Statistiques produit      | Amélioration du service | Intérêt légitime     |
| Logs techniques           | Diagnostic et sécurité  | Intérêt légitime     |
| Exports RGPD              | Réponse aux demandes    | Obligation légale    |
| Suppression de compte     | Droit à l’effacement    | Obligation légale    |
| Détection d’abus          | Protection du service   | Intérêt légitime     |

---

# 5. Modalités de suppression (Article 17 — Droit à l’effacement)

Un utilisateur peut demander :

* suppression de son compte ;
* suppression des contenus uploadés ;
* suppression des résultats de quizz ;
* suppression des exports générés.

La suppression suit le processus suivant :

### Étape 1 — Demande utilisateur

Demande via :

* page profil ;
* formulaire support ;
* demande RGPD.

### Étape 2 — Vérification

Validation de l’identité de l’utilisateur connecté.

### Étape 3 — Mise en attente

Le compte passe en statut :

```
pending_deletion
```

Durée :
**30 jours calendaires**

Objectif :

* permettre une récupération en cas d’erreur.

### Étape 4 — Purge automatique

Exécution planifiée :

```bash
cron: purge_deleted_accounts_daily
```

Actions :

* suppression compte ;
* suppression cours ;
* suppression quizz ;
* suppression réponses ;
* suppression historique ;
* anonymisation des logs.

### Étape 5 — Confirmation

Email envoyé :

> « Vos données ont été supprimées conformément à l’Article 17 du RGPD. »

---

# 6. Export et portabilité (Articles 15 et 20)

EduTutor IA permet l’export automatisé :

Endpoint :

```http
GET /api/accounts/me/export/
```

Formats disponibles :

* JSON
* CSV
* ZIP (optionnel)

L’export inclut :

* données du compte ;
* cours importés ;
* quizz générés ;
* réponses ;
* scores ;
* signalements ;
* logs d’audit.

Le fichier exporté reste disponible :

**30 jours maximum**

Puis suppression automatique.

---

# 7. Audit des demandes RGPD (SAR)

Toutes les demandes sont enregistrées.

Modèle :

```text
DataRequest
```

Champs :

```text
id
user_id
request_type
requested_at
status
responded_at
export_hash
```

États possibles :

```text
RECEIVED
IN_PROGRESS
COMPLETED
REJECTED
```

Objectifs :

* preuve de conformité ;
* traçabilité ;
* audit interne.

---

# 8. Mesures de sécurité associées

Les données conservées sont protégées par :

* chiffrement des mots de passe ;
* contrôle d’accès authentifié ;
* HTTPS ;
* limitation des permissions ;
* journalisation des accès ;
* validation des exports ;
* suppression automatique programmée.

---

# 9. Révision de cette politique

Cette politique est revue :

* à chaque release majeure ;
* après incident sécurité ;
* après changement réglementaire.

Version actuelle : 
**v1.0 — 01/07/2026**

