from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path,convert_from_bytes
import os
import boto3
from botocore.client import Config 
import tempfile
from celery import states
from celery import Celery

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
miniourl= 'http://minio:9000'

s3=boto3.resource('s3',
                    endpoint_url=miniourl,
                    aws_access_key_id='YOUR-ACCESSKEYID',
                    aws_secret_access_key='YOUR-SECRETACCESSKEY',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

bucket = s3.create_bucket(Bucket='pdf')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.pdfocr', bind=True)
def pdfExtraction(self, file):
    self.update_state(state=states.PENDING)
    doc={}
    pa=1
    #Get the file from S3
    fileobj = bucket.download_fileobj('mykey', data) #s3.get_object(Bucket= 'pdf',Key= key)
    filedata = fileobj['Body'].read()
    with open('filename', 'wb') as data:
        bucket.download_fileobj('mykey', data)
    # Convert pdf to array of images
    pages=convert_from_bytes(a)
    # extract text from images
    for p in pages:
        page="page-{}".format(pa)
        print(page)
        doc[page]=pytesseract.image_to_pdf_or_hocr(p,lang='fra', extension='hocr')
        pa+=1
    a.close()  
    return doc