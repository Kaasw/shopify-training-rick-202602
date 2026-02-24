# Shopify API Training Repository

This repository is a template for onboarding developers into:
- Shopify eCommerce concepts and core entities
- Python `requests` fundamentals
- Shopify Admin GraphQL API (queries and mutations)
- Storing created entity IDs into a local SQL database for safe cleanup

The repo contains **skeleton code only** (with TODOs). Do not hardcode secrets or store tokens in code.

---

## 1) Fork & naming convention

1. Fork this repository to your GitHub account.
2. Rename your fork using:

`shopify-training-<yourname>-<yyyymm>`

Example: `shopify-training-alex-202602`

---

## 2) Local setup

### Requirements
- Python 3.10+
- pip

### Create venv and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

---

## 3) Environment variables

1. Copy `.env.sample` to `.env`
2. Fill in:
    - `SHOPIFY_SHOP_DOMAIN`
    - `SHOPIFY_ADMIN_API_VERSION`
    - `SHOPIFY_ADMIN_ACCESS_TOKEN`

---

## 4) SQLite database (raw SQL training)

This training uses raw SQL (SQLite) to assess SQL skills.

The repository only provides:
- A DB connector
- execute/query helper methods

Trainees must implement:
- `CREATE TABLE` statements
- INSERT / UPDATE / DELETE
- SELECT queries (including joins if needed)
- DB file: SQLITE_PATH (default: ./training.db)

---

## 5) Exercises

Run Example:
```bash
python -m src.exercises.exercise_00_onboarding
```


