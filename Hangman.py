from random import choice as ch
animals = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","rabbit","bear"]
countries = ["japan","canada","brazil","egypt","italy","france","mexico","spain","india","turkey"]
sports = ["football","tennis","cricket","volleyball","baseball","swimming","boxing","cycling","golf","karate"]
programming = ["python","java","kotlin","swift","golang","ruby","rust","html","css","sql"]
food = ["pizza","burger","pasta","sushi","shawarma","falafel","steak","salad","noodles","sandwich"]
movies = ["avatar","inception","gladiator","interstellar","coco","up","frozen","moana","titanic","joker"]
categories = [animals,countries,sports,programming,food,movies]
categoriesName = ["Animal","countrie","sport","programming","food","movie"]
def word_choice():
    place = categories.index(ch(categories))
    category = categories[place]
    word = ch(category)
    print("Your Categorie is:"+str(categoriesName[place]))

def display_word(guessedLetters,word):
    for letter in word:
        if letter in guessedLetters:
            print(letter, end=" ")
        else:
            print("-", end=" ")
    print("")