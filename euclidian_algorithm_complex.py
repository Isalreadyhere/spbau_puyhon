def gcdcomplex (first_numb,sec_numb,first_coef = 0,sec_coef = 0):
    if first_numb !=0:
        gcd_ofnumbers,first_coef,sec_coef = gcdcomplex(sec_numb%first_numb, first_numb, first_coef, sec_coef)
        first_coef,sec_coef = sec_coef - (sec_numb // first_numb) * first_coef , first_coef
    else: 
        first_coef = 0
        sec_coef = 1
        gcd_ofnumbers = sec_numb
    return gcd_ofnumbers, first_coef, sec_coef
def write (first_num,sec_num):
    gcd_2,first_coef2,second_coef2 = gcdcomplex(first_num , sec_num )
    print(first_coef2,' * ', first_num, ' + ',  second_coef2, ' * ', sec_num, ' = ', gcd_2  )
    return()
write(5,7)
write(24, 48)
write(12, 15)
write(9, 24)
write(9, 1024)
write(1024, 9)
