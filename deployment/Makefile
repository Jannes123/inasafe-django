SHELL := /bin/bash
PROJECT_ID := inasafe

# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------

default: web

run: build web

deploy: run migrate collectstatic
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh instance "
	@echo "You can access it on http://localhost:61100"
	@echo "------------------------------------------------------------------"

build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) build

web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d web
	#@dipall

migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py migrate

collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in production mode"
	@echo "------------------------------------------------------------------"
	#@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py collectstatic --noinput
	#We need to run collect static in the same context as the running
	# uwsgi container it seems so I use docker exec here
	@docker exec -t -i $(PROJECT_ID)_uwsgi_1 python manage.py collectstatic --noinput

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in production mode"
	@echo "------------------------------------------------------------------"

	@docker-compose -p $(PROJECT_ID) kill

rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing production instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) rm

logs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing uwsgi logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) logs uwsgi

nginxlogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing nginx logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) logs web

shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi /bin/bash

dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production database"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)_db_1 psql -U docker -h localhost gis

qgis:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running QGIS desktop in production mode"
	@echo "Make sure you have started the services with make run first"
	@echo "------------------------------------------------------------------"
	@xhost +; docker run --rm --name="qgis-desktop-2-4" \
	-i -t \
	--link $(PROJECT_ID)_db_1:db \
	--link $(PROJECT_ID)_qgisserver_1:qgisserver \
	--link $(PROJECT_ID)_mapproxy_1:mapproxy \
	--volumes-from $(PROJECT_ID)_qgisserver_1 \
	-v ${HOME}:/home/$(USER) \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$(DISPLAY) \
	kartoza/qgis-desktop:latest; xhost -



# ---------------------------------------------------------------------------
#    S T A G I N G     C O M M A N D S
# ----------------------------------------------------------------------------

staging-run: staging-build staging-web

staging-deploy: staging-run staging-migrate staging-collectstatic
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh staging instance "
	@echo "You can access it on http://localhost:61101"
	@echo "------------------------------------------------------------------"

staging-build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging build

staging-web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging up -d stagingweb
	#@dipall

staging-migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging run uwsgi python manage.py migrate

staging-collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in staging mode"
	@echo "------------------------------------------------------------------"
	#@docker-compose -p $(PROJECT_ID)-staging run uwsgi python manage.py collectstatic --noinput
	#We need to run collect static in the same context as the running
	# uwsgi container it seems so I use docker exec here
	@docker exec -t -i $(PROJECT_ID)staging_uwsgi_1 python manage.py collectstatic --noinput

staging-kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in staging mode"
	@echo "------------------------------------------------------------------"

	@docker-compose -p $(PROJECT_ID)-staging kill

staging-rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing staging instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging rm

staging-logs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing uwsgi logs in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging logs uwsgi

staging-nginxlogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing nginx logs in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging logs web

staging-shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-staging run uwsgi /bin/bash

staging-dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in staging database"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)staging_db_1 psql -U docker -h localhost gis

staging-qgis:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running QGIS desktop in staging mode"
	@echo "Make sure you have started the services with make run first"
	@echo "------------------------------------------------------------------"
	@xhost +; docker run --rm --name="qgis-desktop-2-4" \
	-i -t \
	--link $(PROJECT_ID)staging_db_1:db \
	--link $(PROJECT_ID)staging_qgisserver_1:qgisserver \
	--volumes-from $(PROJECT_ID)_qgisserver_1 \
	-v ${HOME}:/home/$(USER) \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$(DISPLAY) \
	kartoza/qgis-desktop:latest; xhost -


# ---------------------------------------------------------------------------
#    D E V M O D E     C O M M A N D S
# ----------------------------------------------------------------------------

dev-run: dev-build dev-web

dev-deploy: dev-run dev-migrate dev-collectstatic
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh dev instance "
	@echo "You can access it on http://localhost:61101"
	@echo "------------------------------------------------------------------"

dev-build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev build

dev-web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev up -d devweb
	#@dipall

dev-migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev run devuwsgi python manage.py migrate

dev-collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in dev mode"
	@echo "------------------------------------------------------------------"
	#@docker-compose -p $(PROJECT_ID)-dev run devuwsgi python manage.py collectstatic --noinput
	#We need to run collect static in the same context as the running
	# uwsgi container it seems so I use docker exec here
	@docker exec -t -i $(PROJECT_ID)dev_devuwsgi_1 python manage.py collectstatic --noinput

dev-kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in dev mode"
	@echo "------------------------------------------------------------------"

	@docker-compose -p $(PROJECT_ID)-dev kill

dev-rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing dev instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev rm

dev-logs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing uwsgi logs in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev logs devuwsgi

dev-nginxlogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing nginx logs in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev logs devweb

dev-shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID)-dev run devuwsgi /bin/bash

dev-dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in dev database"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)dev_devdb_1 psql -U docker -h localhost gis

dev-qgis:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running QGIS desktop in dev mode"
	@echo "Make sure you have started the services with make run first"
	@echo "------------------------------------------------------------------"
	@xhost +; docker run --rm --name="qgis-desktop-2-4" \
	-i -t \
	--link $(PROJECT_ID)dev_db_1:db \
	--link $(PROJECT_ID)dev_qgisserver_1:qgisserver \
	--volumes-from $(PROJECT_ID)_qgisserver_1 \
	-v ${HOME}:/home/$(USER) \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$(DISPLAY) \
	kartoza/qgis-desktop:latest; xhost -
