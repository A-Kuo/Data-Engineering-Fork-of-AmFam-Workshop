# Insurance AI: Problems, Papers, and How This Repo Maps

Use this doc for interviews and portfolio narrative: **what insurers actually worry about** and **how your explorations are plausible solutions**.

---

## Problems insurers face (with LLMs and AI)

| Problem | Why it matters | Tie to this repo |
|--------|----------------|------------------|
| **Hallucinated coverage / policy answers** | Wrong answers on exclusions, limits, or regulations can mislead customers and create regulatory/legal exposure. Industry write-ups emphasize fabricated coverage, invented limits, and outdated regs. | `rag_hallucination_scoring`, `gemini_rag_pipeline_demo` (judge + citations), `attention_hallucination_demo` |
| **Overpromising** | GEICO-style testing found models implying they could take actions they cannot (e.g. processing payments). | `ai_security_benchmarking_demo`, defense-in-depth + policy-style system prompts |
| **Ambiguous / unstructured policy data** | Endorsements, scans, notes → RAG must retrieve the *right* chunk and stay grounded. | `hugging_face_chromadb_demo` (chunking, vector store), RAG + judge loop |
| **Prompt injection / data exfiltration** | Customer-facing bots and internal copilots are attack surfaces. | `ai_safety_evals_demo`, `adversarial_prompt_crafting_lab` |
| **Governance & auditability** | [NAIC Model Bulletin on Use of AI by Insurers](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers) pushes written AI programs, validation, testing, bias analysis, and accountability. | Your eval notebooks (ROC/AUC, Wilson CIs, ablations) = **documented testing** narrative |
| **Fraud / anomaly detection** | Classic P&C ML; class imbalance and limited public real data. | `ai_safety_evals_demo` (outlier detection, Mahalanobis, IF) as **analogous skill** |

---

## Relevant research (arxiv & adjacent)

- **Synthetic fraud networks / simulation** — [arXiv:2308.11659](https://arxiv.org/abs/2308.11659) (simulation engine for insurance fraud network data; addresses scarcity of public labeled data). *Extension idea:* small fraud-style tabular + graph notebook using public Kaggle/Mendeley-style data.
- **GraphRAG for finance** — ACL 2025 GenAI-K workshop: graph-based RAG for financial/regulatory text (reported gains vs vanilla RAG). *Extension idea:* optional `explorations/policy_graph_rag_sketch.ipynb` (entity extraction → simple graph + retrieval).
- **Multi-layer hallucination mitigation (tutorial)** — MDPI 2025 tutorial on layered mitigation (prompt, RAG, fine-tuning). Aligns narratively with your **defense-in-depth** security notebook + RAG + judge stack.
- **Lookback / frequency / spectral attention (your Hallucinations v2)** — Chuang et al. EMNLP 2024 (lookback); Qi et al. frequency-aware attention; Barbero et al. spectral features. *Extension:* port v2’s 18D features into `self_data_hallucination_classifier` for a stronger detector story.

---

## Public / synthetic datasets (practice, not proprietary AmFam data)

- **Kaggle** — e.g. “Insurance Claims Fraud” style datasets (tabular, fraud label).
- **Mendeley** — anonymized `insurance_claims` style CSVs.
- **Synthetic marketplaces** — e.g. GoMask-style small fraud scenario sets (good for demos only).

*Positioning:* “I didn’t use AmFam customer data; I used public/synthetic data to practice the **same ML patterns** (imbalance, scoring, evaluation) that apply to claims.”

---

## Implemented in-repo (personal use)

1. **`explorations/tabular_claims_fraud_ml.ipynb`** + `synthetic_data/claims_fraud_sample.csv` — tabular fraud, PR-AUC, imbalance.
2. **`explorations/rag_eval_logging.ipynb`** — JSONL observability stub.
3. **`synthetic_data/mini_auto_policy.md`** + **`explorations/synthetic_policy_rag_walkthrough.ipynb`** — fictional policy RAG.
4. **`explorations/fairness_basics_demo.ipynb`** — demographic parity on synthetic groups.
5. **`walkthrough/what_we_learn_from_this_repo.ipynb`** — full narrative walkthrough.

---

## One-sentence pitch for AmFam-style interviews

> “This repo shows end-to-end AI engineering for **trustworthy** assistants: retrieval-grounded answers with **citation and judge validation**, **hallucination signals** (attention + RAG scores), **adversarial robustness**, and **statistical evaluation**—the same problem classes called out in industry RAG deployments and NAIC-style AI governance.”

---

## References (open web)

- NAIC Model Bulletin on AI by insurers: [naic.org article](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers)
- Industry RAG + guardrails narrative (e.g. GEICO RagRails): [ZenML LLMOps DB / GEICO RAG](https://www.zenml.io/llmops-database/implementing-rag-and-ragrails-for-reliable-conversational-ai-in-insurance)
- AmFam ML research group (culture signal): [ai-ml-amfam.com](https://www.ai-ml-amfam.com/)
