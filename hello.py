# Easy project
# First ask user about some question
# Then mark the user answer
# If user got the right answer then give them 1 of each question

print('Welcome to the TEST', 'This is about general computer fundamental!!!')
x = input('What is the first English alphabet? ')
y = input('What is the second English alphabet? ')
z = input('What is third English alphabet for? ')
score = 0
if x.lower() == 'a':
    score += 1
if y.lower() == 'b':
    score += 1
if z.lower() == 'c':
    score += 1
else:
    print('You are wrong !!! ')
print('Here is your final score ', score)
