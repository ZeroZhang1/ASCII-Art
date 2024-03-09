import numpy as np
from ImageLoader import ImageLoader


class Converter:
    def __init__(self):
        self.array = None
        self.width = None
        self.height = None
        self.ASCII_array = None
        self.strategy_functions = {
            "average": self.__average_convert,
            "lightness": self.__lightness_convert,
            "luminosity": self.__luminosity_convert
        }

    def convert(self, source_array, strategy="average"):
        self.array = source_array
        self.width = source_array.shape[1]
        self.height = source_array.shape[0]
        self.ASCII_array = np.zeros((self.height, self.width), dtype=int)
        self.__num_convert(strategy)
        ASCII_list = " `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
        number_of_characters = len(ASCII_list) - 1
        str_list = []

        for h in range(self.height):
            for w in range(self.width):
                character_position = number_of_characters - round((self.ASCII_array[h][w] / 255) * number_of_characters)
                character = ASCII_list[int(character_position)//6]
                for i in range(2):
                    str_list.append(character)
            str_list.append('\n')

        result_string = ''.join(str_list)
        return result_string

    def __num_convert(self, strategy):
        strategy = strategy.strip().lower()

        if strategy in self.strategy_functions:
            return self.strategy_functions[strategy]()
        else:
            raise ValueError("Unsupported conversion strategy")

    def __average_convert(self):
        rgb_channels = self.array[:, :, :3]
        self.ASCII_array = np.mean(rgb_channels, axis=-1, dtype=int)
        return self.ASCII_array

    def __lightness_convert(self):
        rgb_channels = self.array[:, :, :3]
        self.ASCII_array = (np.max(rgb_channels, axis=-1) + np.min(rgb_channels, axis=-1)) // 2
        return self.ASCII_array

    def __luminosity_convert(self):
        rgb_channels = self.array[:, :, :3]
        luminosity_values = np.dot(rgb_channels, [0.21, 0.72, 0.07])
        self.ASCII_array = luminosity_values.astype(int)
        return self.ASCII_array


if __name__ == "__main__":
    img = ImageLoader()
    img.load("test.jpg")
    array = img.image_to_array()
    img.close()
    con = Converter()
    new_array = con.convert(array,"luminosity")
    print(new_array)
