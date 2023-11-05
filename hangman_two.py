import random
hangman_words = open("C:\\Users\\Krith\\Desktop\\files_testing\\hangman.txt", "r")
remaining_chances = 6
hangman_words_list = []
word = []
temp_word = []
for i in hangman_words:
    hangman_words_list.append(i.rstrip('\n'))
chosen_word = random.choice(hangman_words_list)
#inserting the words in the file to the list
for y in chosen_word:
    temp_word.append(y)
#getting the chosen word
word.append(chosen_word[0])
for w in range(1, len(chosen_word)):
    word.append("__")
def draw_hangman():
    print("--------------", end = " ")
    for i in range(0, 7):
        print("|\n")
def draw_stickman(var):
        draw_hangman()
        if(var == 5):
            print("O")
        elif(var == 4):
            print("O")
            print("/")
        elif(var == 3):
            print("O")
            print("/\\")
        elif(var == 2):
            print("O")
            print("/\\")
            print(" |")
        elif(var == 1):
                print("O")
                print("/\\")
                print("|")
                print("/")
        elif(var == 0):
            print("O")
            print("/\\")
            print("|")
            print("/\\")
win=0 
match=0
draw_stickman(remaining_chances)
while(remaining_chances >= 1 and win == 0):
    print(word)
    letter = input("Guess the letter:") 
    match=0
    #checking if the letter matches with any of the chosen word letters
    for y in range(0, len(chosen_word)):
        if(letter == chosen_word[y] and word[y] == "__"):
            word[y] = chosen_word[y]
            match=1
    if(match != 1):
        remaining_chances = remaining_chances - 1
        draw_stickman(remaining_chances)
    if(word == temp_word):
        win=1
        print("You won")  
        
    
if(win == 0):
    print("You lost")
    
print("The correct word was:", chosen_word)