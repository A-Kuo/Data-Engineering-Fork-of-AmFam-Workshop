# AmFam AI & Data Engineering Modification

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-astral-purple.svg)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Modification of AmFam AI Workshop repository, a production-oriented exploration of **retrieval-augmented generation (RAG)**, **vector databases**, **LLM evaluation**, **AI safety**, and **adversarial robustness**—applied to the data engineering and AI challenges relevant to the insurance industry.

> **Purpose:** This portfolio demonstrates end-to-end AI engineering capabilities for building trustworthy, auditable, and secure AI systems—directly aligned with the challenges faced by American Family Insurance and the broader P&C insurance sector.

---

## Abstract

Currently, insurance companies deploying AI face unique challenges that general-purpose ML tutorials rarely address:

| Challenge | Industry Impact | This Portfolio |
|-----------|-----------------|----------------|
| **Hallucinated coverage answers** | Wrong information on policy exclusions, limits, or regulations creates regulatory and legal exposure | RAG with citations + LLM-as-judge validation, 3-tier grounding scores, attention-based hallucination detection |
| **Prompt injection & data exfiltration** | Customer-facing bots and internal copilots are attack surfaces | Defense-in-depth security benchmarking with automated red teaming, threat models, CWE-aligned reporting |
| **Governance & auditability** | [NAIC Model Bulletin](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers) requires written AI programs, validation, testing, bias analysis | Formal evaluation frameworks with ROC/AUC, bootstrap confidence intervals, ablation studies, JSONL logging |
| **Fraud/anomaly detection** | Class imbalance and limited public labeled data make fraud detection challenging | Imbalanced classification with PR-AUC, outlier detection with Mahalanobis and Isolation Forest |
| **Fairness & bias** | Regulatory expectations for equitable AI decision-making | Demographic parity measurement on synthetic groups |

---

## Repository Worktree

```
.
├── foundations/              # Core RAG pipeline (start here)
│   ├── hugging_face_chromadb_demo.ipynb    # PDF → text → embeddings → ChromaDB
│   └── gemini_rag_pipeline_demo.ipynb      # RAG with Gemini + LLM-as-judge grounding check
│
├── explorations/             # AI security, safety, hallucination research
│   ├── ai_safety_evals_demo.ipynb          # Embedding-based anomaly detection, threat models
│   ├── ai_security_benchmarking_demo.ipynb # Calibrated safety judge, red teaming, defense-in-depth
│   ├── rag_hallucination_scoring.ipynb       # Multi-signal grounding score with 3-tier routing
│   ├── attention_hallucination_demo.ipynb    # Attention entropy + KL divergence detection
│   ├── self_data_hallucination_classifier.ipynb  # Self-data pipeline for lightweight detectors
│   ├── tabular_claims_fraud_ml.ipynb         # Imbalanced fraud detection with PR-AUC
│   ├── synthetic_policy_rag_walkthrough.ipynb  # Fictional policy → Chroma → Q&A retrieval
│   ├── rag_eval_logging.ipynb                  # JSONL observability for governance
│   └── fairness_basics_demo.ipynb            # Demographic parity on synthetic groups
│
├── playground/               # Interactive red/blue/purple team labs
│   └── adversarial_prompt_crafting_lab.ipynb  # CTF-style security exercises
│
├── walkthrough/              # Portfolio narrative and interview prep
│   └── what_we_learn_from_this_repo.ipynb    # Master map: what each notebook demonstrates
│
├── docs/
│   └── insurance_alignment_and_extensions.md   # Insurer problems, papers, mappings
│
├── synthetic_data/           # Fictional policy + synthetic claims (safe, non-proprietary)
├── data/                     # OSTEP textbook (gitignored, auto-downloaded)
├── chroma/                   # ChromaDB stores (gitignored)
└── outputs/                  # Eval logs, synthetic policy vector stores (gitignored)
```

---

## Technical Highlights

