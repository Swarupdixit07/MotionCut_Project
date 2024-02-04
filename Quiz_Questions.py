class Quiz:
    """quiz question with multiple-choice answers."""
    
    def __init__(self, question, options, correctAns):
        self.question = question
        self.options = options
        self.correctAns = correctAns

    def ask_question(self):
        """Asks the question and returns True if the user's answer is correct, False otherwise."""
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        
        user_answer = 0
        while user_answer not in range(1, len(self.options) + 1):
            try:
                user_input = input("Enter your answer (1, 2, 3, etc.): ")
                user_answer = int(user_input)
                if user_answer not in range(1, len(self.options) + 1):
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return self.options[user_answer - 1] == self.correctAns


def run_quiz(questions):
    """Runs the quiz with a list of Quiz objects."""
    score = 0
    for question in questions:
        if question.ask_question():
            print("Correct Answer!")
            score += 1
        else:
            print(f"False! The correct answer is '{question.correctAns}'.")

        print()

    print(f"Quiz completed! Your final score is: {score}/{len(questions)}")


# Questions of the quiz
questions = [
    Quiz("Who is prime minister of india?", ["Narendra Modi", "Rahul Gandi", "Amit Shah", "Kejriwal"], "Narendra Modi"),
    Quiz("Which is the capital of india?", ["Mumbai", "Banglore", "Hariyana", "Delhi"], "Delhi"),
    Quiz("How many days in a leap year?", ["365", "364", "366", "367"], "366")
]


run_quiz(questions)
