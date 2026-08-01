.PHONY: setup run test test-smoke test-backend test-backend-smoke test-frontend test-frontend-smoke test-accept-p15

setup:
	python -m pip install -e '.[dev]'
	npm install

run:
	cd src/backend && python main.py --port 8080 --reload

test: test-backend test-frontend

test-smoke: test-backend-smoke test-frontend-smoke

# P15 acceptance gate (P9–P14 regression). Live probes: ACCEPT_LIVE=1 make test-accept-p15
test-accept-p15:
	bash ./scripts/accept_p15.sh

test-backend:
	python -m pytest

test-backend-smoke:
	python -m pytest -q \
		src/backend/tests/test_main_health.py \
		src/backend/tests/test_startup_validator.py \
		src/backend/tests/test_team_manager.py \
		src/backend/tests/test_plaza_dispatch.py \
		src/backend/tests/test_legacy_surfaces.py \
		src/backend/tests/test_information_teams.py \
		src/backend/tests/test_startup_health_layers.py \
		src/backend/tests/test_tradingagents_runtime.py \
		src/backend/tests/test_information_sources.py \
		src/backend/tests/test_information_pipelines.py \
		src/backend/tests/test_investment_engine.py \
		src/backend/tests/test_domain_api_and_security.py \
		src/backend/tests/test_engine_live_cockpit.py

test-frontend:
	npm run test:frontend

test-frontend-smoke:
	npm run test:frontend:smoke
