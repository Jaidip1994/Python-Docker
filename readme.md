## Create a virtual env
```bash
python -m venv venv
``` 
# Run the application locally
## Install the dependency 
```bash
pip install requirements.txt
```

## Run the server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload  
```

## Hit the Apis
- http://localhost:8000/ - Health check of the application
- http://localhost:8000/channel/jackherrington 
    - Retrieve information about cetain channel id
    - If you want to test with different channel id please try to refer to channels.json and use the corresponding channel id

# Run the application using Docker
## Build the Docker Images
```bash
docker build -t channel-api . 
```

## Run the built images
```bash
docker run -d -p 8080:80 channel-api  
```

# Run the application using Docker Compose
```bash
docker-compose up --build 
```