# Data-Engineering-Fork-of-AmFam-Workshop

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Personal%20Fork-orange.svg)]()
[![Fork](https://img.shields.io/badge/Fork-AmFam%20Data%20Engineering%20Workshop-lightgrey.svg)](https://github.com/AmFamGitHub)

> **Personal fork** of the American Family Insurance Data Engineering Workshop, extended with additional pipeline examples, personal annotations, and exploratory implementations beyond the original curriculum.

---

## About This Fork

This repository is a personal extension of the American Family Insurance (AmFam) Data Engineering Workshop. The original workshop provides a structured introduction to enterprise data engineering practices — pipeline design, data quality frameworks, and cloud-native ETL patterns as practiced in production insurance and financial services environments.

This fork extends the original material with:

- **Personal annotations** throughout the workshop notebooks explaining design decisions, tradeoffs, and observed failure modes
- **Additional pipeline examples** exploring patterns that the original workshop introduces but does not fully develop
- **Custom context implementations** applying the workshop's techniques to data engineering problems outside the insurance domain (financial time series, clinical data pipelines)
- **Exploratory experiments** testing edge cases and performance characteristics of the covered tools and frameworks

> **Honesty note:** This fork extends the original AmFam Data Engineering Workshop with personal annotations, additional pipeline examples, and exploration of the techniques in a custom context. The original workshop content and its intellectual structure belong to American Family Insurance; this fork documents what was learned and where those learnings were taken further.

---

## What the Original Workshop Covers

The AmFam Data Engineering Workshop is a professional-grade curriculum covering:

- **Data pipeline architecture** — ingestion, transformation, and serving layer design for enterprise-scale data
- **Data quality frameworks** — validation, schema enforcement, and anomaly detection in production pipelines
- **Cloud-native ETL** — patterns for AWS/GCP-based batch and streaming data workloads
- **Orchestration** — workflow scheduling, dependency management, and failure recovery
- **Data contracts** — schema versioning, producer/consumer agreements, and breaking-change governance

This content reflects real engineering practices used at a large P&C insurance company handling structured and semi-structured financial data at scale.

---

## What This Fork Adds

### Extended Pipeline Patterns

The original workshop demonstrates pipeline patterns at an introductory level. This fork contains additional implementations exploring:

- Multi-source ingestion with heterogeneous schemas (insurance claims + external market data)
- Incremental load patterns for large historical datasets
- Idempotency guarantees and exactly-once semantics in batch ETL

### Cross-Domain Application

The workshop's techniques were applied to problems in adjacent domains:

- **Financial data engineering** — applying insurance data quality patterns to SEC filing ingestion (see [Fine-Tuned-SEC-Filing-Extraction-Pipeline](https://github.com/A-Kuo/Fine-Tuned-SEC-Filing-Extraction-Pipeline))
- **Clinical data pipelines** — adapting enterprise ETL patterns for multi-source clinical data (see [Multi-Source-Clinical-Data-Engineering-Platform](https://github.com/A-Kuo/Multi-Source-Clinical-Data-Engineering-Platform))

### Personal Annotations

Workshop notebooks include inline commentary on:

- Where the demonstrated pattern breaks down at scale
- Alternative approaches considered and why the workshop's choice is defensible
- Connections to production systems observed in related internship and research work

---

## Repository Structure

```
Data-Engineering-Fork-of-AmFam-Workshop/
├── workshop/           # Original AmFam workshop content (upstream)
├── extensions/         # Additional pipeline examples (fork additions)
│   ├── multi_source/   # Heterogeneous ingestion patterns
│   ├── incremental/    # Incremental load implementations
│   └── cross_domain/   # Applications to finance and clinical domains
├── notebooks/          # Annotated workshop notebooks
└── docs/               # Additional documentation and notes
```

---

## Getting Started

```bash
# Clone this fork
git clone https://github.com/A-Kuo/Data-Engineering-Fork-of-AmFam-Workshop.git
cd Data-Engineering-Fork-of-AmFam-Workshop

# Install dependencies
pip install -r requirements.txt

# Start with the annotated workshop notebooks
jupyter notebook notebooks/
```

---

## Relationship to Original

| Aspect | Original Workshop | This Fork |
|--------|------------------|-----------|
| Audience | AmFam engineering curriculum | Personal learning and extension |
| Scope | Insurance/enterprise data patterns | Extended to finance and clinical domains |
| Depth | Introductory to intermediate | Deeper exploration in selected areas |
| Annotations | Clean instructional content | Heavy personal commentary and notes |

This fork is maintained for personal learning and portfolio demonstration. It is not a competing product or redistribution of proprietary content — the workshop curriculum and its core implementations belong to American Family Insurance.

---

## Related Work

This fork connects to a broader data engineering portfolio:

- **[Multi-Source-Clinical-Data-Engineering-Platform](https://github.com/A-Kuo/Multi-Source-Clinical-Data-Engineering-Platform)** — Enterprise data engineering patterns applied to clinical AI
- **[Fine-Tuned-SEC-Filing-Extraction-Pipeline](https://github.com/A-Kuo/Fine-Tuned-SEC-Filing-Extraction-Pipeline)** — Financial document ingestion using similar pipeline architecture
- **[crosscloud-ml-orchestration](https://github.com/A-Kuo/crosscloud-ml-orchestration)** — ML-specific orchestration building on enterprise data engineering foundations

---

## Attribution

Original workshop content: **American Family Insurance** Data Engineering team. This fork was created during and after a professional engagement with AmFam. Personal additions and annotations are authored by A-Kuo.

---

*Last updated: April 2026*
