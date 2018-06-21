import string
import csv


class InvalidCharacterError(Exception):
    def __init__(self, value):
        self.exception = value

    def __str__ (self):
        return "\nThere was an error: " + self.exception + "\nInput was not letter or not lowercase\n"


class ChoiceDoesNotExistError(Exception):
    def __init__(self, value):
        self.exception = value

    def __str__ (self):
        return "\nThere was an error: Answer cannot be " + str(self.exception[0]) + "\nThere is already an answer for this question\n"


class MultipleChoiceQuestion:

    def __init__(self, question):
        self.question = question
        self.answer = None
        self.choices = []

    def printQuestion(self):
        print(str(self.question) + "\n===== ")
        for i in range(len(self.choices)):
            print( str(self.choices[i][0]) + ". " + str(self.choices[i][1]))

    def __str__(self):
        stri = "" + self.question + "\n=====\n"
        for i in range(len(self.choices)):
            stri = stri + (str(self.choices[i][0]) + ". " + str(self.choices[i][1]) + '\n')
        return stri

    def add_choice(self, letter, text):
        self.letter = letter
        self.text = text

        # try this block of code and if the input isnt a letter or uppercase,
        # raise an exception
        try:
            # there was no exception so continue
            if(self.letter.islower() and self.letter.isalpha()):
                tup = (self.letter,self.text)
                self.choices.append(tup)
            # there was an exception so raise the custom class error handling
            else:
                raise InvalidCharacterError(self.letter)
        # error was raised so we interpret it as e, and call the string method which was overridden from the invalid character error class
        # to handle it
        except InvalidCharacterError as e:
            print('{}:{}'.format(e.__class__.__name__, e))

    def set_choices(self, all_choices):
        # find the corresponding letter for the index of the array
        for i in range(len(all_choices)):
            for y in enumerate(string.ascii_lowercase, 1):
                if i+1 == y[0]:
                    letter = y[1]
                    break

            tup = (letter,all_choices[i])
            # store letter and choice as a tuple
            self.choices.append(tup)

    def set_answer(self, letter):
        # try this block and if we raise an exception jump to except block
        try:
            if self.answer != None:
                raise ChoiceDoesNotExistError(self.letter)
            # there was no error so set an answer
            else:
                for i in range(len(self.choices)):
                    if letter == self.choices[i][0]:
                        self.answer = self.choices[i]
                        break

        except ChoiceDoesNotExistError as e:
            print('{}:{}'.format(e.__class__.__name__, e))

    def is_correct_answer(self, letter):
        if letter == self.answer[0]:
            return True
        else:
            return False


class Quiz:

    def __init__(self):
        self.listOfQuestions = []


    def add_question(self, question):
        # question will be an instance of MultipleChoiceQuestion as per hw instructions
        self.listOfQuestions.append(question)


    def __str__(self):
        stri = " "
        for i in range(len(self.listOfQuestions)):
            stri = stri + (str(self.listOfQuestions[i])) + '\n'
        return stri


    def load_questions_from_file(self, file_name):

        file = file_name
        with open(file) as csvfile:
             reader = csv.DictReader(csvfile)
             # load the elements from the csv with the keys being the words
             for row in reader:
               # question will be an instance of MultipleChoiceQuestion as per hw instructions
                q1 = MultipleChoiceQuestion(row['question'])
                q1.add_choice('a',row["choice_a"])
                q1.add_choice('b',row["choice_b"])
                q1.add_choice('c',row["choice_c"])
                q1.add_choice('d',row["choice_d"])
                q1.set_answer(row["answer"])

                self.listOfQuestions.append(q1)

    def run_interactive_quiz(self):
        count = 0
        for i in range(len(self.listOfQuestions)-1):
            # print question and choices in a pretty format
            print("\n" + str(self.listOfQuestions[i].question) + "\n=====\n"+ str(self.listOfQuestions[i].choices[0][0] + ". " + self.listOfQuestions[i].choices[0][1]) + "\n" + \
                  str(self.listOfQuestions[i].choices[1][0] + ". " + self.listOfQuestions[i].choices[1][1]) + "\n" + str(self.listOfQuestions[i].choices[2][0] + \
                ". " + self.listOfQuestions[i].choices[2][1]) + "\n" + str(self.listOfQuestions[i].choices[3][0] + ". " + self.listOfQuestions[i].choices[3][1]) + "\n")
            # ask for user input
            answer = input("Choose an answer: ")
            # check to see if the answer is correct
            if(self.listOfQuestions[i].is_correct_answer(answer)):
                count = count + 1
                print("Correct!")
            else:
                print("Wrong.")
            # ask user to continue
            input('\nPress <return> to go to next question')
        # no more questions so print
        print("End of Quiz\nYou got "+ str(count) + " out of " + str(len(self.listOfQuestions)))




# adds three choices to question, q1...
# q1 = MultipleChoiceQuestion('Which type is immutable?')
# q1.add_choice('a', 'list')
# q1.add_choice('b', 'tuple')
# q1.add_choice('c', 'dict')
# print(q1)

# q1 = MultipleChoiceQuestion('Which type is immutable?')
# q1.add_choice('a', 'list')
# q1.add_choice('b', 'tuple')
# q1.add_choice('c', 'dict')
# q1.set_answer('b')

# q1 = MultipleChoiceQuestion('Which type is immutable?')
# q1.add_choice('a', 'list')
# q1.add_choice('b', 'tuple')
# q1.add_choice('c', 'dict')
# q1.set_answer('b')
# # the following will print False
# print('is a correct? ', q1.is_correct_answer('a'))
# # the following will print True
# print('is b correct? ', q1.is_correct_answer('b'))

