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

visual:
# Generate visual representation of database
	$(call ECHO_GREEN, Generating a pretty image...)
	(\
		$(COMPOSE) $(COMPOSE_CMD) graph_models --pygraphviz -a -g -o visualized.png; \
	)

dumpdata:
# Dump database to fixture file
	$(call ECHO_RED, Database dump...)
	(\
		$(COMPOSE) $(COMPOSE_CMD) dumpdata --exclude auth.permission --exclude contenttypes > ./initial_data.json; \
	)

shell:
# Run a local shell for debugging
	$(call ECHO_GREEN, Opening iPython shell...)
	( \
		$(COMPOSE) $(COMPOSE_CMD) shell; \
	)




######################
# OLD
######################

r_crawl:
# Run ALL scrapy spiders
	$(call ECHO_GREEN, Running Spiders Background Process... )
	 (\
		cd recognition; \
		nohup python crawl.py &  \
	)

crawl_spider:
# Run scrapy spider
	$(call ECHO_GREEN, Running $(spider) spider... )
	 (\
		scrapy crawl $(spider);  \
	)

r_crawl_spider:
# Run scrapy spider
	$(call ECHO_GREEN, Running $(spider) spider as background process... )
	 (\
		nohup scrapy crawl $(spider) &  \
	)

delete_sqlite:
# delete project db
	( \
		rm -rf db.sqlite3;\
	)

reset_migrations:
# delete all migrations furing initial development
	( \
		find . -path "*/migrations/*.py" -not -name "__init__.py" -delete; \
		find . -path "*/migrations/*.pyc"  -delete; \
	)

map_points:
	( \
		python manage.py plot_lng_lat;\
	)

r_map_points:
	( \=
		nohup python manage.py plot_lng_lat & \
	)

validate_urls:
	( \
		python manage.py valid_url;\
	)

r_validate_urls:
	( \
		nohup python manage.py valid_url & \
	)

find_contacts:
	( \
		nohup python manage.py find_contacts & \
	)

map_locations:
	( \
		nohup python manage.py plot_lng_lat & \
	)

rank:
	# Start ranking centers
	(\
		python manage.py rank; \
	)

r_rank:
	# Start ranking centers
	(\
		nohup python manage.py rank & \
	)

sql_dump:
	# dump to fixtures file
	(\
		rm -rf recognition/fixtures/dump.json; \
		./manage.py dumpdata --natural-primary --natural-foreign > fixtures/dump.json ; \
	)


initial_data:
# load initial db data
	( \
		pg_restore -p 5433 -d recognition --verbose initial_data.dump; \
	)

r_initial_data:
# load initial db data in vm
	( \
		sudo -u postgres pg_restore -p 5433 -d recognition --verbose initial_data.dump; \
	)


createuser:

	# docker exec -it seeker_app echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'pass')" | ./manage.py shell;
	( \
		docker exec -it seeker_app python manage.py createsuperuser
	)



# docker exec -it seeker_app python manage.py createsuperuser


# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'pass')" | ./manage.py shell;
