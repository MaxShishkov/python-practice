def censor(text, word):
    cens_word = ""
    for i in range(0,len(word)):
        cens_word += "*"
    
    text = text.replace(word, cens_word)
    
    return text
    
    
    
print censor("this hack is wack hack", "hack")