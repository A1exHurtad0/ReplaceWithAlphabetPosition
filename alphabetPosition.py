def alphabet_position(text):
    newlist = [ord(x.upper()) - 64 for x in text if 64 < ord(x) < 91 or 96 < ord(x) < 123]    
    return(" ".join([str(_) for _ in newlist]))
