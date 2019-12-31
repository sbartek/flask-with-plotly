FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install -r datageneratorapp/requirements.txt
RUN mkdir /var/datasink
ENTRYPOINT ["sh", "generator_loop.sh", "datageneratorapp/config.yaml"]

