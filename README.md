# SAS.NerService

**SAS.NerService** is a microservice built to perform **Named Entity Recognition (NER)** for Arabic text. It extracts named entities such as persons, organizations, and locations using the Stanza NLP library.

This service is part of the larger **SAS (Situational Awareness System)** platform, which detects, classifies, and visualizes events from social media.

---

## 📦 Folder Structure

```bash
src/
│
├── app/
│   ├── core/
│   │   ├── configs/            # Environment and base configuration classes
│   │   │   ├── base_config.py
│   │   │   └── env_config.py
│   │   ├── factory/            # Service factory for dependency injection
│   │   │   ├── services_factory.py
│   │   │   └── services_registry.py
│   │   ├── models/             # Domain model for NamedEntity
│   │   │   └── named_entity.py
│   │   ├── services/
│   │   │   └── NER/            # NER interface and Stanza implementation
│   │   │       ├── ner_service_base.py
│   │   │       └── stanza_ner_service.py
│   ├── routes/                 # Flask route definitions for NER API
│   │   └── ner_routes.py
│   └── main.py                 # Entry point for running the service
│
├── tests/
│   ├── NerTests/               # Unit tests for the NER service
│   │   └── test_ner.py
│   └── conftest.py             # Pytest configuration
````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hasankhadd0ur/SAS.NerService.git
cd SAS.NerService
```

### 2. Setup a Python environment

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m stanza.download('ar')  # Arabic NER model
```

### 4. Run the service

```bash
cd src
uvicorn app.main:app --reload
```

The service will start on `http://localhost:8000`.

---

## 🧠 Features

* 📎 Arabic Named Entity Recognition using Stanza
* 🧩 Modular service design
* 🧪 Unit test coverage
* 📤 REST API for real-time inference

---

## 🛠️ API Usage

### Endpoint: `POST /ner/extract`

#### Request:

```json
{
  "text": "وقع انفجار في مدينة جبلة بمحافظة اللاذقية"
}
```

#### Response:

```json
[
  {
    "text": "جبلة",
    "type": "LOC"
  },
  {
    "text": "اللاذقية",
    "type": "LOC"
  }
]
```

---

## 🧪 Run Tests

```bash
pytest src/tests
```

---

## ⚙️ Configuration

Set environment variables via `.env` or your deployment method.

| Variable    | Description                |
| ----------- | -------------------------- |
| `ENV`       | Environment mode           |
| `LOG_LEVEL` | Logging level (INFO/DEBUG) |

---

## 📚 Technologies

* Python 3.10+
* Flask
* Stanza (for Arabic NLP)
* Pytest

---

## 👤 Author

Hasan Khaddour
Higher Institute for Applied Sciences and Technology (HIAST)

---

## 🏁 License

MIT License – see the [LICENSE](LICENSE) file for details.

