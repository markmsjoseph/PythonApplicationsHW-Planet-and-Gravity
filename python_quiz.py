
from quizzical import Quiz
from quizzical import MultipleChoiceQuestion


quiz = Quiz()# create quiz object

questions = quiz.load_questions_from_file("questions.csv")
quiz.add_question(questions)
quiz.run_interactive_quiz()