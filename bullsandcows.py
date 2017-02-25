import random

#function for generation random number
def gen_number():
    debug = 0

    secret = str(random.randint(0, 9))
    if debug == 1:
        print("Random number: " + secret)

    a = 1
    while (a < 4):
        while True:                 # while number is different from others
            gen = str(random.randint(0, 9))
            unique = True
            for b in range(0, a):  # Is it unique?
                if debug == 1:
                    print("Random number: " + secret[b])
                if secret[b] == gen:
                    unique = False
            if unique == True:      # It is unique!!
                secret += gen
                a += 1
                break
    return secret

#function for comparation numbers
def compare_num (data , secret):
    debug = 0

    cows = 0
    bulls = 0
    match = list("OOOO")

    if data == secret:              # Is it right number
        bulls = 4
    else:
        if debug == 1:
            print("It's not right number")

        for i in range(4):          # index of strings starts 0 ends with 3
            if str(data)[i] == str(secret)[i]:
                match[i] = 'X'      # BULL- dont use this position from secret
                bulls += 1

        if debug == 1:
            print("MATCH: %s" % match)

        for i in range(4):  # index of strings starts 0
            if debug == 1:
                print ( "i: %d" % i)
            if match[i] != 'X':  # was a BULL?
                for n in range(4):
                    if match[n] != 'x':  # was a COW?
                        if debug == 1:
                            print("i: %d n: %d" % (i, n))
                        if str(data)[i] == str(secret)[n]:
                            if debug == 1:
                                print("COW i: %d n: %d" % (i, n))
                            match[n] = 'x'  # COW - dont use this position from secret
                            cows += 1
                            if debug == 1:
                                print("MATCH: %s" % match)
                            continue
    return [ bulls, cows ]

# main program
if __name__ == '__main__':
    debug = 0
    print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n")

    secret = gen_number()
    guesses = 0

    # secret = 9123
    print("SECRET: " + secret + "\n")

    while True:            #main cycle
        again = True    #read user number
        while again:
            data = str(input("Enter a number:"))  # input returns string
            again = False

            try:                    # Is it number?
                temp = int(data)
            except ValueError:
                print("That's not a number!")
                again = True
                continue            # Try it again

            if len(data) != 4:      # Is it right length?
                again = True
                print("Please give 4 numbers.")
                continue            # wrong length, try it again

            for a in range(4):      # Is it unique?
                for b in range(a + 1, 4):
                    if data[a] == data[b]:
                        print("Please give 4 UNIQUE numbers.")
                        again = True

        # User gave correct input
        d = compare_num (data, secret)
        guesses += 1

        if debug == 1:
            print("Return of func compare_num %d" % d)

        print("BULLS: %s COWS: %s" % (d[0], d[1]))

        if ( d[0] == 4 ):           # Does bulls equal 4?
            print("Correct, you've guessed the right number in %d guesses!" % guesses)
            break;