# Audit Trail des demandes RGPD (SAR) — EduTutor IA

**Projet :** EduTutor IA  
**Équipe :** Groupe 21  
**Document :** equipe21-j3bis-sar-audit-trail-v1.0.md  
**Version :** v1.0  
**Date :** 01/07/2026  
**Statut :** J3-bis — RGPD

---

# 1. Objectif

Ce document définit le mécanisme d’audit trail des demandes RGPD (SAR) pour garantir :

- la traçabilité complète des demandes utilisateur
- la conformité au RGPD (Articles 15, 16, 17, 20)
- la preuve de traitement en cas de contrôle
- la sécurité et l’intégrité des exports de données

---

# 2. Périmètre

Sont concernées toutes les demandes liées aux données personnelles :

- droit d’accès (Art. 15)
- droit de rectification (Art. 16)
- droit à l’effacement (Art. 17)
- droit à la portabilité (Art. 20)

---

# 3. Principe général

Chaque demande RGPD génère automatiquement une entrée persistée en base.

Aucune demande ne peut être traitée sans enregistrement préalable dans l’audit trail.

---

# 4. Modèle de données (DataRequest)

Chaque demande est enregistrée avec les informations suivantes :

- identifiant unique de la demande
- utilisateur concerné
- type de demande
- date de création
- statut de traitement
- date de réponse
- format d’export (JSON / CSV / ZIP)
- hash du fichier exporté
- adresse IP et user-agent
- notes internes éventuelles

---

# 5. Cycle de vie d’une demande

Une demande SAR suit le flux suivant :

RECEIVED → IN_PROGRESS → COMPLETED  
ou  
RECEIVED → IN_PROGRESS → REJECTED

### Description des statuts

- RECEIVED : demande enregistrée
- IN_PROGRESS : traitement en cours
- COMPLETED : demande traitée et export fournie
- REJECTED : demande invalide ou non authentifiée

---

# 6. Traitement d’une demande

## Étape 1 — Création
La demande est créée automatiquement lors de la requête utilisateur.

## Étape 2 — Vérification
Contrôle de l’identité et validation de la session utilisateur.

## Étape 3 — Collecte des données
Récupération des données liées à l’utilisateur :

- compte
- cours importés
- quiz générés
- réponses et scores
- logs associés

## Étape 4 — Génération de l’export
Les données sont structurées au format JSON ou CSV.

## Étape 5 — Vérification d’intégrité
Un hash SHA-256 est généré pour garantir l’intégrité du fichier.

## Étape 6 — Finalisation
La demande est marquée comme complétée et archivée.

---

# 7. Sécurité et contrôle d’accès

- accès réservé à l’utilisateur propriétaire
- accès admin et DPO uniquement pour audit
- chiffrement des exports
- communication HTTPS obligatoire
- logs non modifiables

---

# 8. Journalisation des événements

Chaque action est enregistrée :

- création de demande
- validation
- traitement
- génération d’export
- finalisation ou rejet

---

# 9. API associée

Endpoint principal :

GET /api/accounts/me/export/

Réponse :

- données utilisateur
- cours
- quiz
- réponses
- logs
- historique des demandes

---

# 10. Traçabilité et conformité

Ce système permet :

- conformité RGPD complète
- preuve de traitement
- audit CNIL en cas de contrôle
- transparence utilisateur

---

# 11. Limites connues

- anonymisation avancée non encore implémentée
- suppression distribuée non automatisée
- signature électronique des exports non incluse

---

# 12. Conclusion

Le système d’audit trail garantit :

- traçabilité complète
- sécurité des données
- conformité RGPD
- robustesse en cas d’audit

---
