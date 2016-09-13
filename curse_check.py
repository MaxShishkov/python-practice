import urllib

def read_text():
    quotes = open("E:\\MyCode\\python\\text.txt",'r')
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    connection.close()

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No curse words are found.")
    else:
        print("Could not scan the document")
    
read_text()
