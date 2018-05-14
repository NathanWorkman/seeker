PROJECT_NAME = seeker
SHELL := /bin/sh
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "virtualenv                   Create virtual enviroment"
	@echo "requirements                 Install requirements.txt"
	@echo "migrate 						Run Django migrations"
	@echo "user  						Create user account"
	@echo "test  						Run tests"
	@echo "clean 						Remove all *.pyc, .DS_Store and temp files from the project"
	@echo "shell 						Open Django shell"
	@echo "migrations 					Create database migrations"
	@echo "collectstatic 				Collect static assets"
	@echo "run 							Run Django Server"
	@echo "crawl <spidername>           Run Scrapy Spider"

.PHONY: requirements


# Command variables
MANAGE_CMD = python manage.py
PIP_INSTALL_CMD = pip install
PLAYBOOK = ansible-playbook
VIRTUALENV_NAME = venv

# Helper functions to display messagse
ECHO_BLUE = @echo "\033[33;34m $1\033[0m"
ECHO_RED = @echo "\033[33;31m $1\033[0m"
ECHO_GREEN = @echo "\033[33;32m $1\033[0m"

# The default server host local development
HOST ?= localhost:8000

reset: delete_sqlite migrate user run
setup: virtualenv requirements migrate user yarn build collectstatic 

virtualenv:
# Create virtualenv
	$(call ECHO_GREEN, Creating virtualenv... )
	virtualenv -p python3 $(VIRTUALENV_NAME)

requirements:
# Install project requirements
	$(call ECHO_GREEN, Installing requirements... )
	( \
		source venv/bin/activate;\
		$(PIP_INSTALL_CMD) -r requirements.txt; \
	)

migrate:
# Run django migrations
	$(call ECHO_GREEN, Running migrations... )
	( \
		cd seeker; \
		$(MANAGE_CMD) migrate; \
	)

user:
# Create user account
	$(call ECHO_GREEN, Creating super user... )
	( \
		cd seeker; \
		echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'pass')" | ./manage.py shell; \
	)

test:
# Run the test cases
	( \
		cd seeker; \
		$(MANAGE_CMD) test; \
	)

clean:
# Remove all *.pyc, .DS_Store and temp files from the project
	$(call ECHO_BLUE,removing .pyc files...)
	@find . -name '*.pyc' -exec rm -f {} \;
	$(call ECHO_BLUE,removing static files...)
	@rm -rf $(PROJECT_NAME)/_static/
	$(call ECHO_BLUE,removing temp files...)
	@rm -rf $(PROJECT_NAME)/_tmp/
	$(call ECHO_BLUE,removing .DS_Store files...)
	@find . -name '.DS_Store' -exec rm {} \;

shell:
# Run a local shell for debugging
	( \
		cd seeker; \
		$(MANAGE_CMD) shell; \
	)

migrations:
# Create database migrations
	( \
		cd seeker; \
		$(MANAGE_CMD) makemigrations; \
	)

collectstatic:
# Collect static assets
	$(call ECHO_GREEN, Collecting static assets...)
	( \
		cd seeker; \
		$(MANAGE_CMD) collectstatic; \
	)

run:
# run django server
	$(call ECHO_GREEN, Starting Django Server...)
	( \
		cd seeker; \
		gulp; \
	)


crawl:
# Run ALL scrapy spiders
	$(call ECHO_GREEN, Running spiders... )
	 (\
		cd seeker; \
		python crawl.py;  \
	)

crawl_spider:
# Run scrapy spider
	$(call ECHO_GREEN, Running $(spider) spider... )
	 (\
		cd seeker; \
		scrapy crawl $(spider);  \
	)

delete_sqlite: 
# delete project db
	( \
		cd seeker; \
		rm -rf db.sqlite3;\
	)

yarn: 
# install npm modules
	$(call ECHO_GREEN, Installing npm modules... )
	( \
		yarn; \
	)

build: 
# build static assets
	$(call ECHO_GREEN, Compiling static assets... )
	( \
		cd seeker; \
		gulp build; \
	)


deploy_staging:
# deploy to staging server
	$(call ECHO_BLUE, deploy changes to the STAGING server... )
	(\
		ssh-add -K; \
		cd ansible; \
		$(PLAYBOOK) -i hosts deploy_staging.yml --verbose --extra-vars branch=$(branch);  \
	)

deploy_production:
# deploy to production server
	$(call ECHO_RED, deploy changes to the PRODUCTION server... )
	(\
		ssh-add -K; \
		cd ansible; \
		$(PLAYBOOK) -i hosts deploy_production.yml --verbose --extra-vars branch=$(branch);  \
	)
