#!/bin/bash

# DOCKER -------------------------------------------------------
file := "docker-compose.yml"

up:
# Create the image and container
ifeq (${file}, "docker-compose.yml")
	sudo docker-compose -f ${file} up -d
else
	sudo docker-compose -f ${file} up
endif


start:
	# Start containers
	sudo docker-compose -f ${file} start

stop:
	# Stop containers
	sudo docker-compose -f ${file} stop

