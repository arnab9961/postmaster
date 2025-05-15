# Postmaster Docker Solution

## The Issue
You encountered an error: "Bind for 0.0.0.0:9000 failed: port is already allocated"

This happens because port 9000 is already being used by another service on your system.

## Solution Implemented
I've made the following changes to resolve this issue:

1. Modified `docker-compose.yml` to use port 9052 externally (matching your development setup) while keeping the internal container port as 9000
2. Added support for a configurable port via the HOST_PORT environment variable
3. Updated the README.docker.md documentation to reflect these changes

## How to Run Your Container

### With Docker Compose (Recommended):
```bash
# Run with default port (9052)
sudo docker compose up -d

# OR specify a custom port if 9052 is also in use
sudo HOST_PORT=8080 docker compose up -d
```

### With Docker directly:
```bash
sudo docker build -t postmaster .
sudo docker run -p 9052:9000 --env-file .env -d postmaster
```

## Checking Your Container
```bash
# List running containers
sudo docker ps

# View logs
sudo docker logs <container_id>

# Stop the container
sudo docker compose down
```

## Permanent Docker Permission Fix
If you want to run Docker without sudo, you can add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Then logout and log back in for the changes to take effect.
