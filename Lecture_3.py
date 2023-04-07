# In Python, one can take input directly from the user using the input() function. 
# The input() function prompts the user to enter input from the keyboard, and returns a string containing the user's input.
Field_of_experiance = input('Whate is your field of experience? ')
Years = int(input('How many years of experiance do you have?' ))
print(type(Years))

# Operators. The in and not in operators are used to check whether a value or element is present in a sequence or not in Python. These operators can be used with strings, lists, tuples, sets, and other iterable objects.
if Years > 3:
    print(Field_of_experiance, 'You are eligible for admission.')
else:
    print('You need to do bridging courses. You are not eligible.')

print('This statement comes after the if else block')

name = input('Whate is the gene name? ')
if name == 'insulin':
     print('This is having a role to play in diabetes')
else:
    print('We will go back and search for insulin')

sequence = input('Type in the sequence: ')

if 'T' in sequence and 'U' not in sequence:
    print('DNA sequence')
elif 'T' not in sequence and 'U' in sequence:
    print('RNA sequence')
else:
    print('Sequence is incorrect')

number = int(input('Enter the number: '))

if number < 20 or number > 50:
    print('yes')
else:
    print('no')
  
sequence = input('Type in the sequence: ')

if 'A' in sequence and 'G' in sequence:
    print('Both A and G are present')
elif 'A' in sequence and 'G' not in sequence:
    print('G is not there')
elif 'A' not in sequence and 'G' in sequence:
    print('A is not there')
else:
    print('A and G are not there')