### RAG Pipeline with Grounding Validation
- **Ingestion:** PDF → per-page text extraction with PyMuPDF
- **Embeddings:** Hugging Face `sentence-transformers/all-MiniLM-L6-v2` with mean pooling, L2 normalization
- **Vector Store:** ChromaDB persistent collections (`ostep`, `attack_patterns`)
- **Retrieval:** Top-k document search with source attribution (`<SOURCE chapter_id="..." page_number="...">`)
- **Generation:** Gemini with structured JSON output (answer + citations + key concepts)
- **Validation:** LLM-as-judge checks grounding; retry loop for ungrounded claims

### Hallucination Detection (Three Approaches)
1. **RAG-based:** Composite score from retrieval relevance + citation coverage + judge groundedness → RELIABLE/UNCERTAIN/UNRELIABLE routing
2. **Attention-based:** Shannon entropy (per-head diffuseness) + cross-layer KL divergence → Z-test classification (no training data required)
3. **Self-data classifier:** Seed QA → Gemini answers → judge labels → feature extraction → Logistic Regression (scales with API budget, no hand labels)

### AI Security & Safety
- **Threat Model:** L0–L3 severity levels for prompt attacks (system prompt extraction, jailbreak, indirect injection, privacy extraction)
- **Anomaly Detection:** Centroid cosine, Mahalanobis distance, Isolation Forest for adversarial prompt screening
- **Red Teaming:** Automated single-turn and multi-turn attacks with calibrated LLM-as-safety-judge
- **Defense-in-Depth:** ChromaDB screen → safety prompt → judge → retry layers with ablation studies
- **Statistical Rigor:** ROC/AUC, bootstrap confidence intervals, Wilson score intervals for safety rates

### Insurance-Specific ML
- **Fraud Detection:** Synthetic claims dataset with class imbalance handling, PR-AUC evaluation, stratified validation
- **Policy RAG:** Fictional auto policy chunked and indexed for coverage-style Q&A
- **Fairness:** Demographic parity difference measurement on synthetic groups (NAIC awareness)
- **Observability:** JSONL logging per query (timestamps, retrieval tier, distances) for governance

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| **Language** | Python 3.12 |
| **ML & Embeddings** | PyTorch, Transformers, scikit-learn |
| **LLM** | Google Gemini 2.5 Flash via Vertex AI |
| **Vector DB** | ChromaDB |
| **Data Processing** | PyMuPDF, pandas |
| **Visualization** | matplotlib |
| **Validation** | pydantic |
| **Environment** | uv (dependency management) |

