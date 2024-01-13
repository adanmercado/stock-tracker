# Stock tracker API
API dedicated to product registration and stock control, written with FAST API and Python3.

# Dependencies
- Python3
- Fast API
- SqlAlchemy
- Uvicorn

To install the dependencies run the following command on you virtual environment.
```
pip install -r requirements.txt
```

# Run server
To run the server run the following command.
```
# Minimal
uvicorn api.main:app

# Autoreload
uvicorn api.main:app --reload
```