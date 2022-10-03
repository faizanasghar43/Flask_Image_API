from service import app, barcode_reader
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    try:
        if request.method == 'POST':
            if request.files:
                image = request.files['image']
                response = barcode_reader(image.filename)
                return render_template("response.html", response=response)
        return render_template("upload.html")
    except:
        raise Exception(" Please add a valid QRcode/Barcode ")
