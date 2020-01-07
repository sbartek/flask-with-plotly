.PHONY: app

flask_app:
	python app.py

app:
	sbin/run_app.sh

.PHONY: data
data:
	python generate_data.py

.PHONY: build_generator_docker
build_generator_docker:
	docker build --tag barteks/datageneratorapp -f datageneratorapp/Dockerfile .

.PHONY: run_generator_docker
run_generator_docker:
	docker run barteks/datageneratorapp

.PHONY: build_dashboard_docker
build_dashboard_docker:
	docker build --tag barteks/datagenerateddashboard -f datagenerateddashboard/Dockerfile .

