NAME := markdown_to_html_converter
GRAMMAR_FILE := Markdown
TAG := $(shell git log -1 --pretty=%h)
IMG := ${NAME}:${TAG}
LATEST := ${NAME}:latest
antlr4 := java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:${CLASSPATH}" org.antlr.v4.Tool

antlr_build:
	$(antlr4) -Dlanguage=Python3 -visitor ./grammar/$(GRAMMAR_FILE).g4 -Werror -no-listener

docker_build:
	docker build -t ${IMG} .
	docker tag ${IMG} ${LATEST}

run:
	PYTHONPATH=.. python lang_bin.py

test:
	PYTHONPATH=.. python -m pytest --cov=./semantics

clean_pyc:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "*.pytest_cache" -exec rm -rf {} \;

install_dev:
	PYTHONPATH=.. python -m pip install -r requirements.txt -r test_requirements.txt

docker_run: docker_build
	docker container run ${IMG}
