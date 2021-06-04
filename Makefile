clear-reports:
	rm -rdf reports/*

deploy-localy:
	pip3 install -r dependencies.list
	
run-locally: clear-reports
	pytest --junitxml=reports/junit_report.xml --html=reports/testing_report.html $(ARGS)

run-locally-implementing: clear-reports
	pytest -k Implementing --junitxml=reports/junit_report.xml --html=reports/testing_report.html $(ARGS)

run-locally-stable: clear-reports
	pytest -k Stable --junitxml=reports/junit_report.xml --html=reports/testing_report.html $(ARGS)

image:
	docker build . -t my-tests:latest

run-container:
	mkdir -p container-reports
	docker run --mount type=bind,source=`pwd`/container-reports,target=/tests/reports -e TEST_ARGS="-k Stable --containerized"  my-tests:latest

build-and-run: image run-container

# just to simplify features formatting, you shoud execute "pip3 install reformat-gherkin" before using this command
format:
	reformat-gherkin .
