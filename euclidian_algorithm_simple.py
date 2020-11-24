def gcdsimple (first_number, second_number):
    '''Нахождение НОД самым простым способом'''
    while (first_number != second_number) and (first_number != 0) and (second_number != 0):  
        if first_number > second_number:
            first_number = (first_number % second_number)
        else: second_number = second_number % first_number
        gcd_ofnumbers = max(first_number,second_number)
    return(gcd_ofnumbers)
print(gcdsimple(12, 15))
