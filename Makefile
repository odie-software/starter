all: env build restart
build: api web modules
start: restart

env:
	@echo "UID=$$(id -u)" > .env
	@echo "GID=$$(id -g)" >> .env

api:
	docker compose up api -d --build

web:
	docker compose up web -d --build

restart:
	docker compose up -d --force-recreate

migrate:
	docker compose exec api python manage.py makemigrations
	docker compose exec api python manage.py migrate

shell:
	docker compose exec api python manage.py shell -i ipython

test:
	docker compose exec api coverage run manage.py test ${APP}
	docker compose exec api coverage report -m

api_modules:
	cd ./api && python -m venv .venv
	./api/.venv/bin/pip install -r ./api/requirements.txt

web_modules:
	cd ./web && npx pnpm install

modules: api_modules web_modules

web_pkg:
	./bin/pkg_helper.py web

api_pkg:
	./bin/pkg_helper.py api
