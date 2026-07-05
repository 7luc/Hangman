from random import choice as ch
animal = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","rabbit","bear"]
countrie = ["japan","canada","brazil","egypt","italy","france","mexico","spain","india","turkey"]
sport = ["football","tennis","cricket","volleyball","baseball","swimming","boxing","cycling","golf","karate"]
programming = ["python","java","kotlin","swift","golang","ruby","rust","html","css","sql"]
food = ["pizza","burger","pasta","sushi","shawarma","falafel","steak","salad","noodles","sandwich"]
movie = ["avatar","inception","gladiator","interstellar","coco","up","frozen","moana","titanic","joker"]
categories = [animal,countrie,sport,programming,food,movie]
categoriesName = ["Animal","countrie","sport","programming","food","movie"]
def word_choice():
    place = categories.index(ch(categories))
    categorie = categories[place]
    word = ch(categorie)
    print("Your Categorie is:"+str(categoriesName[place]))
    print(word)

word_choice()
