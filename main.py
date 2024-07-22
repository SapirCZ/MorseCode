morse_code = {
    "a": ".- ",
    "b": " -... ",
    "c": " -.-. ",
    "d": " -.. ",
    "e": " . ",
    "f": " ..-. ",
    "g": " --. ",
    "h": " .... ",
    "i": " .. ",
    "j": " .--- ",
    "k": " -.- ",
    "l": " .-.. ",
    "m": " -- ",
    "n": " -. ",
    "o": " --- ",
    "p": " .--. ",
    "q": " --.- ",
    "r": " .-. ",
    "s": " ... ",
    "t": " - ",
    "u": " ..- ",
    "v": " ...- ",
    "w": " .-- ",
    "x": " -..- ",
    "y": " -.-- ",
    "z": " --..",
    " ": " ",
    "1": ".---- ",
    "2": " ..--- ",
    "3": " ...-- ",
    "4": " ....- ",
    "5": " ..... ",
    "6": " -.... ",
    "7": " --... ",
    "8": " ---.. ",
    "9": " ----. ",
    "0": " ----- ",
    "-": " -....- ",
    "=": " -...- ",
    ",": " --..-- ",
    ".": " .-.-.- ",
    "/": " / ",
    "?": " ..--.. ",
    ";": " -.-.-."
}


def translate(string_to_translate: str) -> str:
    return "".join([morse_code[letter] if letter in morse_code else letter for letter in string_to_translate.lower()])


print(translate(input('Write text in English and it will translate into Morse:')))
