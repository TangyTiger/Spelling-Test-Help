import pyttsx3
import random
import time

wrong = []
engine = pyttsx3.init()


words = []
with open('spellinglist.txt') as f:
    words = f.readlines()

temp_words = words

while len(temp_words) > 0: 
    rand = random.randint(0, len(temp_words)-1)
    engine.say(temp_words[rand])
    engine.runAndWait()
    inputed = input("Spell: ").lower()+"\n"
    if inputed != temp_words[rand]:
        print("Incorrect")
        wrong.append(temp_words[rand])
    temp_words.pop(rand)


if len(wrong) == 0:
    print("None wrong!")
    time.sleep(10)
else:
    print("Wrong: ", wrong)
    time.sleep(10)