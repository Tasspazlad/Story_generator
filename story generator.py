import random
from time import sleep

mainChar = input("Main character: ")
rivalName = input("Rival's name: ")
activity = input("Daily activity (e.g. watching TV): ")
posAdj  = input("Positive adjective (e.g. funny,happy) : ")
negAdj  = input("Negative adjective (e.g. Careless,Dishonest) : ")

word1 = ['question','code','comment']
word2 = ['penguins','programmer jokes','text generation','another amazing fireworks','finding your partner']
word3 = ['C#','C++','Python','Javascript','Java','code']
word4 = ['liked','disliked','reported','deleted']

Sentance = [
    'Yesterday, while browsing ChekToLearn and ', 'activity', ', ', 'mainChar', ' noticed that ',
    'rivalName', ' posted a new ', 'word1', ' about ', 'word2', '. He ', 'word4', 'it and challenged him to a ',
    'word3', ' battle.  Then he posted his own ', 'posAdj', ' ', 'word1', ', but ', 'rivalName', ' retaliate with his', 'negAdj', ' comment about', 'word2', '.',
    
]
#item is the item of the list

for item in Sentance:
    if item == "activity" : Sentance[Sentance.index(item)] = activity # index -> list[index] = val
    elif item == "mainChar" : Sentance[Sentance.index(item)] = mainChar
    elif item == "rivalName" : Sentance[Sentance.index(item)] = rivalName
    elif item == "posAdj" : Sentance[Sentance.index(item)] = posAdj
    elif item == "negAdj" : Sentance[Sentance.index(item)] = negAdj

    elif item == "word1" : 
        index = Sentance.index(item)
        Sentance[ index ] = random.choice(word1)

    elif item == "word2" : Sentance[Sentance.index(item)] = random.choice(word2)
    elif item == "word3" : Sentance[Sentance.index(item)] = random.choice(word3)
    elif item == "word4" : Sentance[Sentance.index(item)] = random.choice(word4)

    else:continue

#Story
story = " ".join(item for item in Sentance)
sleep(1)
print("\nStory is generating\n")
sleep(1)
print(story)