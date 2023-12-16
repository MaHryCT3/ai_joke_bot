TAIL=100

define set-default-container
	ifndef c
	c = bot
	else ifeq (${c},all)
	override c=
	endif
endef


set-container:
	$(eval $(call set-default-container))
build:
	docker compose -f docker-compose.yml build
up:
	docker compose -f docker-compose.yml up -d
down:
	docker compose -f docker-compose.yml down
logs: set-container
	docker compose -f docker-compose.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.yml exec $(c) /bin/bash

compile-reqs: set-container
	docker compose -f docker-compose.yml run --rm $(c) bash -c 'pip install pip-tools && pip-compile'

