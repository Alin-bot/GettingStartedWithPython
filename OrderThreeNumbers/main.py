
def printing_numbers(nr_1, nr_2, nr_3):
    print(nr_1 + ' ' + nr_2 + ' ' + nr_3)


def ordering(nr_1, nr_2, nr_3):
    if nr_2 == nr_1 == nr_3:
        print('Equal')
    else:
        if nr_1 < nr_2:
            if nr_1 < nr_3:
                if nr_2 < nr_3:
                    printing_numbers(nr_1, nr_2, nr_3)
                else:
                    printing_numbers(nr_1, nr_3, nr_2)
            else:
                printing_numbers(nr_3, nr_1, nr_2)
        else:
            if nr_1 < nr_3:
                printing_numbers(nr_2, nr_1, nr_3)
            elif nr_3 < nr_2:
                printing_numbers(nr_3, nr_2, nr_1)
            else:
                printing_numbers(nr_2, nr_3, nr_1)


ordering(input('First number is: '), input('Second number is: '), input('Third number is: '))
