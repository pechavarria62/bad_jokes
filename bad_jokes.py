# Bad Jokes by Pedro Echavarria.

text_file = "bad_jokes.txt"
lol = "Hee hee hee!, ha ha ha!, ho ho ho!, ha ha ha!, ho ho ho!"
bad_files = open(text_file)
def bad_jokes():
    for i in bad_files:
        line = i.rstrip().split(',')
        ask = input(line[0])
    # if the answer is not right then keep waiting for next answer 
    # after NOPE!
        if ask != line[1]:
            print('NOPE!')
    # else if the user used the 3 tries then give answer.
        # elif :
        
        # print(line)
bad_jokes()