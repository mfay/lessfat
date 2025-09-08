VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
UVICORN=$(VENV)/bin/uvicorn

# Create virtual environment
create_venv:
	python3 -m venv $(VENV)

# Install dependencies
install: $(VENV)/bin/activate requirements.txt
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) app.main:app --reload

