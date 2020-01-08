FROM python:3.6
WORKDIR /app
COPY . /app
COPY datagenerateddashboard/config.yaml /app/flask_app_config.yaml
RUN pip install -r datagenerateddashboard/requirements.txt
RUN mkdir /var/datasource
ENTRYPOINT ["sbin/run_app.sh"]
CMD ["--data_path=data/test_data.json"]
