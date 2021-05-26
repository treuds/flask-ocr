from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path,convert_from_bytes
import os 
import tempfile
from celery import states
from celery import Celery
import libnfs

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
NFS_SERVER=os.environ.get(NFS_SERVER, 'nfs://127.0.0.1/data/tmp/')
nfs = libnfs.NFS(NFS_SERVER)

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.pdfocr', bind=True)
def pdfExtraction(self, file):
    self.update_state(state=states.PENDING)
    doc={}
    pa=1
    #Open the file from the nfs server
    a = nfs.open(file, mode='w+')
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