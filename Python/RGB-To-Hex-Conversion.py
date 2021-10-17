def rgb(r, g, b):
    rgb_list = [r, g, b]
    for i in rgb_list:
        if i > 255:
            rgb_list [ rgb_list.index(i) ] = 255
        elif i < 0:
            rgb_list [ rgb_list.index(i) ] = 0
    return(str('{:02X}'.format(rgb_list[0])) + 
           str('{:02X}'.format(rgb_list[1])) + 
           str('{:02X}'.format(rgb_list[2])))
