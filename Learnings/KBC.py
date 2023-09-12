"""
Create a program capable of displaying questions to the user like KBC.
Use list datatype to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
"""

questions = ["When was Chandrayaan 3 launched?", "How much is the depth of kola superdeep borehole?",
             "Which one of these is the moon of mars?", "Titan is the moon of which planet?",
             "Which is the tallest statue in the world?", "Which is the biggest country in America?",
             "Which is the fastest object ever made by humans?", "Which is the brightest object in the universe?",
             "Which is the most costliest object ever made by humans?",
             "Which company made the world's first quantum computer?", "How many days is equals to 1 lunar day?",
             "Which is the most strongest material ever found?", "Which is the most powerful nuclear bomb ever made?",
             "Which is the most powerful bomb?", "Which company made the world's first mobile?",
             "When was apollo 11 launched?"]

answers = [
    "14 july,2023\n12 july,2023\n15 july,2023\n16 july,2023",
    "11,112 meters\n11,034 meters\n12,110 meters\n12,262 meters",
    "Ceres\nPhobos\nEuropa\nGanymede",
    "Jupiter\nUranus\nSaturn\nNeptune",
    "Statue of Liberty\nStatue of unity\nStatue of Peace\nStatue of Love",
    "Canada\nUnited States\nBrazil\nMexico",
    "Voyager 1\nNew Horizons\nCassini\nParker solar probe",
    "Quasar\nPulsar\nUY scuti\nNeutron star",
    "New Horizons\nPioneer 10\nInternational Space Station\nJames web space telescope",
    "Apple\nGoogle\nSamsung\nAmazon",
    "12 days\n13 days\n14 days\n15 days",
    "Graphene\nCarbon fibre\nDiamond\nUranium",
    "MK-17\nTsar bomba\nW-59\nBTV",
    "Atom bomb\nNuclear bomb\nHydrogen bomb\nAtomic bomb",
    "Samsung\nMotorola\nHuawei\nApple",
    "16 july,1969\n17 july,1969\n18 july,1969\n19 july,1969"
]

prizes = ["1,000", "2,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000", "3,20,000",
          "6,40,000", "12,50,000", "25,00,000", "50,00,000", "10,000,000", "20,000,000", "70,000,000"]

options = [1, 4, 2, 3, 2, 1, 4, 1, 3, 2, 3, 1, 2, 3, 2, 1]

score = 0

i = 0
while i < len(questions):
    print(questions[i])
    print(answers[i])
    a = int(input("Enter option no."))
    if options[i] == a:
        print("Correct\n")
        score += 1
    else:
        print("Incorrect! Game Over")
        break

    i += 1

if score == 0:
    print("Your total prize is: 0")
else:
    print("Your total prize is: ", prizes[score-1])
