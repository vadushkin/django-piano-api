# Run Project

run:
	docker-compose up -d --build

stop:
	docker-compose stop

csu:
	docker exec -it backend poetry run python manage.py createsuperuser

migrate:
	docker exec -it backend poetry run python manage.py migrate
