# Data Layer Integrity Sentinel & E-Commerce Event QA CLI

> Stop deploying broken tracking tags. Automatically validate dataLayer e-commerce event payloads in your CI/CD pipeline before release.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a pure Python dataLayer integrity testing tool (`datalayer_sentinel.py`): 1) Validates JSON-LD and dataLayer payloads against GA4 standard schemas (`view_item`, `add_to_cart`, `begin_checkout`, `purchase`), 2) Checks for critical parameters (currency ISO code, value numeric type, item arrays, transaction_id uniqueness), 3) Emits clear pass/fail terminal reports and JSON summaries suitable for GitHub Actions CI/CD.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `ci/github-action-workflow.yml`
- `examples/sample_datalayer_dumps.json`
- `examples/sample_page_datalayer.json`
- `LICENSE`
- `README.md`
- `schema/ecommerce_datalayer_schema.json`
- `schemas/ga4_ecommerce_schemas.json`
- `src/datalayer_sentinel.py`
- `tests/test_sentinel.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/datalayer_sentinel.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "data-layer-integrity-sentinel",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **JSON Schema Validation:** Validates client-side dataLayer.push payloads against strict schema contracts for standard e-commerce events.
- **Asynchronous Event Race Conditions:** Detects when purchase or addToCart events push before user consent or container library initialization.
- **Automated CI/CD Quality Gate:** Runs headless assertion tests during automated staging builds to prevent regressions during store checkout updates.

---

## 📚 Primary Documentation & Verifiable References

- [W3C Customer Experience Digital Data Community Group (CEDDL)](https://www.w3.org/2013/12/ceddl-201312.pdf) - Standardized event schema and dataLayer object specifications.
- [Google Tag Manager Data Layer Guide](https://developers.google.com/tag-platform/tag-manager/datalayer) - Implementation guidelines for dataLayer architecture.
- [JSON Schema Draft-07 Specification](https://json-schema.org/draft-07/json-schema-release-notes) - Standard syntax for declaring structural validation rules on JSON objects.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
