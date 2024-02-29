import random
import art
import people
print(art.logo)

gameStatus = ''
objectOneIndex = people.peopleList[random.randint(0, 100)]
objectOne = people.peopleDict[objectOneIndex]
streakCount = 0


while gameStatus != 'lose':
    objectTwoIndex = random.choice(people.peopleList)
    while objectTwoIndex == objectOneIndex:  # Ensure the second index is different from the first
        objectTwoIndex = random.choice(people.peopleList)
    print(f"{objectOneIndex} has a net worth of {objectOne}")
    print(art.vs)
    objectTwo = people.peopleDict[objectTwoIndex]
    userGuess = input(f"{objectTwoIndex}'s net worth is \nhigher \nor \nlower? (Type 'quit' to exit): ").lower()    
    if userGuess == 'quit':
        break
    if (objectTwo > objectOne and userGuess == 'higher') or (objectTwo < objectOne and userGuess == 'lower'):
        print(f"Correct! {objectTwoIndex} has a net worth of ${objectTwo}")
        objectOneIndex = objectTwoIndex
        objectOne = objectTwo
        streakCount += 1
        print(f"Your current streak: {streakCount}")
    else:
        print(f"Incorrect! {objectTwoIndex} has a net worth of ${objectTwo}")
        gameStatus = 'lose'