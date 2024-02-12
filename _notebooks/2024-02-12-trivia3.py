import requests

def get_trivia_questions(category, amount):
    api_url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "category": category,
        "type": "multiple"
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["response_code"] == 0:
        return data["results"]
    else:
        print("Error fetching trivia questions")
        return None

def play_trivia_game(questions):
    score = 0

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        options.sort()

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ")

        if options[int(user_answer) - 1] == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['correct_answer']}")

    print(f"\nGame Over! Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("# Welcome to the Travel Trivia Game! #\n")
    category = 22  # Travel category in the Open Trivia Database
    amount = 5  # Number of questions to fetch

    trivia_questions = get_trivia_questions(category, amount)

    if trivia_questions:
        play_trivia_game(trivia_questions)