---

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/A-Kuo/MadData-2026-AmFam-Workshop.git
cd MadData-2026-AmFam-Workshop
uv sync
```

### 2. Configure Environment

Create `.env` in the repo root:

```bash
GCP_PROJECT=your-gcp-project-id
GCP_LOCATION=us-central1
# Add API key if not using Vertex AI
```

### 3. Run Order

**Path A: Insurance-Style Stack (No External Downloads Required)**
1. `explorations/tabular_claims_fraud_ml.ipynb` — Imbalanced fraud ML
2. `explorations/synthetic_policy_rag_walkthrough.ipynb` — Policy RAG with synthetic data
3. `explorations/rag_eval_logging.ipynb` — Observability patterns
4. `explorations/fairness_basics_demo.ipynb` — Fairness measurement
5. `explorations/attention_hallucination_demo.ipynb` — Standalone hallucination detection (GPT-2)

**Path B: Full RAG Pipeline (Requires OSTEP Textbook Download)**
1. `foundations/hugging_face_chromadb_demo.ipynb` — Build vector store from OSTEP PDFs
2. `foundations/gemini_rag_pipeline_demo.ipynb` — RAG with grounding validation

**Path C: Security & Advanced Hallucination Research**
1. `explorations/ai_safety_evals_demo.ipynb` — Build `chroma_security/` anomaly detector
2. `explorations/ai_security_benchmarking_demo.ipynb` — Red team benchmarking
3. `explorations/rag_hallucination_scoring.ipynb` — RAG grounding scores
4. `explorations/self_data_hallucination_classifier.ipynb` — Train lightweight detector
5. `playground/adversarial_prompt_crafting_lab.ipynb` — Interactive security lab

**Portfolio Overview:** Start with `walkthrough/what_we_learn_from_this_repo.ipynb` for the full narrative.

---

## Attribution & Lineage

This portfolio extends the **MadData 2026 AmFam Workshop** ([original repository](https://github.com/zachzhou777/MadData-2026-AmFam-Workshop)) conducted at the University of Wisconsin–Madison.

**Original workshop:** 2 notebooks introducing RAG fundamentals with Hugging Face and ChromaDB.

**This portfolio:** 13 notebooks with original extensions in:
- AI safety & security evaluation frameworks
- Hallucination detection (RAG-based, attention-based, self-data classifiers)
- Insurance-aligned ML (fraud detection, policy RAG, fairness)
- Red-team security labs
- Statistical evaluation rigor

All synthetic data and fictional policies were created specifically for this portfolio. No proprietary insurance data is used.

---

## Related Work & Research

### Complementary Repositories

- **[Hallucinations](https://github.com/A-Kuo/Hallucinations)** — Information-theoretic hallucination detection using attention pattern analysis. Features two implementations: (v1) statistical Z-test on entropy + KL divergence; (v2) trained 18D-feature classifier with lookback ratio, frequency domain, and spectral features. Uses open-source models (Pythia, Llama, Mistral) and Claude for labeling.

### Hallucination Detection Research

This portfolio's attention-based hallucination detection aligns with recent advances in using transformer attention patterns for hallucination identification:

- **Chuang et al. (EMNLP 2024)** — "Lookback» attention ratio analysis for detecting factual inconsistencies in LLM outputs. [Implementation in Hallucinations v2]
- **Qi et al. (2026)** — Frequency-domain attention analysis for hallucination detection. [Implementation in Hallucinations v2]
- **Barbero et al. (2025)** — Spectral and Laplacian features for attention-based hallucination detection. [Implementation in Hallucinations v2]

### AI Safety & RAG Systems

- **MDPI 2025 Tutorial** — Multi-layer hallucination mitigation (prompt engineering, RAG, fine-tuning). Aligns with the defense-in-depth security approach and RAG + judge validation stack in this portfolio.
- **ACL 2025 GenAI-K Workshop** — GraphRAG for financial/regulatory text. Graph-based retrieval methods showing gains over vanilla RAG for structured domain documents.

### Insurance AI & Fraud Detection

- **arXiv:2308.11659** — "Synthetic Fraud Network Simulation Engine" for insurance fraud data generation. Addresses the scarcity of public labeled fraud datasets and motivates the synthetic data approach used in `tabular_claims_fraud_ml.ipynb`.
- **NAIC Model Bulletin on AI by Insurers** — [NAIC guidance](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers) on written AI programs, validation, testing, bias analysis, and accountability. The evaluation frameworks in this portfolio (ROC/AUC, bootstrap CIs, Wilson intervals, ablation studies) directly address these governance requirements.

### Industry RAG Implementations

- **GEICO RagRails / ZenML LLMOps Database** — [Implementation guide](https://www.zenml.io/llmops-database/implementing-rag-and-ragrails-for-reliable-conversational-ai-in-insurance) for reliable conversational AI in insurance, covering RAG guardrails, grounding validation, and safety layers. Mirrors the defense-in-depth and judge-validation patterns in this portfolio.
- **AmFam ML Research** — [ai-ml-amfam.com](https://www.ai-ml-amfam.com/) — American Family Insurance's ML research group, demonstrating industry investment in AI/ML capabilities aligned with this portfolio's focus areas.

---

## Interview Quick Reference

> *"This portfolio shows end-to-end AI engineering for trustworthy assistants: retrieval-grounded answers with citation and judge validation, hallucination signals from multiple detection methods, adversarial robustness with defense-in-depth, and statistical evaluation frameworks—the same problem classes prioritized in industry RAG deployments and NAIC-style AI governance."*

**See `walkthrough/what_we_learn_from_this_repo.ipynb` for:**
- One-paragraph summaries for each notebook
- Honest gap acknowledgment (synthetic data, minimal production logging)
- Suggested talking points for technical interviews

---

## License

MIT License — See [LICENSE](LICENSE) for details.

---

## Contact

Built as a portfolio piece demonstrating alignment with American Family Insurance's AI/ML engineering challenges. For questions or discussions about the technical approach, please open an issue or reach out via GitHub.
