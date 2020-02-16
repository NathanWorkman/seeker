.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<


# Defaults
PROJECT_NAME = seeker
SHELL := /bin/bash

# Command variables
COMPOSE = docker-compose
COMPOSE_CMD = exec app python manage.py
MANAGE_CMD = python manage.py

# Helper functions to display messagse
ECHO_GREEN = @echo "\033[33;32m $1\033[0m"
ECHO_BLUE = @echo "\033[33;34m $1\033[0m"
ECHO_RED = @echo "\033[33;31m $1\033[0m"

# The default server host local development
HOST ?= localhost:8000

## migrate 	Run migrations.
migrate:
	$(call ECHO_GREEN, Running migrations... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) migrate --no-input; \
	)

## collectstatic 	Collect static assets.
collectstatic:
	$(call ECHO_GREEN, Collect static assets... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) collectstatic --no-input; \
	)

## migrations 	Create new database migrations.
migrations:
	$(call ECHO_GREEN, Create new database migrations... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) makemigrations; \
	)

## build 		Build Docker images.
build:
	$(call ECHO_GREEN, Building new images... )
	( \
		$(COMPOSE) build; \
	)

## down 		Shutdown Docker containers.
down:
	$(call ECHO_GREEN, Tear down containers... )
	( \
		$(COMPOSE) down; \
	)

## up 		Run Docker containers.
up:
	$(call ECHO_GREEN, Launching starship... )
	( \
		$(COMPOSE) up; \
	)


## test_backend 	Run PyTest.
test:
	$(call ECHO_GREEN, Running pytest...)
	( \
		./utils/test.sh; \
	)

## setup 		Project initial setup.
setup:
	$(call ECHO_GREEN, Setting up project...)
	( \
		./utils/setup.sh; \
	)

