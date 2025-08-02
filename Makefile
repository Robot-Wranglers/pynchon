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
SHORT_SHA=$(shell git rev-parse --short HEAD)

# DOCKER_IMAGE_NAME?=${py.pkg_name}
pynchon.tag=robotwranglers/${pynchon.img}
pynchon.img=pynchon
py.pkg_name=pynchon

include .cmk/compose.mk 
$(call mk.import.plugins, py.mk actions.mk)

$(call docker.import, \
        namespace=docker.pynchon \
        file=Dockerfile img=${pynchon.img})

.PHONY: build docs

init: flux.stage/initializing py.init
build: flux.stage/building py.pkg.build docker.pynchon.build
	docker tag ${pynchon.img} ${pynchon.tag}:latest
	docker tag ${pynchon.img} ${pynchon.tag}:${SHORT_SHA}

clean: flux.stage/cleaning \
	py.clean docker.rmi/$(pynchon.img)

docker-shell: docker.pynchon.shell

# docker.push:
# 	docker push ${pynchon.tag}:latest
# 	docker push ${pynchon.tag}:${SHORT_SHA}

docker.pynchon.test: docker.pynchon.dispatch/self.test.docker
self.test.docker:; set -x && pynchon plugins list && bash tests/smoke/test.sh

version: py.pkg.version

release: clean normalize static-analysis test pypi.release

$(call tox.import, \
        normalize static-analysis itest stest utest dtest )

# normalize: tox/normalize
lint: tox/static-analysis
smoke-test: stest
test-integrations: itest
test-units: utest
docs-test: dtest
test: flux.stage/testing \
	py.test docker.pynchon.test
py.test: test-units test-integrations smoke-test

iterate: clean normalize lint test

# plan: docs-plan
# plan-docs: docs-plan
# docs-plan:
# 	@# Run from tox, not vice versa 
# 	pynchon src plan 
# 	pynchon docs plan
# 	pynchon python-api plan
# 	pynchon python-cli plan

docs: docs-apply
docs-apply apply:
	@# Run from tox, not vice versa 
	pynchon src apply
	pynchon docs apply
	pynchon python-api apply
	pynchon python-cli apply
