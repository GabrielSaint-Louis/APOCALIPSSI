# Plan d'audit sécurité — EduTutor IA
> PERTURBATION J3 · CONFORMITÉ / ÉTHIQUE  
> Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|---|---|
| **Équipe n°** | 21 |
| **Version** | v1.0 |
| **Date** | 01/07/2026 |
| **Objectif** | Identifier toutes les surfaces d'attaque potentielles de l'application, pas seulement l'injection découverte |

> 📁 Dépôt GitHub : `/docs/perturbations/j3/`

---

## POURQUOI UN PLAN D'AUDIT ?

La perturbation J3 a révélé une vulnérabilité par injection de prompt. La question que pose le professeur est : **y en a-t-il d'autres ?** Un plan d'audit structure la recherche systématique de vulnérabilités sur l'ensemble de l'application, pas uniquement sur le point d'entrée identifié.

---

## 1. Périmètre d'audit

### 1.1. Surfaces d'attaque identifiées

| Surface | Description | Priorité |
|---|---|---|
| **Endpoint génération quiz** | POST /api/quiz/generate — reçoit le texte cours et appelle le LLM | 🔴 Critique — déjà exploité |
| **Upload PDF** | POST /api/courses/upload — reçoit un fichier binaire | 🔴 Critique — vecteur de l'attaque J3 |
| **Authentification** | POST /api/auth/login, /api/auth/signup | 🟠 Haute |
| **Export données RGPD** | GET /api/accounts/me/export/ | 🟠 Haute — lié à J3-bis |
| **Back-office admin** | Interface d'administration Django | 🟡 Modérée |
| **Saisie texte libre** | Champ texte ≥ 200 caractères sur /upload | 🟠 Haute — même vecteur que PDF |

---

## 2. Familles de vulnérabilités à auditer

### 2.1. Vulnérabilités LLM (OWASP LLM Top 10)

| Référence | Vulnérabilité | Testé ? | Résultat |
|---|---|---|---|
| LLM-01 | Prompt Injection directe | ✅ Oui | Patché (couche 1+2) |
| LLM-01 | Prompt Injection indirecte (PDF) | ✅ Oui | Patché (couche 2) |
| LLM-01 | Jailbreak par rôle (DAN-like) | ✅ Oui | Patché (couche 1) |
| LLM-01 | Extraction system prompt | ✅ Oui | Patché (couche 1) |
| LLM-01 | Overflow JSON / désérialisation | ✅ Oui | Patché (couche 3) |
| LLM-02 | Insecure output handling | ⚠️ Partiel | Validation JSON — pas de sanitization HTML en sortie |
| LLM-06 | Sensitive information disclosure | ❌ Non testé | Le LLM pourrait reproduire des données sensibles du cours |

### 2.2. Vulnérabilités web classiques (OWASP Top 10)

| Référence | Vulnérabilité | Statut | Action |
|---|---|---|---|
| A01 | Broken Access Control | ⚠️ À vérifier | Tester accès aux données d'un autre user |
| A02 | Cryptographic Failures | ✅ Géré | Django hash mdp par défaut (PBKDF2) |
| A03 | Injection SQL | ✅ Géré | Django ORM — pas de SQL brut |
| A05 | Security Misconfiguration | ⚠️ À vérifier | DEBUG=True en prod ? SECRET_KEY exposée ? |
| A07 | Auth failures | ⚠️ À vérifier | Pas de rate limiting sur /login |
| A10 | SSRF | ❌ Non testé | L'upload URL (US-14) pourrait être exploitée |

---

## 3. Tests à réaliser par priorité

### 3.1. Tests immédiats (avant livraison MVP mercredi 17h45)

| Test | Description | Responsable |
|---|---|---|
| T-SEC-01 | Vérifier que l'export RGPD ne retourne que les données du user authentifié | Gabriel |
| T-SEC-02 | Vérifier que le back-office admin n'est pas accessible sans compte staff | Nicolas |
| T-SEC-03 | Vérifier que DEBUG=False en production Docker | Nolan |
| T-SEC-04 | Vérifier que la SECRET_KEY Django n'est pas dans le repo GitHub | Nicolas |
| T-SEC-05 | Les 5 tests adversariaux LLM passent après le patch | Nolan |

### 3.2. Tests post-MVP (Release 2 ou Release 3)

| Test | Description |
|---|---|
| T-SEC-06 | Rate limiting sur /api/auth/login (max 5 tentatives/minute) |
| T-SEC-07 | Test de fuite inter-comptes sur tous les endpoints authentifiés |
| T-SEC-08 | Audit de la surface d'upload URL si US-14 est développée |
| T-SEC-09 | Sanitization HTML de la sortie LLM avant affichage React |
| T-SEC-10 | Test LLM-06 : reproduction de données sensibles du cours source |

---

## 4. Résultats de l'audit J3 — synthèse

| Famille | Vulnérabilités trouvées | Patchées | Résiduelles |
|---|---|---|---|
| LLM Injection | 5 | 5 | 2 (sémantique + multi-langues) |
| Access Control | À vérifier | — | — |
| Config sécurité | À vérifier | — | — |
| Auth | Pas de rate limiting | 0 | 1 |

> **Conclusion** : la surface d'attaque principale (LLM injection) est traitée. Les surfaces web classiques nécessitent une passe de vérification avant la livraison MVP.

---

## 📚 Références

- OWASP LLM Top 10 2025 : https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP Top 10 Web 2021 : https://owasp.org/www-project-top-ten/
- AI Act EU — Article 15 : robustesse des systèmes IA à haut risque
