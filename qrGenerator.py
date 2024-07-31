import qrcode   #first we need to install -> pip install qrcode in cmd
from pyzbar.pyzbar import decode    #->pip install pyzbar
from PIL import Image   #->pip install pillow

print("Enter the details for the QR code (type 'done' to finish):")

lines = []
while True:
    line = input()  #->input any link or text to qr-ed
    if line == "done":
        break
    lines.append(line)

content = "\n".join(lines)

# Generate the QR code
myqr = qrcode.make(content)
myqr.save("myqr.png")  # Save the QR code as an image file

# This is to Decode the QR code
#b = decode(Image.open("myqr.png"))
#decoded_content = b[0].data.decode("ascii")   # here b[0] indicates that we are giving permission in the 0th index

# Print the decoded content
#print("Decoded content from QR code:")
#print(decoded_content)
