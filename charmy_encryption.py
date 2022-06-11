import time


encode = {"a": "!",
             "b": "'",
             "c": "^",
             "d": "+",
             "e": "%",
             "f": "&",
             "g": "/",
             "h": "(",
          "ı": "8",
             "i": ")",
             "j": "=",
             "k": "?",
             "l": "_",
             "m": ">",
             "n": "£",
             "o": "#",
             "p": "$",
             "r": "½",
             "s": "{",
             "t": "[",
             "u": "]",
             "v": "}",
            "w": "1",
             "y": "|",
             "z": "~",
             " ": " ",
             ".": ".",
          "?": "5",
          "8": "ı",
          "ş": "6",
          "ğ": "ğ"

             }

decode = {"!": "a",
             "'": "b",
             "^": "c",
             "+": "d",
             "%": "e",
             "&": "f",
             "/": "g",
             "(": "h",
             ")": "i",
             "=": "j",
             "?": "k",
             "_": "l",
             ">": "m",
             "£": "n",
             "#": "o",
             "$": "p",
             "½": "r",
             "{": "s",
             "[": "t",
             "]": "u",
             "}": "v",
             "|": "y",
             "~": "z",
             " ": " ",
             ".": ".",
          "5":"?",
          "1": "w",
          "6": "ş",
          "8": "ı",
          "ğ": "ğ"

             }

print("Charmy $!$$)[{#£ encode&decode'r\n")
time.sleep(0.4)
encode_decode = input("E for encode, D for decode: ").lower()


def hash():
    if encode_decode == "e":
        encrypt = input("Type to encrypt! ").lower()
        for char in encrypt:
            print(encode[char], end="")

    elif encode_decode == "d":

        decrypt = input("Type to decrypt! ").lower()
        for char in decrypt:
            print(decode[char], end="")
            time.sleep(0.1)
        print(" laa~")

    else:
        print("Unauthorized user! System is self destroying ")





hash()


