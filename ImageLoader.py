from PIL import Image
import numpy as np


def check(image_path):
    image_extension = image_path.split('.')[-1].lower()
    if image_extension == "jpg":
        return True
    return False


class ImageLoader:
    def __init__(self):
        self.array = None
        self.image = None
        self.image_path = None
        self.height = None
        self.width = None

    def load(self, image_path):
        if not check(image_path):
            print("Invalid image_path!")

        self.image_path = image_path
        try:
            self.image = Image.open(self.image_path)
            self.width = self.image.size[0]
            self.height = self.image.size[1]
        except Exception as e:
            print(f"Error occurred while loading the image: {e}")

    def resize(self, new_height, new_width):
        if self.image:
            self.image = self.image.resize((new_width, new_height))
            self.height = new_height
            self.width = new_width

    def info(self):
        if self.image:
            print("Image loaded successfully")
            if self.array is not None:
                print("Successfully constructed pixel matrix!")
            print("Image Format:", self.image.format)
            print("Image Mode:", self.image.mode)
            print(f"Image Size: {self.width}x{self.height}")
            if self.array is not None:
                print("Image Array Shape", self.array.shape)
        else:
            print("No valid image")

    def image_to_array(self):
        self.array = np.array(self.image)
        return self.array

    def close(self):
        self.image.close()


if __name__ == "__main__":
    img = ImageLoader()
    img.load("ascii-pineapple.jpg")
    img.image_to_array()
    img.resize(100, 100)
    img.info()
    img.close()
