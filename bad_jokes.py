# Bad Jokes by Pedro Echavarria.

text_file = "bad_jokes.txt"
lol = "Hee hee hee!, ha ha ha!, ho ho ho!, ha ha ha!, ho ho ho!"
bad_files = open(text_file)
def bad_jokes():
    for i in bad_files:
        line = i.rstrip().split(',')
        question = line[0]
        answer = line[1].strip()
        # print(question)
        # print()
        # print(answer)
        count = 0
        while count <=3:
            ask = input(question).upper()
            while ask != answer and count <= 3:
                print('NOPE!')
                pregunta = input('Try again! or Quit ').upper()
            if ask == answer:
                print('Yes!!',lol)
            else:
                print(answer)
                print(lol)
        count +=1
bad_jokes()
# while (i := sys.stdin.read(1)) != '\n':
#   do_smthg(i)
# while (ask := input(question).upper()) != answer: