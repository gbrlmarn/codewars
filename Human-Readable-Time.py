def make_readable(seconds):
    SS = seconds % 60
    MM = (seconds // 60) % 60
    HH = (seconds // 60) // 60
    return(str(HH).zfill(2) + ":" + str(MM).zfill(2) + ":" + str(SS).zfill(2))
