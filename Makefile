.PHONY: app

app:
	gunicorn app:app --bind 0.0.0.0:80\
         --access-logfile logs/gunicorn-access.log\
         --error-logfile logs/gunicorn-error.log

.PHONY: data
data:
	python generate_data.py
