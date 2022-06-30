from flask_restful import Resource

class Document(Resource):
    def post():
        #Upload to MinIO
        pass 
    def delete():
        pass
    def get(self, document_id):
        pass
    def search(self, text):
        #Call the elasticsearch service
        pass