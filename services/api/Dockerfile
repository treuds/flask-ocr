# For more information, please refer to https://aka.ms/vscode-docker-python
#FROM python:3.8-slim-buster
FROM ubuntu:20.04
RUN apt-get update -y && apt-get install -y libnfs-utils libnfs-dev python3  python3-pip gunicorn 
RUN apt-get clean && apt-get autoremove

EXPOSE 5000
 
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
RUN ls
# Install pip requirements
COPY ./requirements.txt .
#
COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt


# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
