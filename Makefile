.PHONY: install lint format test security build check clean
install:
	python -m pip install -e '.[dev]'
lint:
	ruff check .
	ruff format --check .
format:
	ruff check --fix .
	ruff format .
test:
	pytest --cov=capital_growth --cov-report=term-missing --cov-fail-under=90
security:
	bandit -r src/
	pip-audit .
build:
	python -m build
check:
	twine check dist/*
clean:
	rm -rf dist build .pytest_cache .coverage coverage.xml
