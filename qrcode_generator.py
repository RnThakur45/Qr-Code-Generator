import qrcode

url = input("Enter the URL to generate QR code: ").strip() #removes extra spaces
file_path = "qrcode.png"

qr = qrcode.QRCode() #create a QR code object
qr.add_data(url)    #add the URL data to the QR code

img = qr.make_image() #generate the QR code image
img.save(file_path)

print(f"QR code generated and saved to {file_path}")