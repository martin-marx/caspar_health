#!/bin/bash

brew update # Update the list of packages
brew install docker-compose # Install Docker Compose
brew install git # Install Git
brew install git-lfs # Install Git lfs
git lfs install

docker build -t airflow_with_deps:1.0 . # Build the image for Apache Airflow
