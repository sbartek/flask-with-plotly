FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install -r datageneratorapp/requirements.txt
RUN mkdir /var/dataSink
ENTRYPOINT ["sbin/generator_loop.sh"]
CMD ["--data_path=/var/dataSink/data.json"]

