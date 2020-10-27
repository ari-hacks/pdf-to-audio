#!/bin/bash
sudo apt-get install -y poppler-utils
sudo apt-get install poppler-dev
sudo apt-get install build-essential
sudo apt-get install libpoppler-cpp-dev
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
sudo apt-get install -y pkg-config

