# Postmaster

## Docker Setup

### Build and run using Docker Compose
```bash
docker compose up -d
```

The application will be available at http://localhost:9052 by default.

You can choose a different port by setting the HOST_PORT environment variable:
```bash
HOST_PORT=8080 docker compose up -d
```

### Build and run using Docker directly
```bash
# Build the Docker image
docker build -t postmaster .

# Run the container (change the first port number if 9052 is also in use)
docker run -p 9052:9000 --env-file .env -d postmaster
```

### Environment Variables
Make sure your `.env` file contains:
```
deepseek_api_key = your_api_key_here
```

## Development
For local development without Docker:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9052
```
