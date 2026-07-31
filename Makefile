.PHONY: setup run test test-backend test-frontend

setup:
	python -m pip install -e '.[dev]'
	npm install

run:
	cd src/backend && python main.py --port 8080 --reload

test: test-backend test-frontend

test-backend:
	python -m pytest

test-frontend:
	npm run test:frontend
