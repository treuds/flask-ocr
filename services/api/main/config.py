"""Flask configuration."""
from os import environ, path


class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    #Celery
    CELERY_BROKER_URL=environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
    CELERY_RESULT_BACKEND=environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

    #MinIO
    MINIO_ENDPOINT= environ.get('MINIO_ENDPOINT','play.minio.io:9000')
    MINIO_ACCESS_KEY=environ.get('MINIO_ACCESS_KEY','Q3AM3UQ867SPQQA43P2F')
    MINIO_SECRET_KEY=environ.get('MINIO_SECRET_KEY','zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG')
    MINIO_SECURE= True
    MINIO_REGION = None
    MINIO_HTTP_CLIENT=None

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')