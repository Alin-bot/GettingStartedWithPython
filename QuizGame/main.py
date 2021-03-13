from Question import Question
question_prompt = [
        'What color are bananas?\na) Blue\nb) Banana\nc) Yellow\n',
        'What color are kiwis?\na) Green\nb) Brown \nc) Banana\n',
        'What color are strawberries\na) Red\nb) Green\nc) Green\n']
questions = [
    Question(question_prompt[0], 'c'),
    Question(question_prompt[1], 'b'),
    Question(question_prompt[2], 'a')]


def run_test(questions):
    print('Just type the letter of your answer!\n')
    score = 0
    for question in questions:
        answer = input(question.prompt + 'Your answer: ')
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')


run_test(questions)
