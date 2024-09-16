# APP-TESTS
Esta imagen contiene una Aplicación Flask para realizar tests de exámenes.


## Prerequisites

- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

## Ejecución de la aplicación
```
docker-compose up -d
```


## Tests
### Prerequisites
Para ejecutar los tests, antes asegúrate de tener instalado pytest y pytest-flask. Si no los tienes, puedes instalarlos con pip:

```
pip install pytest pytest-flask
```

Lanza los tests con:
```
pytest .
```
