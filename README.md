# Receipt Processor API

A web service for processing receipts and calculating reward points based on defined business rules.

Built with **Python 3.12**, **FastAPI**, and **Uvicorn**.

---

## Features

- Process receipt data and return a unique ID
- Retrieve reward points based on receipt ID
- Validates all input fields with Pydantic
- In-memory storage (no persistence)
- Follows spec from [`api.yml`](https://github.com/SabrinaKung/receipt-processor/blob/main/api.yaml)

---

## Run with Docker

### 1. Build the image

```bash
docker build -t receipt-processor .
```
### 2. Run the container

```bash
docker run -p 8000:8000 receipt-processor
```

---

## Run Locally (No Docker)

1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the API server

```bash
uvicorn app.main:app --reload
```
