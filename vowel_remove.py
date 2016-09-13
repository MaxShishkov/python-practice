def anti_vowel(text):
    for letter in text:
        if letter in "aoeuiAOEUI":
            text = text.replace(letter, "")
    return text