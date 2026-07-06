from random import choice as ch
animals = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","rabbit","bear"]
countries = ["japan","canada","brazil","egypt","italy","france","mexico","spain","india","turkey"]
sports = ["football","tennis","cricket","volleyball","baseball","swimming","boxing","cycling","golf","karate"]
programming = ["python","java","kotlin","swift","golang","ruby","rust","html","css","sql"]
food = ["pizza","burger","pasta","sushi","shawarma","falafel","steak","salad","noodles","sandwich"]
movies = ["avatar","inception","gladiator","interstellar","coco","up","frozen","moana","titanic","joker"]
categories = [animals,countries,sports,programming,food,movies]
category_names = ["Animal","Countries","sport","programming","food","movie"]

def choose_word():
    place = categories.index(ch(categories))
    category = categories[place]
    word = ch(category)
    category_name = category_names[place]
    return word, category_name

def display_word(guessed_letters,word):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("-", end=" ")
    print("")

def check_allowed(letter):
    if len(letter)==1 and letter.isalpha():
        add_guessed_letter(letter)
    elif len(letter)!=1:
        print("Please enter only one letter")
    else:
        print("Please enter a letter only")

def add_guessed_letter(letter):
    global mistakes
    if letter in guessed_letters:
        print("You've already guessed this letter!!")
    else:
        guessed_letters.append(letter)
        mistakes = check_winner(letter,word,mistakes)

def draw_hangman(mistakes):
    hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]
    print(hangman[mistakes])

def check_winner(letter,word,mistakes):            
    if letter not in word:
        mistakes+=1
        draw_hangman(mistakes)
    return mistakes

mistakes = 0
word, category_name = choose_word()
print("The category is:",category_name)
guessed_letters = []
while True:
    if mistakes == 6:
        print("Game Over! 💀")
        print("The word was:"+word)
        break
    count=0
    for letter in word:
        if letter in guessed_letters:
            count+=1
    if count==len(word):
        print("Congratulations! You guessed the word! 🎉")
        break 
    display_word(guessed_letters,word)
    choice=input("Enter a letter:")
    check_allowed(choice.lower())