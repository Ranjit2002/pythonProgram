class KBCGame:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.prize_money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000,
                            5000000, 10000000]
        self.current_question = 0
        self.current_prize = 0
        self.is_game_over = False

    def display_question(self):
        print(f"Question {self.current_question + 1}: {self.questions[self.current_question]}")
        for i, option in enumerate(self.answers[self.current_question]):
            print(f"{i + 1}. {option}")

    def check_answer(self, choice):
        correct_answer = self.answers[self.current_question]
        if choice == correct_answer[1]:
            print("Correct!\n")
            self.current_prize = self.prize_money[self.current_question]
            self.current_question += 1
            if self.current_question == len(self.questions):
                self.is_game_over = True
                print("Congratulations! You've won 10,000,000!")
            else:
                self.display_question()
        else:
            print("Incorrect! Game Over.")
            self.is_game_over = True

    def start(self):
        print("Welcome to KBC!")
        self.display_question()

        while not self.is_game_over:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    self.check_answer(choice)
                else:
                    print("Invalid choice. Please choose between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Modify the answers to include options as a list of strings for each question
answers = [
    ["14 july,2023", "12 july,2023", "15 july,2023", "16 july,2023"],
    ["12,262 meters", "10,000 meters", "14,000 meters", "8,000 meters"],
    ["Phobos", "Deimos", "Europa", "Ganymede"],
    ["Saturn", "Jupiter", "Uranus", "Neptune"],
    ["Statue of unity", "Statue of Liberty", "Statue of Peace", "Statue of Love"],
    ["Canada", "United States", "Brazil", "Mexico"],
    ["Parker solar probe", "Voyager 1", "New Horizons", "ISS"]
]

kbc = KBCGame(questions, answers)
kbc.start()
