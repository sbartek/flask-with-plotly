FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install -r datageneratorapp/requirements.txt
RUN mkdir /var/dataSink
ENTRYPOINT ["generator_loop.sh", "--data_path=/var/dataSink/data.json"]

