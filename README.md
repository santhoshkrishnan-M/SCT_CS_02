# Image Encryption Tool Using Pixel Manipulation

## Overview

This project is a simple Image Encryption and Decryption Tool developed using Python and the Pillow (PIL) library. The application secures images by manipulating pixel values with a user-defined encryption key. The encrypted image can only be restored using the same key.

This project was completed as **Task 2** of the Cybersecurity Internship at SkillCraft Technology.

## Features

* Encrypt images using pixel manipulation
* Decrypt images using the same encryption key
* User-friendly command-line interface
* Supports common image formats
* Fast and lightweight implementation

## Technologies Used

* Python 3
* Pillow (PIL)

## How It Works

### Encryption

Each pixel's RGB values are modified using the formula:

```python
New Pixel Value = (Original Pixel Value + Key) % 256
```

### Decryption

The original image is restored using:

```python
Original Pixel Value = (Encrypted Pixel Value - Key) % 256
```

This ensures that the encryption and decryption processes are reversible when the correct key is used.

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd SCT_CS_2
```

3. Install the required library:

```bash
pip install pillow
```

## Usage

Run the program:

```bash
python image_encryption.py
```

You will see:

```text
1. Encrypt Image
2. Decrypt Image
```

Enter:

* Choice (1 or 2)
* Image path
* Encryption key

The program will generate:

* encrypted_image.png
* decrypted_image.png

## Example

### Encryption

Input:

```text
Choice: 1
Image Path: sample.png
Key: 50
```

Output:

```text
Image encrypted successfully.
Saved as: encrypted_image.png
```

### Decryption

Input:

```text
Choice: 2
Image Path: encrypted_image.png
Key: 50
```

Output:

```text
Image decrypted successfully.
Saved as: decrypted_image.png
```

## Learning Outcomes

Through this project, I learned:

* Basics of image encryption
* Pixel-level image manipulation
* Working with the Pillow library
* Encryption and decryption techniques
* Python file handling and image processing

