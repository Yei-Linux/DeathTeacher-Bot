import os
from subprocess import Popen
from io import BytesIO

import deep_animator.cli as deepAnimatorCli
import calendar
import time
from helpers.GoogleCloudHelper import GoogleCloudHelper
from helpers.ApiVideoHelper import ApiVideoHelper

class DeepFake:
    @staticmethod
    def generateFakerVideo(imageBytes,videoBytes):
        timeStamp = calendar.timegm(time.gmtime())
        file_name = 'DeepFakeVideo_'+str(timeStamp)+'.mp4'
        up_file_name = 'up_'+file_name

        full_path = os.path.dirname(os.path.abspath(__file__))
        generated_videos_path = os.path.join(full_path,'generated_videos')
        config_path = os.path.join(full_path,'conf.yml')
        checkpoint_path = os.path.join(full_path,'deep_animator_model.pth.tar')
        dest_path = os.path.join(full_path,'generated_videos',file_name)
        up_dest_path = os.path.join(full_path,'generated_videos',up_file_name)

        deepAnimatorCli.deep_animate_with_bytes(imageBytes,'.png',videoBytes,'.mp4',config_path,checkpoint_path,dest_path)
        process = Popen('ffmpeg -i '+file_name+' -vf  "setpts=0.30*PTS" '+up_file_name, shell=True, cwd=generated_videos_path)
        process.wait()
        buffer_file = open(up_dest_path,'rb')

        response = DeepFake.upload_to_gcp(buffer_file,file_name)

        buffer_file.close()

        os.remove(dest_path)
        os.remove(up_dest_path)

        return response

    @staticmethod
    def upload_to_gcp(buffer_file,file_name):
        gcp = GoogleCloudHelper()
        response = gcp.upload_blob(buffer_file,file_name)
        return response

    @staticmethod
    def upload_to_api_video(buffer_file,file_name):
        apiVideo = ApiVideoHelper()
        apiVideo.login('2iaAtIomq63PExQOjfnNjKTMD8MmBazmiST3HvuP4w1')
        response = apiVideo.upload(buffer_file,file_name)
        return response