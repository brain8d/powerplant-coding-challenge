# Powerplant Coding Challenge ENGIE 

## Overview
This repository contains is for the coding challenge for a data engineering position in SPAAS team at ENGIE
For this challenge I decided to use FastAPI, as it allows for quick high performance web framework with Python

## Installation
Clone git repository 
```bash
git clone https://github.com/brain8d/powerplant-coding-challenge.git
```
Next step is to install dependencies \
`pip install -r requirements.txt`

## Launch API
To launch the API simply run the python script \
`python main.py`

# Use the API
Once the server is running you can access the API at:

`localhost:8888/docs`

Send a payload to API at /productionplan endpoint

`localhost:8888/productionplan`

You can use example filed in repo to send payload, i.e.

`
curl -X POST http://127.0.0.1:8888/productionplan/ \
-H "Content-Type: application/json" \
-d @examples/example_payloads.json
`

## Further Challenge
For the extra challenge I would have chosen to build a Dockerfile by copying the main.py and models, installing requirements, setting entrypoint and exposing port then then using a platform like Render to host the API there.
