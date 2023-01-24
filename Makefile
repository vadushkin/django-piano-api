# Run Project

run:
	docker-compose up -d --build
	docker exec -it backend_piano poetry run python manage.py migrate
	docker exec -it backend_piano poetry run python manage.py createsuperuser

stop:
	docker-compose stop
