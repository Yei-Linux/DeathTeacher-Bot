from google.cloud import storage
import os

class GoogleCloudHelper:
    def __init__(self):
        full_path = os.path.dirname(os.path.abspath(__file__))
        jsonPath = os.path.join(full_path, '../','config','keys.json')

        self.storage_client = storage.Client.from_service_account_json(jsonPath)
        self.bucket_name = 'cinetask.appspot.com'

    def upload_blob(self,file_stream,file_name):

        bucket = self.storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_file(file_stream,content_type='video/mp4')

        return 'Uploaded correctly'

    def getSignedUrlOfFile(self,nameFile):
        return 'https://storage.googleapis.com/'+self.bucket_name+'/'+nameFile