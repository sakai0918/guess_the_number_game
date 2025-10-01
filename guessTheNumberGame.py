import sys, random

numTrial = 4
numTrialstr = str(numTrial)
number01=''
number02=''

while True:
    print('Enter a number.')
    number01 = sys.stdin.buffer.readline()
    print('Enter a number that is larger than the one you entered.')
    number02 = sys.stdin.buffer.readline()
    if number01 <= number02:
        break
    print('The second number you enter must be greater than or equal to the first number you entered.')

number01str = number01.decode().replace('\n', '')
number02str = number02.decode().replace('\n', '')

answerNum = random.randint(int(number01str), int(number02str))
#print(answerNum)
print('Guess the randomly generated number between ' + number01str + ' and ' + number02str + ' in '+ numTrialstr + ' times.')

while True:
    guessNum = sys.stdin.buffer.readline()

    if int(guessNum.decode()) == answerNum:
        break

    numTrial = numTrial - 1
    if numTrial < 1:
        break
    numTrialstr = str(numTrial)

    print('Wrong...')
    print( numTrialstr + ' times remaining.')

if numTrial < 1:
    print('Game over. You cannot attempt this challenge any further.')
else:
    print('Correct answer!')
