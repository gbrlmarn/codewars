def sum_dig_pow(a, b):
    final_list=[]
    for i in range(a, b + 1):
        r = 0
        c= 1
        for d in str(i):
            r += int(d) ** c
            c += 1
        if r == i:
            final_list.append(r)
    return(final_list) 
