# Development Tools

format:
	@autoflake --in-place --remove-all-unused-imports  --ignore-init-module-imports -r .
	@flake8 .
	@mypy .
	@isort .
	@black .

push:
	@git status
	@echo "All files listed above will be added to commit. Enter commit message to proceed. Ctr-C to abort."
	@read -p "Commit message: " COMMIT_MESSAGE; git add . ; git commit -m "$$COMMIT_MESSAGE"
	@git push

migrations:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test
