import os
Windows = "nt"


class Color:
    if os == Windows:
        YELLOW = "Color 6"
        RED = "Color 4"
        GREEN = "Color 2"
        BLUE = "Color 1"
        WHITE = "Color F"
    else:
        YELLOW = "\033[33m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[94m"
        WHITE = "\033[97m"
