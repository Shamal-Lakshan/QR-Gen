# Importing library
import qrcode
import uuid

print()
print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
print("█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░██████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█")
print("█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█")
print("█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░▄▀░░██████████████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█")
print("█░░▄▀░░██░░▄▀░░███░░▄▀░░████░░▄▀░░██████████████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██░░▄▀░░█")
print("█░░▄▀░░██░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░░░░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")
print("█░░▄▀░░██░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")
print("█░░▄▀░░██░░▄▀░░███░░▄▀░░░░░░▄▀░░░░███░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")
print("█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░████████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░▄▀░░█")
print("█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█")
print("█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█")
print("█░░░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█")
print("█https://www.github.com/Shamal-Lakshan/QR-Gen████████████████████████████████████████████████████████████")
print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
print()
# Name of the QR Code Image file
QRCodefile = uuid.uuid1()

# Data for which you want to make QR Code
data = input("Enter the data you need to encode: ")
print()

# Getting a color for the qr code from the user
qr_color = input("Enter the color of the QR code (Foreground) (Black, White, etc...): ")
print()

# Getting a color for the qr code background from the user
bg_color = input("Enter the color of the background (Black, White, etc...): ")
print()

# instantiate QRCode object
qrObject = qrcode.QRCode()

# add data to the QR code
qrObject.add_data(data)

# compile the data into a QR code array
qrObject.make()
image = qrObject.make_image(fill_color=qr_color, back_color=bg_color)

# Saving image into a file
image.save(f'./output/{QRCodefile}.png')

# Saving the file
print("Processing your QR code...")
print(f'QR code saved as {QRCodefile}.png in the output folder')
