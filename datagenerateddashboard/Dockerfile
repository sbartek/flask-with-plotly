FROM python:3.6
WORKDIR /app
COPY . /app
COPY datagenerateddashboard/config.yaml /app/flask_app_config.yaml
RUN pip install -r datagenerateddashboard/requirements.txt
RUN mkdir /var/datasource
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
