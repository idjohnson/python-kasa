FROM python:3.8.15
#FROM python:3.9
#FROM python:slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app
COPY . .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN pip install Flask
RUN pip install pipenv

# Adding new REST App
WORKDIR /usr/src/restapp
COPY ./cashman-flask-project/some.sh ./cashman-flask-project/swap.sh ./cashman-flask-project/Pipfile ./cashman-flask-project/Pipfile.lock ./cashman-flask-project/bootstrap.sh ./
COPY ./cashman-flask-project/restapi ./restapi

# Install API dependencies
RUN pip install pipenv --upgrade
RUN pipenv lock
RUN pipenv install --system --deploy

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/restapp/bootstrap.sh"]

#harbor.freshbrewed.science/freshbrewedprivate/kasarest:1.1.5