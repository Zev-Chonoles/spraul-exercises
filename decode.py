#
#  This is my work regarding a problem in Chapter 2 of Spraul's "Think Like a Programmer":
#
#    A message has been encoded as a text stream that is to be read character by character.
#    The stream contains a series of comma-delimited integers, each a positive number.
#    However, the character represented by a particular integer depends on the current
#    decoding mode. There are three modes: uppercase, lowercase, and punctuation.
#
#    In uppercase mode, each integer represents an uppercase letter: The integer modulo 27
#    indicates the letter of the alphabet (where 1 = A and so on). The lowercase mode works
#    the same but with lowercase letters. In punctuation mode, the integer is instead considered
#    modulo 9, with the interpretation given by the table below. At the beginning of each
#    message, the decoding mode is uppercase letters. Each time the modulo operation (by 27 or 9,
#    depending on mode) results in 0, the decoding mode switches,  U --> L --> P --> U.
#
#           1: !    2: ?    3: ,    4: .    5: (space)    6: ;    7: "    8: '
#

#-----------------------------------------------
#  Cycling through the different decoding modes.
#
#  I need the global declaration in "increment_mode" but not "current_mode"
#  because of this: http://stackoverflow.com/a/423668

current_mode_int = 0

decoding_modes = ["U", "L", "P"]

def current_mode():
    return decoding_modes[current_mode_int]

def increment_mode():
    global current_mode_int
    current_mode_int += 1
    current_mode_int %= len(decoding_modes)

#----------------------------------
#  Turning a list of strings into a string.

def str_list_into_str(l):
    return "".join(l)

#----------------------------------
#  Turning a list of integers (as strings) into an integer.

def str_list_into_int(l):
    return int(str_list_into_str(l))

#-----------------------------------------------
#  The rules for how to decode an integer (given as a list of digits).

decoding_info = {
    "U": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "L": "abcdefghijklmnopqrstuvwxyz",
    "P": "!?,. ;\"'"
}

def decode(l):
    chars = decoding_info[current_mode()]
    n = str_list_into_int(l) % (1 + len(chars))
    if n == 0:
        increment_mode()
        return ""
    else:
        return chars[n-1]

#--------------------------------------------------------------
#  Reading in comma-separated integers one character at a time.

result = []
current_digit_list = []
finished = False

print("\nType the integers separated by commas, pressing enter after each")
print("digit and comma, then press enter again when you're done.\n")

while(not finished):
    
    current_char = input()
    
    if current_char == "":
        if len(current_digit_list) == 0:
            print("Error: you have not entered any digits for the current integer yet.")
        else:
            result.append(decode(current_digit_list))
            print(str_list_into_str(result))
            finished = True
    
    elif current_char == ",":
        if len(current_digit_list) == 0:
            print("Error: you have not entered any digits for the current integer yet.")
        else:
            result.append(decode(current_digit_list))
            current_digit_list = []
    
    elif current_char not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        print("Error: invalid character")
    
    else:
        current_digit_list.append(current_char)


