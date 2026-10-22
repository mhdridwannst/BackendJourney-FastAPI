# BackendJourney-FastAPI

My learning log for becoming a backend developer. I'm building small APIs with FastAPI,
one topic at a time, and keeping the code here as I go.

## Stack

- Python
- FastAPI
- Uvicorn

## Running it locally

```bash
git clone https://github.com/mhdridwannst/BackendJourney-FastAPI.git
cd BackendJourney-FastAPI

python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs on http://127.0.0.1:8000. Interactive docs are at `/docs`.

## Project layout

```
main.py          app entry point
routers/         route modules
requirements.txt dependencies
```

## What I've covered so far

- [x] Basic routing
- [ ] Pydantic models and validation
- [ ] Database (SQLAlchemy + PostgreSQL)
- [ ] Authentication (JWT)
- [ ] Tests with pytest
- [ ] Docker
- [ ] Deployment

I'll update this list as I finish each one.
