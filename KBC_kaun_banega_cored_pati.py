# 🎯 Kaun Banega Crorepati - Quiz Game
# 📝 Developed by Om Nagnath Kale

# Welcome Message
print("🪙 Welcome to Kaun Banega Crorepati!")
print("💡 Test your knowledge and win virtual prize money!")
print("⚠️ One wrong answer, and the game ends. Let's begin!\n")

# Questions List
questions = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "A) HyperText Machine Language",
            "B) Hyper Transfer Markup Language",
            "C) HyperText Markup Language",
            "D) HighText Mark Language"
        ],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) define", "C) def", "D) func"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A) Tuple", "B) List", "C) String", "D) Integer"],
        "answer": "B"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    },
    {
        "question": "Which tag is used to create a hyperlink in HTML?",
        "options": ["A) <a>", "B) <link>", "C) <href>", "D) <hyper>"],
        "answer": "A"
    },
    {
        "question": "Which of these is a Python library for data analysis?",
        "options": ["A) NumPy", "B) Pandas", "C) TensorFlow", "D) All of the above"],
        "answer": "D"
    },
    {
        "question": "What is the full form of CSS?",
        "options": [
            "A) Color Style Sheet",
            "B) Cascading Style Sheets",
            "C) Creative Style Script",
            "D) Custom Style Sheets"
        ],
        "answer": "B"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["A) //", "B) <!--", "C) #", "D) /*"],
        "answer": "C"
    },
    {
        "question": "Which loop is used when the number of iterations is unknown?",
        "options": ["A) for", "B) while", "C) do-while", "D) repeat-until"],
        "answer": "B"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"],
        "answer": "C"
    }
]

# Prize Money for each question
prize_money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 1000000]

# Game Logic
score = 0
for i in range(len(questions)):
    q = questions[i]
    print(f"\n💭 Question {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("👉 Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct Answer!")
        score += prize_money[i]
        print(f"💰 You have won: ₹{score}")
    else:
        print("❌ Wrong Answer!")
        print(f"📉 You lose ₹{prize_money[i]}. Game Over!")
        break

# Final Score
print("\n🏆 Your final score is:", score)
print("🎉 Thanks for playing Kaun Banega Crorepati!")
