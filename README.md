# flask-ocr

A system for fulltext indexing of Haitian laws.
- Flask
- Celery
- MinIO
- Redis
- ElasticSearch
- tesseract

## Docker Compose for API, Celery with Redis, Minio

This Docker Compose configuration sets up a multi-container environment for your application. It includes the following services:

- `api`: Your API service.
- `redis`: Redis as the backend and result storage for Celery.
- `minio`: Minio for object storage.
- `celery`: Celery for task processing.

## Prerequisites

Before using this Docker Compose setup, ensure that you have Docker and Docker Compose installed on your system.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Usage

1. Clone this repository to your local machine.

2. In the root directory of the repository, create a `.env` file and specify your environment variables. You can use the provided `.env.example` as a template.

3. Run the following command to start the services:

   ```bash
   docker-compose up -d
   ```

   The `-d` flag runs the services in detached mode.

4. Access your services:

   - API: http://localhost:5000
   - Minio: http://localhost:9000
   - Celery: Configured to use Redis for both backend and result storage.

## Environment Variables

- `CELERY_RESULT_BACKEND` and `CELERY_BROKER_URL` are configured to use Redis for Celery task management, including both backend and result storage.
- Minio is configured with access and secret keys. Change these values for production use.

## Customization

You can modify the service configurations in the `docker-compose.yml` file to match your specific requirements.

## Networks

The services are connected to a custom bridge network called `backend`.

## Cleanup

To stop and remove the containers, use the following command:

```bash
docker-compose down
```

