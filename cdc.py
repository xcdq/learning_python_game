import random
Words = "python", "hello", "easy", "answer"

# print("jumble", jumble)
print("hello\n")
iscontinue = 'y'
while iscontinue == 'y':
    word = random.choice(Words)
    jumble = ''
    correct = word
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position]+word[position+1:]
    print("乱序后的单词: ", jumble)
    guess = ''
    while guess != correct:
        guess = input("猜测：")
        if guess == correct:
            print('right')
            iscontinue = input("continue(n:no / y:yes): ")
        else:
            print('not')
