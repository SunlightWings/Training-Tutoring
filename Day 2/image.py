## IMage:
from PIL import Image

# Reading and displaying an image
def read_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()  # Opens the image in the default image viewer
        print(f"Image loaded successfully from {image_path}")
    except FileNotFoundError:
        print(f"Image file {image_path} not found.")
    except Exception as e:
        print(f"Error loading image: {e}")

# Example usage
image_path = "james.jpeg"  # Provide the path to the image file
read_image(image_path)
