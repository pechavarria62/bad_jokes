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
        while (ask := input(question)) != answer:
            pregunta += input('NOPE!')
            
            if count_answer == 3:
                print("Yes!" + lol)
            ask += 1
    # if the answer is not right then keep waiting for next answer 
    # after NOPE!
    # while ask != like[1]:
        # ask = input("'NOPE!'")
        # if ask == line[1]:
        #     print("Yes!" + lol)
            
            
            
        # elif :
        # else:
        #     print(line[1])
        #     print(lol)
        
bad_jokes()
# while (i := sys.stdin.read(1)) != '\n':
#   do_smthg(i)