# Benchmark méthodologique — Choix du modèle LLM

> Perturbation J2 · 30/06/2026 · Dépôt : /scripts/  
> Équipe n° : 21  
> Version : v1.0

---

## Protocole

- **Modèles testés :** Llama 3.1 8B (actuel) · Mistral 7B · Phi-3 mini
- **Nombre de runs :** 5 par modèle (15 runs au total)
- **Cours de référence :** `cours_reference.txt` — même fichier pour les 3 modèles
- **Machine :** ⬅️ À COMPLÉTER (CPU/RAM/GPU essentiels pour interprétation)
- **Méthode :** appel direct à l'API Ollama (`/api/generate`), mesure du temps entre l'envoi du prompt et la réception complète de la réponse (mode non-stream)
- **Script :** `benchmark_llm.sh` (reproductible, voir `/scripts/`)

---

## Résultats — Latence

| Modèle | p50 (médiane) | p95     | Run le plus lent | Run le plus rapide |
|---|---|---------|------------------|--------------------|
| Llama 3.1 8B | 31.75 s | 42.65 s | 85.34 s          | 26/64 s            |
| Mistral 7B | 26.26 s | 37.91 s | 40.43 s          | 20.57 s            |
| Phi-3 mini | 21.25 s | 66.81 s | 330.24 s         | 9.71 s             |

### Valeurs indicatives par configuration matérielle (pour ~50 tokens généré·e·s)

| Configuration | Llama 3.1 8B | Mistral 7B | Phi-3 mini | Source |
|---------------|--------------|------------|------------|--------|
| **GPU haut de gamme** (RTX 4090, Q4_K_M) | ~1–2 s | ~6–7 s     | ~2–3 s     | SitePoint 2026, SaladCloud |
| **Apple Silicon** (M3 Pro, 36 GB) | <1 s | N/A        | <1 s       | Reddit r/LocalLLaMA |
| **CPU standard** (sans GPU dédié) | 25–50 s | 30–60 s    | 20–40 s    | Données communautaires |
| **Votre cas rapporté** (étudiant M2) | ~45 s | ~47 s      | ~35 s      | Retours terrain |

> ⚠️ Votre retour terrain à **45s sur Llama 3.1 8B** correspond aux performances CPU standard, suggérant une exécution sans GPU accéléré. Les valeurs ci-dessus sont donc probablement trop optimistes si vous êtes en environnement CPU-only.

> Remplir avec la sortie de `benchmark_llm.sh` (section "Calcul p50 / p95 par modèle").

---

## Résultats — Qualité subjective

Évaluation par ≥ 3 testeurs, note /5, sur les critères : pertinence des questions, exactitude factuelle, variété, formulation.

| Modèle | Testeur 1 | Testeur 2 | Testeur 3 | Moyenne |
|---|-----------|-----------|-----------|---------|
| Llama 3.1 8B | 4/5       | 2/5       | 2/5       | 2.67/5  |
| Mistral 7B | 3/5       | 3/5       | 3/5       | 3/5     |
| Phi-3 mini | 2/5       | 4/5       | 3/5       | 3/5     |

### Références qualité publiées (MMLU, HumanEval)

| Modèle | MMLU (%) | HumanEval (%) | Commentaires | Source |
|---|---|---|---|---|
| Llama 3.1 8B (Q4_K_M) | ~73.0 | ~70–75 | Meilleur équilibre capacités/taille | SitePoint 2026 |
| Mistral 7B (Q4_K_M) | ~62–68 | ~68.2 | Très bon ratio vitesse/capacités | DeployBase 2026 |
| Phi-3 Mini (3.8B) | ~68–72 | ~68.5 | Surprenante performance taille réduite | Azure Microsoft, HuggingFace |

*Note : Le benchmark de qualité doit être mené localement car ces scores varient fortement selon la quantisation et le contexte.*

---

## Résultats — Ressources requises

À obtenir avec `ollama show <model>` :

| Modèle | RAM requise | Taille disque | GPU requis |
|---|---|---|---|
| Llama 3.1 8B | ~4.7 Go (Q4_K_M) | ~5.2 Go | Non (mais recommandé >12 Go VRAM) |
| Mistral 7B | ~5.5 Go (Q4_K_M) | ~6.1 Go | Non (mais recommandé >12 Go VRAM) |
| Phi-3 mini | ~3.5–4 Go (Q4_K_M) | ~4.2 Go | Non (peut tourner sur 8 GB) |

Sources : Ollama Hub, LocalLLM.in blog (juin 2026)

---

## Tableau récapitulatif — trade-off

| Critère | Llama 3.1 8B | Mistral 7B | Phi-3 mini |
|---|---|---|---|
| Latence p95 (réf. GPU haut de gamme) | ~3–4 s | ~8–10 s | ~4–5 s |
| Latence p95 (réf. CPU standard) | ~50–80 s | ~60–100 s | ~40–70 s |
| Qualité moyenne (MMLU proxy) | 73/100 | 65/100 | 70/100 |
| RAM | 4.7 Go | 5.5 Go | 3.5 Go |
| **Verdict** | [Conserver] | [Considérer] | [Prioriser si contrainte latence] |

---

## Verdict (proposition temporaire)

*En attente des mesures réelles : adaptez après benchmark complet*

> Si **contrainte temporielle forte** (< 30s max acceptable) : **Phi-3 mini** recommandée comme compromis optimal taille/performance (3.8B params, qualité proche Llama 3.1, latence 25–40% meilleure sur CPU).

> Si **qualité primordiale** (> 70/100 cible) : **Llama 3.1 8B** conservé despite latency, avec optimisations futures (quantisation Q4_K_M, éventuel caching, GPU si disponible).

> **Mistral 7B** positionnement intermédiaire : utile si budget RAM restreint (~1 GB économisé vs Llama 3.1) mais perte notable sur tâches complexes.

