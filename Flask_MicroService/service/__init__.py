import base64
from flask import Flask
from pyzbar import pyzbar
from PIL import Image
from io import BytesIO


app = Flask(__name__)


def new_reader(encoded_img):
<<<<<<< HEAD
    # decoding the base64 encoded image and opening it as an image
    img = Image.open(BytesIO(base64.b64decode(encoded_img)))
    qr_code = pyzbar.decode(img)[0]
    data = qr_code.data.decode("utf-8")
    type_ = qr_code.type
    return {"Type": type_, "Data": data}
=======
    img = Image.open(BytesIO(base64.b64decode(encoded_img)))    #decoding the base64 encoded image and opening it as an  image
    qr_code = pyzbar.decode(img)[0]
    data = qr_code.data.decode("utf-8")
    type_ = qr_code.type
    response = {"Type": type_, "Data": data}
    return response

>>>>>>> 9860fe7aee2b2efc7bd2abcf6596ec8a2999a1a5


from .routes import app