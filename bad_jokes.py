# Bad Jokes by Pedro Echavarria.

text_file = "bad_jokes.txt"
lol = "Hee hee hee!, ha ha ha!, ho ho ho!, ha ha ha!, ho ho ho!"
bad_files = open(text_file)
def bad_jokes():
    for i in bad_files:
        line = i.rstrip().split(',')
        print(input(line[0]))
        # print(line)
bad_jokes()