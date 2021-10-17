def find_even_index(arr):
    solution_checker = False
    for i in range(len(arr)):
        split1 = arr[0 : i]
        split2 = arr[i + 1:]
        if split1 == []:
            split1 = [0]
        if split2 == []:
            split2 = [0]
        if sum(split1) == sum(split2):
            return(i)
            solution_checker = True
    if solution_checker == False:
        return(-1)
