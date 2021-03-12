from Student import Question
    question_prompt = [
        'What color are bananas?\na) Blue\nb) Banana\nc) Yellow\n',
        'What color are kiwis?\na) Green\nb) Brown \nc) Banana\n',
        'What color are strawberries\na) Red\nb) Green\nc) Green\n' ]
    questions = [ Question(question_prompt[0], 'c'),
              Question(question_prompt[1], 'b'),
              Question(question_prompt[2], 'a') ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct') \
run_test(questions)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer