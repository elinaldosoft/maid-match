runserver:
	python manage.py runserver

dev_env_install:
	pip3 install -r requirements/dev.txt

test:
	pytest

check-code:
	pre-commit run --all-files