
def gcdcomplex (a, b, x = 0, y = 0):
    if a != 0: 
       d,x,y = gcdcomplex(b%a, a, x, y)
       x,y = y - (b // a) * x , x
    else: 
       x = 0
       y = 1
       d = b
    return d, x, y

def write (a,b):
  t,y,u = gcdcomplex(a , b )
 
  print(y,' * ', a, ' + ',  u, ' * ', b, ' = ', t  )
  

  return()
write(5,7)
write(24, 48)
write(12, 15)
write(9, 24)
write(9, 1024)
write(1024, 9)
input()
