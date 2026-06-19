#!/bin/bash

set -e

cd /home/bennett/stack/websites/kervian.com

echo "Pulling latest changes..."
git pull

echo "Installing dependencies..."
npm install

echo "Building site..."
npm run build

echo "Deploy complete."

