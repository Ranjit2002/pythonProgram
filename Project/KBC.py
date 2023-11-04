class Crorepati:
    def __init__(self):
        self.first = 10000
        self.second = 320000

    def Questions(self):
        global questions
        questions = [
            ["When was Chandrayaan 3 launched?", "14 july,2023", "12 july,2023", "15 july,2023", "16 july,2023", 1],
            ["How much is the depth of kola superdeep borehole?", "11,112 meters", "11,034 meters", "12,110 meters",
             "12,262 meters", 4],
            ["Which one of these is the moon of mars?", "Ceres", "Titan", "Phobos", "Europa", 3],
            ["Titan is the moon of which planet?", "Neptune", "Jupiter", "Uranus", "Saturn", 4],
            ["Which is the tallest statue in the world?", "Statue of unity", "Statue of buddha", "Statue of liberty",
             "Statue of redeemer", 1],
            ["Which is the biggest country in the North American continent?", "USA", "Mexico", "Canada", "Cuba", 3],
            ["Which is the fastest object ever made by humans?", "Parker solar probe", "Voyager 1", "New Horizons",
             "Cassini probe", 1],
            ["Which is the brightest object in the universe?", "Pulsar", "UY scuti", "Neutron star", "Quasar", 4],
            ["Which is the most expensive thing ever made by humans?", "Pioneer 10", "International space station",
             "horizons", "James web space telescope", 2],
            ["Which company made the world's first quantum computer?", "Amazon", "Apple", "Google", "Samsung", 3],
            ["How many days is equals to 1 lunar day?", "14 days", "15 days", "16 days", "17 days", 1],
            ["Which is the most strongest material ever found?", "Graphene", "Carbon fibre", "Diamond", "Osmium", 1],
            ["Which is the most powerful nuclear bomb ever made?", "MK-17", "W-59", "Tsar bomba", "BTV", 3],
            ["Which company made the world's first mobile phone?", "Samsung", "Motorola", "Huawei", "Nokia", 2],
            ["Who invented computer?", "Nikola tesla", "Micheal faraday", "Edwin hubble", "Charles babbage", 4],
            ["Which countries have more trees?", "Russia", "America", "China", "Brazil", 1]]

    def prize_levels(self):
        global prizes
        prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
                  10000000, 70000000]

    def check(self):
        for i in range(len(questions)):
            try:
                print(f"{i + 1}. Question for Rs.{prizes[i]} is:")
                print(questions[i][0])
                k = 1
                for j in questions[i][1:-1]:
                    print(f"{k}. {j}")
                    k += 1
                print(f"5. Exit")
                choice = int(input("Enter your choice:- "))
                if i == 15:
                    if choice == questions[i][-1]:
                        print(f"Congratulations! You won Rs.{prizes[-1]}")
                elif choice == questions[i][-1]:
                    print(f"You won Rs.{prizes[i]}")
                elif choice == 5:
                    print(f"You won Rs.{prizes[i-1]}")
                    break
                else:
                    if 0 <= i <= 5:
                        print("Wrong answer\nYou won Rs.0")
                        break
                    elif 5 < i <= 10:
                        print(f"Wrong answer\nYou won Rs.{self.first}")
                        break
                    else:
                        print(f"Wrong answer\nYou won Rs.{self.second}")
                        break
                print()
            except Exception as e:
                print(type(e))
                print(e, "\n")


a = Crorepati()
a.Questions()
a.prize_levels()
a.check()
