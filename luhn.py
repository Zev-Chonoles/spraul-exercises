#
#  This is my work regarding a problem in Chapter 2 of Spraul's "Think Like a Programmer":
#
#    Write a program that takes an identification number of arbitrary length and
#    determines whether the number is valid under the Luhn formula. The program must
#    process each character before reading the next one.
#
#  Because we don't know the length in advance, we don't know which digits we should be doubling
#  and taking the digit sum of until the end. This program tackles the problem by doing the
#  computations for both possibilities as we go along, then choosing the right one to output.
#

def digit_list(myint):
    return [int(a) for a in list(str(myint))]

def digit_sum_of_double(myint):
    return sum(digit_list(2 * myint))

def validity(check_digit):
    if check_digit == 0:
        return("Valid!")
    else:
        return("Invald :(")

doubled_odd_positions_check_digit  = 0
doubled_even_positions_check_digit = 0
current_position = 0
finished = False

print("\nType the digits, pressing enter after each,")
print("then press enter again when you're done.\n")

while(not finished):
    s = input()
    if s != "":
        newdigit = int(s)
        current_position += 1
        if current_position % 2 == 0:
            doubled_odd_positions_check_digit  += newdigit
            doubled_even_positions_check_digit += digit_sum_of_double(newdigit)
        else:
            doubled_odd_positions_check_digit  += digit_sum_of_double(newdigit)
            doubled_even_positions_check_digit += newdigit
        doubled_odd_positions_check_digit  %= 10
        doubled_even_positions_check_digit %= 10
    else:
        if (current_position % 2 == 0):
            print(validity(doubled_odd_positions_check_digit))
        else:
            print(validity(doubled_even_positions_check_digit))
        finished = True
