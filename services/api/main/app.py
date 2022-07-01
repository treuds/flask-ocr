from flask import Flask
from flask_restful import Api
from resources.User import User
from resources.Document import Document
from celery import Celery, states

app = Flask(__name__)


app.config.from_object('config.Config')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)


api = Api(app)
api.add_resource(Document, '/User', '/User/<string:id>')
api.add_resource(Document, '/Document', '/Document/<string:id>')