from service import app, new_reader
from flask import request


@app.route('/api/getphoto', methods=['POST'])
def api_call():
    try:
        return new_reader(request.data)   #gets the encoded image and passes it to decoding + scanning function
    except:
        raise Exception(" Please add a valid QRcode/Barcode ")
