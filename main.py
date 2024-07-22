morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": " ",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "-": "-....-",
    "=": "-...-",
    ",": "--..--",
    ".": ".-.-.-",
    "/": "/",
    "?": "..--..",
    ";": "-.-.-."
}


# Function to translate text to Morse code
def translate(string_to_translate: str) -> str:
    # Join the Morse code for each letter in the input string
    return "".join([morse_code.get(letter, letter) for letter in string_to_translate.lower()])


# User input prompt
user_input = input("Write text in English to translate into Morse code: ")

# Print the translated Morse code
print("Morse Code Translation:", translate(user_input))
