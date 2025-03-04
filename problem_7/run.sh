#!/bin/bash

# Build the Docker image
docker build -t csv-processor .

# Run the Docker container
# You can override input/output files if needed
docker run --rm csv-processor