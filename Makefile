.PHONY: app

app:
	gunicorn app:app --bind 0.0.0.0:80\
         --access-logfile logs/gunicorn-access.log\
         --error-logfile logs/gunicorn-error.log

.PHONY: data
data:
	python generate_data.py

.PHONY: docker_generator_app
docker_generator_app:
	sh generator_loop.sh datageneratorapp/config.yaml
