import base64

def decodeImage(imgstring, filename):
    imgdata=base64.b64decode(imgstring)

    with open(filename,"wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(cropped_image_path):
    with open(cropped_image_path,"rb") as f:
        return base64.b64encode(f.read())
    