#!/bin/bash

sudo apt-get update # Update the list of packages
sudo apt-get install docker-compose-plugin # Install Docker Compose
sudo apt-get install git # Install Git
sudo apt-get install git-lfs # Install git-lfs
git lfs install

docker build -t airflow_with_deps:1.0 . # Build the image for Apache Airflow
