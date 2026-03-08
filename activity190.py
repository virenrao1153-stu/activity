import requests

url = "http://opentdb.com/api.php?amount=5&type=multiple"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        questions = data["results"]

        for i, q in enumerate(questions, start=1):
            print("Question", i)
            print("Category:", q["category"])
            print("Question:", q["question"])

            print("Options:")
            for option in q["incorrect_answers"]:
                print(" -", option)

            print(" -", q["correct_answer"], "(Correct Answer)")
            print("-" * 40)

        else:
            print("Failedc to frtch trivia questions")
except Exception as e:
    print("Error:", e)