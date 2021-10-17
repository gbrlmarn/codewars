def solution(n):
    roman_values={"M":1000,"CM":900, "D":500,"CD":400, "C":100,"XC":90, "L":50,"XL":40, "X":10,"IX":9, "V":5,"IV":4, "I":1}
    rom=""
    while n>0:
        for key in roman_values:
            if n>=roman_values[key]:
                rom+=key
                n-=roman_values[key]
                break
    
    return rom
