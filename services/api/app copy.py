from flask import Flask, render_template, request
from flask_restful import Resource, Api

import os
import boto3
from botocore.client import Config
from celery import Celery, states
import uuid



# allow files of a specific type
ALLOWED_EXTENSIONS = set(['pdf','png', 'jpg', 'jpeg'])

app = Flask(__name__,static_url_path='', static_folder='./client/build')
api = Api(app)


class Document(Resource):
    def post():
        #Upload to MinIO
        pass 
    def get(self, document_id):
        pass
    def search(self, text):
        #Call the elasticsearch service
        pass

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
s3 = boto3.resource('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id=os.environ.get(),
                    aws_secret_access_key=os.environ.get(),
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')
bucket_name="documents"
bucket = s3.create_bucket(Bucket='pdf')
#bucket.upload_fileobj(data, 'bucket_name', 'mykey')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file_string = base64.b64encode(file.read())
            exten=file.filename.rsplit('.', 1)[1].lower()
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            filename="{}.{}".format(uuid.uuid4().hex,exten)
            print(filename)
            try:
                bucket.upload_fileobj(file_string)
                celery.send_task('tasks.pdfocr',kwargs={'file':filename
                })
            except:
                pass


            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text['page-1'],
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')