from PIL import Image


def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    image.save("encrypted_image.png")
    print("Image encrypted successfully.")
    print("Saved as: encrypted_image.png")


def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    image.save("decrypted_image.png")
    print("Image decrypted successfully.")
    print("Saved as: decrypted_image.png")


print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice (1/2): ")
image_path = input("Enter image path: ")
key = int(input("Enter encryption key: "))

if choice == "1":
    encrypt_image(image_path, key)

elif choice == "2":
    decrypt_image(image_path, key)

else:
    print("Invalid choice.")