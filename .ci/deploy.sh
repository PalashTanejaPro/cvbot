#!/usr/bin/env bash

# Continuous deployment to solar.cloudcv.io
# This script is meant to run on solar.cloudcv.io

# Execute this script in a CI environment with
# the required SSH added to the agent, with
# this command:
# $ ssh solar.cloudcv.io "bash -s" < /path/to/script

set -e -x

WORK_DIR=/opt/solar/cvbot

fail() {
    echo "FAIL: $*"
    exit 1
}

cd $WORK_DIR || \
    fail "It looks like $WORK_DIR doesn't exist"

docker-compose pull || \
    fail "An error has occured during updating the image(s)"

docker-compose up --force-recreate -d || \
    fail "An error has occured during deploying the container(s)"

sleep 5s

docker-compose ps
