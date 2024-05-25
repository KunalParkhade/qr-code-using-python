# QR Code Generator using Python

This repository contains a simple Python script to generate a QR code for a specified URL using the `qrcode` library. The QR code generated in this example links to a YouTube video.

## Repository Name
`qr-code-using-python`

## Description

This script demonstrates how to use the `qrcode` library in Python to create a QR code. The QR code generated in this script links to the Chiraj Jain "Time Complexity & common errors" Competitive Programming video on YouTube.

## Installation

To run this script, you need to have Python installed on your system. Additionally, you'll need to install the `qrcode` and `Pillow` libraries. You can install these libraries using `pip`.

```bash
pip install qrcode pillow
```

## Usage

1. Clone the repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/qr-code-using-python.git
   ```

2. Navigate to the directory.

   ```bash
   cd qr-code-using-python
   ```

3. Run the script.

   ```bash
   python qr_code.py
   ```

   This will generate a QR code image file named `youtube_qr.png` in the same directory.

## Code Explanation

Here's a breakdown of the script:

```python
import qrcode

# URL to be encoded in the QR code
website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Create a QRCode object with specific configuration
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Add data to the QR code
qr.add_data(website_link)
qr.make()

# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')

# Save the image to a file
img.save('youtube_qr.png')
```

- **Import the `qrcode` library**: The script starts by importing the `qrcode` library, which is used to generate QR codes.
- **Define the URL**: The `website_link` variable holds the URL that you want to encode in the QR code.
- **Create a QRCode object**: The `qr` object is created with specific parameters: `version` defines the size of the QR code, `box_size` defines how many pixels each box of the QR code is, and `border` defines the thickness of the border (in boxes).
- **Add data to the QR code**: The `add_data` method is used to add the URL to the QR code.
- **Generate the QR code**: The `make` method is called to generate the QR code based on the added data.
- **Create an image**: The `make_image` method creates an image of the QR code with specified foreground (`fill_color`) and background (`back_color`) colors.
- **Save the image**: Finally, the generated QR code image is saved to a file named `youtube_qr.png`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes and also read the `Contributing.md` file for Contribution Guidelines. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or issues, please open an issue in the repository.

---

Thank you for using this QR code generator script!

Repo owner - @KunalParkhade