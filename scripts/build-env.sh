#!/usr/bin/env bash
# Used by CircleCI to build environment for code testing

set -xe

apt-get update

echo Updating conda...
conda update conda

echo Building environment...
conda env update --name root -f environment.yml
