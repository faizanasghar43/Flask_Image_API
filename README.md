# FLASK Image BASE64 API example application

This is a simple example of how can you pass an image from a client side as BASE64 and then decode it back as an 
image to perform barcode or QRcode scanning.

There's only one route in it which is expecting a BASE64 encoded image to pass it further to a decoder+scanner function.

# Install 
- Reqiurements.txt contains all the packages.

# Run
- Open the terminal after installing all the packages requiered.
- Try "python run.py" or execute "run.py" from your IDE.

# Example of Use 
The REST API to the example app is described below.

import requests
body = {"image": 'iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEUAAAD///+l2Z/dAAAAAWJLR0QB/wIt3gAAAXlJREFUWEft1jGO5CAQheEfETjkCNwELmbJLXEx+yYcocIKLL8JvNKOe2ekjUwHrgx9CVCCeuj3Mh588MEH39EBJKlrs9iBOBir1L0wZ69qXVIbjIXYvdrSCRa7kz4CS1L3ktrHIMxQbfkErFL3YLFrTfqx2TcjwHlzJbWfnsPNeNZmiwh/1yPxSDuQdghGBpbBKFtESa17UBP1ez+H4JF2tKYXHtQ0aTiuqQmIohoQRqND7NNm4EGtT9twDLYI0guHpU+bNBgBqHplL8x4SW0wFhYRtDPJ5uzhstsRGGyGYHPWcQ6XOBa1JkmyqEnas9bLJzUAz/R2JGnabJFXvTf7ZpQkTZt2vCT1abNvux2BHix2qsUuGRDemn07SpK86pUliz9d3834J5swMx2pdb8eZQTWM70t5+T161wZgYXYtUmdYLx/GOPQyDqSzjEzHp3UugPZr+F3BFapa017JmiH61wZgQCSmqja8z9h6Xb8pR588MEH/x+/AK6v4JA2HX67AAAAAElFTkSuQmCC'}
response = requests.post("http://127.0.0.1:5000/api/getphoto", body["image"])
response.json() 
 This is an example reqeust from client side .
 The server will get the Base64 image, decode Base64 and then at the end will process the image to get the data from barcode or qrcode in that image.
