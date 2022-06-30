from flask import Flask
from flask_restful import Api
from resources.User import User
from resources.Document import Document
from celery import Celery, states


app = Flask(__name__,static_url_path='', static_folder='./client/build')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL 
app.config['CELERY_RESULT_BACKEND'] = CELERY_RESULT_BACKEND

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)

api = Api(app)
api.add_resource(Document, '/User', '/User/<string:id>')
api.add_resource(Document, '/Document', '/Document/<string:id>')