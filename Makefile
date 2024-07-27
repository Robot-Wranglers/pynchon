##
# Python project makefile.
##
.SHELL := bash
MAKEFLAGS += --warn-undefined-variables
# .SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := none

THIS_MAKEFILE := $(abspath $(firstword $(MAKEFILE_LIST)))
THIS_MAKEFILE := `python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' ${THIS_MAKEFILE}`
SRC_ROOT := $(shell dirname ${THIS_MAKEFILE})

NO_COLOR:=\033[0m
COLOR_GREEN=\033[92m

PYPI_PROJECT_NAME:=pynchon
DOCKER_IMAGE_NAME?=pynchon

.PHONY: build docs

init: py-init
build: py-build docker-build
clean: py-clean docker-clean

docker-clean:
	docker rmi $(DOCKER_IMAGE_NAME) >/dev/null || true

SHORT_SHA=$(shell git rev-parse --short HEAD)
docker-build docker.build build.docker:	
	docker build -t $(DOCKER_IMAGE_NAME) .
	docker tag $(DOCKER_IMAGE_NAME) robotwranglers/pynchon:latest
	docker tag $(DOCKER_IMAGE_NAME) robotwranglers/pynchon:${SHORT_SHA}

docker.push:
	docker push robotwranglers/pynchon:latest
	docker push robotwranglers/pynchon:${SHORT_SHA}

docker-shell:
	docker run -it --rm -v `pwd`:/workspace -w /workspace \
		--entrypoint bash $(DOCKER_IMAGE_NAME)

docker-test:
	docker run --rm -v `pwd`:/workspace -w /workspace --entrypoint sh $(DOCKER_IMAGE_NAME) -x -c "pynchon--help"

py-init:
	# $(call _announce_target, $@)
	set -x \
	; pip install build \
	; pip install --quiet -e .[dev] \
	; pip install --quiet -e .[testing] \
	; pip install --quiet -e .[publish]

py-build: py-clean
	export version=`python setup.py --version` \
	&& (git tag $$version \
	|| printf 'WARNING: Failed to git-tag with release-tag (this is normal if tag already exists).\n' > /dev/stderr) \
	&& printf "# WARNING: file is maintained by automation\n\n__version__ = \"$${version}\"\n\n" \
	| tee src/${PYPI_PROJECT_NAME}/_version.py \
	&& python -m build

py-clean:
	rm -rf tmp.pypi* dist/* build/* \
	&& rm -rf src/*.egg-info/
	find . -name '*.tmp.*' -delete
	find . -name '*.pyc' -delete
	find . -name  __pycache__ -delete
	find . -type d -name .tox | xargs -n1 -I% bash -x -c "rm -rf %"
	rmdir build || true

version:
	@python setup.py --version

pypi-release:
	PYPI_RELEASE=1 make build \
	&& twine upload \
	--user $${PYPI_USER} \
	--password $${PYPI_TOKEN} \
	dist/*

release: clean normalize static-analysis test pypi-release

tox-%:
	tox -e ${*}

normalize: tox-normalize
lint static-analysis: tox-static-analysis
smoke-test stest: tox-stest
test-integrations itest: tox-itest
utest test-units: tox-utest
dtest: tox-dtest
docs-test: dtest
test: test-units test-integrations smoke-test
iterate: clean normalize lint test

plan: docs-plan
plan-docs: docs-plan

docs-plan:
	@# Run from tox, not vice versa 
	pynchon src plan 
	pynchon docs plan
	pynchon python-api plan
	pynchon python-cli plan
docs: docs-apply
docs-apply apply:
	@# Run from tox, not vice versa 
	pynchon src apply
	pynchon docs apply
	pynchon python-api apply
	pynchon python-cli apply
