def generate_hashtag(s):
    h1=s.title().replace(" ","")
    if len(h1)>140:return False
    if len(h1)==0:return False
    else:h2="#"+h1 
    return h2
