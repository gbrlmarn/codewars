def domain_name(url):
    
    if url.split(".")[0] == "http://www" or url.split(".")[0] == "https://www":
        domain = url.split(".")[1]    
    elif url[0] == "h":
        domain = url.split("://")[-1].split(".")[0]
    elif url[0] == "w":
        domain = url.split("www.")[-1].split(".")[0]
    else:
        domain = url.split(".")[0]
    return domain
