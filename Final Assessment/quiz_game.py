# Quiz Game Program

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Gandhinagar", "D. Jaipur"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 5", "B. 8", "C. 10", "D. 15"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Over!")
print("Your Score:", score, "/", len(questions))
