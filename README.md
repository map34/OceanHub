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
# Note, these are not sequential steps. You can use any of them independently of each other.

# To run bash shell
docker-compose -f infra/docker_dev/docker-compose.yml run --rm oceanhub_server bash

# To run Flask Python shell
docker-compose -f infra/docker_dev/docker-compose.yml run --rm oceanhub_server bash -c "source activate TEST && python backend/server/manage.py shell"

# To run the cluster up
docker-compose -f infra/docker_dev/docker-compose.yml up
```
