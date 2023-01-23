import random, sys

messages = ['It is certain',
    'It is decidedly so',
    'Yes, definitely',
    'Reply hazy, try again'
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
while True:
    print('Do you want your fortune read? (y)es (n)o (q)uit')
    answer = input()
    if answer == 'y':
        print(messages[random.randint(0,len(messages)-1)])
    elif answer == 'n':
        print('aww too bad')
    elif answer == 'q':
        sys.exit()