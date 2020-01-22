PROJECT_NAME = seeker
SHELL := /bin/sh
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "migrate                   	Run database migrations"
	@echo "collectstatic				Collect static assets"


.PHONY: requirements


# Command variables
COMPOSE = docker-compose
COMPOSE_CMD = exec app python manage.py
MANAGE_CMD = python manage.py

# Helper functions to display messagse
ECHO_BLUE = @echo "\033[33;34m $1\033[0m"
ECHO_RED = @echo "\033[33;31m $1\033[0m"
ECHO_GREEN = @echo "\033[33;32m $1\033[0m"

# The default server host local development
HOST ?= localhost:8000

migrate:
# Run django migrations inside docker
	$(call ECHO_GREEN, Running migrations... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) migrate --no-input; \
	)

collectstatic:
# Run django migrations inside docker
	$(call ECHO_GREEN, Collect static assets... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) collectstatic --no-input; \
	)

migrations:
# Run django migrations inside docker
	$(call ECHO_GREEN, Create new database migrations... )
	( \
		$(COMPOSE) $(COMPOSE_CMD) makemigrations; \
	)

build:
# Run django migrations inside docker
	$(call ECHO_GREEN, Building new images... )
	( \
		$(COMPOSE) build; \
	)

down:
# Run django migrations inside docker
	$(call ECHO_GREEN, Tear down containers... )
	( \
		$(COMPOSE) down; \
	)

up:
# Run django migrations inside docker
	$(call ECHO_GREEN, Launching starship... )
	( \
		$(COMPOSE) up; \
	)
