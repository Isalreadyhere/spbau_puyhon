
def gcdsimple (a, b):
    while (a != b) and (a != 0) and (b != 0):
        
        if a > b:
            a = (a % b)
        else: b = b % a
        d = max(a,b)
    return(d)

print(gcdsimple(12, 15))
input()