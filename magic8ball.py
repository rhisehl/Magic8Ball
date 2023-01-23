import random , sys
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'



while True: #answer loop
    print('Are you ready to have your fortune read?')
    while True: #player input loop
        print('Enter your answer: (y)es (n)o (q)uit')
        answer=input()
        if answer == 'q':
            sys.exit() #quit the program
        if answer == 'y' or answer == 'n':
            break #break out of player input loop
    if answer == 'y':
        r = random.randint(1,9)
        fortune = getAnswer(r)
        print(fortune)
    elif answer == 'n':
        print('Be brave, accept your fortune')