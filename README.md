# OceanHub

See the beauty of the ocean from your favorite device

## Configs

* Use PowerShell or Bash shell for the steps below

## Build images

From the root folder of the project:

```bash
docker-compose -f infra/docker_dev/docker-compose.yml build
```

## Using Docker

From the root folder of the project:

```bash
# Run bash shell
docker-compose -f infra/docker_dev/docker-compose.yml run oceanhub_server bash

# Run Flask Python shell
docker-compose -f infra/docker_dev/docker-compose.yml run oceanhub_server bash -c "source activate TEST && python backend/server/manage.py shell"

# Run Flask server
docker-compose -f infra/docker_dev/docker-compose.yml run oceanhub_server bash -c "source activate TEST && python backend/server/manage.py runserver"
```
