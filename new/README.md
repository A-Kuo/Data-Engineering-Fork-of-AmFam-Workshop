# AI Security & Safety Benchmarking: Research-Grade Evaluation Framework

An extension of the [MadData 2026 AmFam Workshop](../README.md) that applies the same RAG and LLM techniques to the critical domain of **AI security evaluation, adversarial robustness, and defense-in-depth pipelines**. These notebooks are designed to meet the rigor expected in empirical AI safety research, with formal threat models, statistical analysis, and calibrated evaluation methodology.

## Notebooks

| Notebook | Mirrors | Research Focus |
|----------|---------|---------------|
| `ai_safety_evals_demo.ipynb` | `hugging_face_chromadb_demo.ipynb` | Embedding-space anomaly detection for adversarial prompt classification |
| `ai_security_benchmarking_demo.ipynb` | `gemini_rag_pipeline_demo.ipynb` | Calibrated LLM-as-a-safety-judge with defense pipeline ablation |

## Research methodology

### Notebook 1: Embedding-Space Anomaly Detection

**Formal threat model** with adversary capability levels (L0-L3), defender constraints (latency, FPR, updatability).

**Three detection methods** with comparative analysis:
- Centroid cosine similarity
- Mahalanobis distance (Ledoit-Wolf covariance shrinkage)
- Isolation forest (one-class anomaly detection)

**Rigorous evaluation**:
- ROC/AUC and Precision-Recall curves (threshold-independent)
- Bootstrap confidence intervals (n=1000) for all AUC estimates
- Stratified 5-fold cross-validation for threshold selection
- Fisher's discriminant ratio for separability diagnostics
- KL divergence for information-theoretic category analysis
- Ablation study across all method combinations
- Adversarial robustness testing (character obfuscation, paraphrase, multilingual)

### Notebook 2: Calibrated Safety Evaluation

**Formal safety specification** with measurable properties (Safety Rate, Attack Success Rate, False Refusal Rate, Violation Severity Score).

**Judge calibration**:
- Multi-invocation agreement analysis (N=3 per test case)
- Cohen's kappa for inter-rater reliability
- Confidence-consistency correlation analysis

**Defense-in-depth pipeline** with per-layer ablation:
- 9 configurations tested (from no defense to full 4-layer pipeline)
- Marginal contribution and interaction effects measured
- Safety Rate vs. False Refusal Rate tradeoff analysis

**Statistical rigor**:
- Wilson score confidence intervals on all benchmark proportions
- CWE-aligned vulnerability reports for enterprise security teams
- Multi-turn attack generation (conversation-level red teaming)

## Key techniques from AI security industry

Extracted from analysis of [Anthropic's AI security roles](https://www.anthropic.com/careers/jobs) (7 job postings scraped):

| Technique | Notebook | Industry Role |
|-----------|----------|---------------|
| Embedding-based anomaly detection | NB1 | Applied Safety Research Engineer |
| Mahalanobis distance / covariance methods | NB1 | ML/Research Engineer, Safeguards |
| Adversarial robustness testing | NB1 | AI Security Fellow |
| Automated red teaming (single + multi-turn) | NB2 | Frontier Red Team (Cyber) |
| LLM-as-a-safety-judge with calibration | NB2 | Applied Safety Research Engineer |
| Defense-in-depth pipeline | NB2 | Safeguards team architecture |
| Statistical benchmarking with CIs | NB2 | Research Scientist (Emerging Risks) |
| CWE-aligned vulnerability reports | NB2 | Enterprise security integration |

## Setup

```bash
cd ..
uv sync
```

### Run order
1. `ai_safety_evals_demo.ipynb` (creates ChromaDB attack pattern collection with detection metadata)
2. `ai_security_benchmarking_demo.ipynb` (loads the collection, extends it with red team results)

### Environment variables
Notebook 2 requires Gemini/Vertex AI credentials:
```
GCP_PROJECT=your-project-id
GCP_LOCATION=your-location
```

## References

- Greshake et al. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.* arXiv:2302.12173
- Perez et al. (2022). *Red Teaming Language Models with Language Models.* arXiv:2202.03286
- Zheng et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* NeurIPS 2023
- Mazeika et al. (2024). *HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal.* ICML 2024
- Jain et al. (2023). *Baseline Defenses for Adversarial Attacks Against Aligned Language Models.* arXiv:2309.00614
- Alon & Kamfonas (2023). *Detecting Language Model Attacks with Perplexity.* arXiv:2308.14132
- Landis & Koch (1977). *The Measurement of Observer Agreement for Categorical Data.* Biometrics 33(1)

## Architecture parallel

| Original Workshop | Security Workshop | Shared Pattern |
|-------------------|-------------------|----------------|
| Embed textbook pages | Embed adversarial prompts | Sentence Transformers |
| t-SNE of OS topics | t-SNE with sophistication overlay | Embedding visualization |
| Custom VectorDatabase | 3-method ensemble detector | Cosine similarity + Mahalanobis + Isolation Forest |
| ChromaDB for RAG | ChromaDB for threat scoring | Persistent vector store |
| RAG with Gemini | Multi-turn red teaming | LLM-powered generation |
| LLM-as-a-judge (grounding) | LLM-as-a-judge (safety) + calibration | Second-LLM validation |
| Structured JSON output | CWE-aligned vulnerability reports | JSON mode |
| Retrieve → Generate → Judge → Retry | Screen → Generate → Judge → Retry + ablation | Multi-layer pipeline |
| — | Bootstrap CIs, ROC/AUC, Cohen's kappa | Statistical rigor |
