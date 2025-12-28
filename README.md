# QR Code Generator (Python)

## 📌 Project Overview

The **QR Code Generator** is a simple Python application that generates a QR code image from a user-provided URL. It uses the popular **qrcode** library to encode the URL into a scannable QR code and saves it as a PNG image.

This project is ideal for beginners learning how to work with external libraries, user input, and image generation in Python.

---

## 🎯 Features

* Takes a URL as user input
* Generates a QR code image
* Saves the QR code as a PNG file
* Simple and easy-to-understand implementation

---

## 🛠️ Technologies Used

* **Python 3**
* **qrcode** library
* **Pillow (PIL)** for image generation

---

## 📂 Project Structure

```
Qr_Code_Generator/
│
├── qrcode_generator.py    # Main Python script
└── qrcode.png             # Generated QR code image
```

---

## ▶️ How the Code Works

1. The user is prompted to enter a URL
2. Extra spaces are removed using `.strip()`
3. A QR code object is created
4. The URL is added to the QR code
5. The QR code image is generated and saved as a PNG file

---

## 🧾 Python Code

```python
import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"QR code generated and saved to {file_path}")
```

---

## ▶️ How to Run the Project

### Step 1: Install Required Library

```bash
pip install qrcode[pil]
```

### Step 2: Run the Script

```bash
python qr_generator.py
```

### Step 3: Enter URL

Provide a valid URL when prompted. Example:

```
https://www.google.com
```

### Step 4: Output

A file named **qrcode.png** will be created in the same directory.

---

## 👤 Author

**Satya Thakur**
