import qrcode

def generateQRcode(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(file_name)

# input url
text = input("URL: ")
# Save QR code
file_name = input("File Name: ")

# Generate QR code
generateQRcode(text,file_name)
print(f"QR code saved as {file_name}")
    