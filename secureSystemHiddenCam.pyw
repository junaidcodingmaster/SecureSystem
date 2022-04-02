import os
import cv2
import dropbox
import time
import random


start_time = time.time()


class TakePhoto:
    def main():
        file = open("SSController.txt", "r")

        mkLoop = True
        i = 1
        while mkLoop == True:
            i = i + 1
            status = file.read()
            name = TakePhoto.take_snapshot()
            TakePhoto.upload_file(name)
            TakePhoto.deleteImages(name)
            time.sleep(1)
            if status == "False":
                mkLoop = False
                break
            else:
                pass

            if i == 100:
                break

    def take_snapshot():
        number = random.randint(0, 100)
        # initializing cv2
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        i = 0
        while result:

            # read the frames while the camera is on
            ret, frame = videoCaptureObject.read()
            # cv2.imwrite() method is used to save an image to any storage device
            img_name = "img" + str(number) + ".png"
            cv2.imwrite(img_name, frame)
            start_time = time.time
            result = False
            print("\nsnapshot taken!\n")
        return img_name

    def token():
        file = open("token.txt", "r")
        access_token = file.read()
        return access_token

    def upload_file(img_name):
        access_token = TakePhoto.token()
        file = img_name
        file_from = file
        file_to = "/SecureSystem" + img_name
        dbx = dropbox.Dropbox(access_token)

        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
            print("\nfile uploaded!\n")

    def deleteImages(img_name):
        os.remove(img_name)


TakePhoto.main()
