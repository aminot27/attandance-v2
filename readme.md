Now, let’s hop into the interactive Python shell and play around with the free API Django gives you. To invoke the
Python shell,
use this command:

```bash
python manage.py shell
```

## Development

Now this project was based on
[Django Cookiecutter](https://github.com/pydanny/cookiecutter-django)

To start working on this project I highly recommend you to check
[pydanny's](https://github.com/pydanny)
[Django Cookiecutter](https://github.com/pydanny/cookiecutter-django)
[documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)

## Update dev_template_serv

Remove .docker folder

```bash
docker-compose -f compose-dev.yml build
docker-compose -f compose-dev.yml up

docker-compose -f compose-dev.yml up --build tech_store_serv_dev
docker-compose -f compose-prod.yml up -d --build tech_store_serv_prod
```

## Test

to run test based on unittest

```bash
python manage.py test
```

to run test based on pytest

```bash
pytest
```

to generate coverage based on unittest

```bash
coverage run manage.py test
```

to generate coverage report and coverage.xml

```bash
coverage report
coverage xml
```