from python26 import Question

question_prompts = [
    "What colour are apples? \n (a) Red/Green\n(b) Purple\n (c) Orange",
    "What colour are Bananas? \n (a) Yellow/Green\n(b) Purple\n (c) Orange",
    "What colour are strawberries? \n (a) Purple\n(b) Red\n (c) Orange"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " answers correct")

run_test(questions)