from flask import Flask
import cv2
from pyzbar import pyzbar

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def barcode_reader(path):
    image = cv2.imread(path)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        response = {"Type": barcodeType, "Data": barcodeData}
        return response


from .routes import app