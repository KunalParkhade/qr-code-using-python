import qrcode

# URL to be encoded in the QR code
website_link = 'https://www.youtube.com/live/ws_AvHGigpg?si=zwnZ1ajO0_xWq8oO'

# Create a QRCode object with specific configuration
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Add data to the QR code
qr.add_data(website_link)
qr.make()

# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')

# Save the image to a file
img.save('youtube_qr.png')

from IPython.display import Image
Image(filename='youtube_qr.png')