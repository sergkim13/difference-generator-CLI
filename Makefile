install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

force-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml