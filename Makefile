lint:
	@flake8
	@isort --check

test:
	flake8
	isort
	py.test -v

detect-migrations:
	@python manage.py makemigrations --dry-run --no-input | grep 'No changes detected' -q || (echo 'Missing migration detected!' && exit 1)
