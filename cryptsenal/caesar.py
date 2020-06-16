"""
description: caesar cipher
author: ao wang
date: june 16, 2020
"""


from cipher import Cipher


class Caesar(Cipher):
    def __init__(self, text, key):
        super().__init__(text)
        self.key = key

    def encrypt(self):
        self.text = list(self.removePunctuation())
        self.text = [(self.charToInt(char) + self.key) for char in self.text]
        return "".join([self.intToChar(num) for num in self.text])

    def decrypt(self):
        self.text = list(self.removePunctuation())
        self.text = [(self.charToInt(char) - self.key) for char in self.text]
        return "".join([self.intToChar(num) for num in self.text])

    def getKey(self):
        return key

    def setKey(self, key):
        self.key = key


if __name__ == "__main__":
    c = Caesar("EFGFOEUIFFBTUXBMMPGUIFDBTUMF", 27)
    print(c.decrypt())