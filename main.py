import math  # imports 'math' module that allows more complex calculations
import random  # imports a library allowing generation of random numbers

print("PART I:")

random_number1 = random.randint(1, 6)
# this assigns a random number from 1 to 6 to 'random_number1'

random_number1_cubed = math.pow(random_number1, 3)
# raises 'random_number' to the power of 3

print('The 1st random number generated is:', random_number1)
print('And', random_number1, 'raised to the third power equals', random_number1_cubed)
# prints both random number and its value cubed

print()

print('PART II:')

random_number2 = random.randint(51, 100)
# assigns random number from 51 to 100 to 'random_number2'

random_number2_sqrt = (math.sqrt(random_number2))
# assigns the square root of 'random_number2' to 'random_number2_sqrt'

print('The 2nd random number generated is:', random_number2)
print('And the square root of', random_number2, 'is', random_number2_sqrt)

print()

print('PART III:')

random_number3 = random.randint(10001, 30000)
# assigns a random number between 10001 and 30000 to 'random_number3'

print('The random number is:', random_number3)
print('And its digits are:')

random_number_ones = int(random_number3 % 10)
# gets the ones digit out of the random number
print(random_number_ones)

random_number_tens = int((random_number3 // 10) % 10)
# gets the tens digit out of the random number
print(random_number_tens)

random_number_hundreds = int((random_number3 // 100) % 10)
# gets the hundreds digit out of the random number
print(random_number_hundreds)

random_number_thousands = int((random_number3 // 1000) % 10)
# gets the thousands digit out of the random number
print(random_number_thousands)

random_number_ten_thousands = int((random_number3 // 10000) % 10)
# gets the ten thousands digit out of the random number
print(random_number_ten_thousands)
