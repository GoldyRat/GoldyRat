import math

# def exo_1():
#     a=12
#     a*=3
#     a-=17
#     a=a**4
#     a/=5
#     a+=23
#     a=math.sqrt(a)
#     print(f"The final result is : {a}")

# def exo_2(b):
#     a=b*2
#     a+=23
#     a/=3
#     a**=2
#     a+=25
#     a=math.sqrt(a)
#     print(f"For chosen number {b}, final result is: {a}")

def logical_and(b1, b2):
    depend = True
    if b1 and b2 == True:
        depend = True
    else:
        depend = False
    depend = f"{depend}"
    return depend

def logical_or(b1,b2):
    depend = True
    if b1 or b2 == True:
        depend = True
    else:
        depend = False
    depend = f"{depend}"
    return depend

print(logical_or(False, True))



# exo_1()
# exo_2(float(input("Value of b : ")))


