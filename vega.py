import os
import sys
import time
import pcfg
from pyfiglet import Figlet
from time import sleep as w


# Creating classes for: Visual, Base, Advanced parts
class Style:
    def __init__(self):
        self.types = ["[INFO]", "[WARN]", "[ERR]", "[LOG]", "[DEB]"]
        self.colors = ["YELLOW", "RED", "GREEN", "BLUE", "CYAN", "GREEN", "WHITE"]

    def t_color(self, type, color, text, wt):
        match wt:
            case 0:
                main = getattr(Fore, self.colors[color]) + self.types[type] + Style.RESET_ALL + text
                return main
            case 1:
                main = getattr(Fore, self.colors[color]) + self.types[type] + text + Style.RESET_ALL
                return main

    @staticmethod
    def text_print(text, duration):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(duration)

    @staticmethod
    def figlet(font, text, duration):
        f = Figlet(font=font)
        Style.text_print(f.renderText(text), duration)

class Main:
    def __init__(self):
        pass
