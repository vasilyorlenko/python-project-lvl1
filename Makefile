install:
	poetry install

brain-games:
	poetry run brain-games

build:
	rm -rf dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games