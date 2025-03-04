Copy#!/bin/bash

# Docker იმიჯის აგება
docker build -t weather-api .

# Docker კონტეინერის გაშვება
docker run -p 8000:8000 weather-api