from Converter import Converter
from ImageLoader import ImageLoader


class ASCII_Art:
    def __init__(self, path, strategy):
        self.image_path = path
        self.strategy = strategy
        self.__load()

    def __load(self):
        self.img_loader = ImageLoader()
        self.img_loader.load(self.image_path)

    def __construct_str(self):
        self.array = self.img_loader.image_to_array()
        converter = Converter()
        self.str = converter.convert(self.array, "luminosity")

    def display(self):
        self.__construct_str()
        print(f"\033[1;32;40m{self.str}\033[0m")

    def resize(self, new_height, new_weight):
        self.img_loader.resize(new_height, new_weight)


if __name__ == "__main__":
    photo = ASCII_Art("man.jpg", "average")
    # photo.resize(100, 100)
    photo.display()
