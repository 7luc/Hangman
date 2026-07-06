from random import choice as ch
animals = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","rabbit","bear"]
countries = ["japan","canada","brazil","egypt","italy","france","mexico","spain","india","turkey"]
sports = ["football","tennis","cricket","volleyball","baseball","swimming","boxing","cycling","golf","karate"]
programming = ["python","java","kotlin","swift","golang","ruby","rust","html","css","sql"]
food = ["pizza","burger","pasta","sushi","shawarma","falafel","steak","salad","noodles","sandwich"]
movies = ["avatar","inception","gladiator","interstellar","coco","up","frozen","moana","titanic","joker"]
categories = [animals,countries,sports,programming,food,movies]
category_names = ["Animal","countrie","sport","programming","food","movie"]
def choose_letter():
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

def choised_letter(letter):
    if letter in guessed_letters:
        print("Doublicted letter!!")
    else:
        guessed_letters.append(letter)
        display_word(guessed_letters,word)

word, category_name = choose_letter()
print("The category is:",str(category_name))
guessed_letters = []
while True:
    display_word(guessed_letters,word)
    choice=input("Enter a letter:")
    choised_letter(choice)