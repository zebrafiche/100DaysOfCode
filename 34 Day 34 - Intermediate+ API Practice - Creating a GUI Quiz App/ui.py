from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # How do we get the same Quizbrain instance that we created in our main.py?
    # Otherwise if we create another instance of Quizbrain here the questions might be different
    # You do it like this, in main.py -
    # quiz = QuizBrain(question_bank)
    # quiz_ui = QuizInterface(quiz)
    # So now the quiz_ui object has the same QuizBrain instance created in main.py
    # So this now means that the QuizInterface now takes a QuizBrain object as an argument

    # though we have passed in quiz_brain as an argument, QuizInterface still doesn't know what quiz_brain is
    # so to let it know we have to import QuizBrain
    # and then when we declare that quiz_brain is a QuizBrain object
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Todo 1 - Create the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=50, pady=50)

        # Todo 2 - Create the canvas
        # Todo 2a - Import the text box photo
        # text_box = PhotoImage(file=)
        # Todo 2b - Use the photo as your text box
        self.canvas = Canvas(width=300, height=400)
        # canvas.create_image(200, 200, image=text_box)
        self.canvas.grid(column=1, row=1, columnspan=2)
        # Todo 3 - Put the(or any) text inside the canvas
        # to let the entire question fit into the canvas, set the width of the text a bit lower than the canvas width
        self.question_text = self.canvas.create_text(160, 200, text="Hello", width=280, font=('Courier', 15, 'bold'))

        # Todo 4 - Create the buttons
        # Todo 4a - True Button
        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0)
        self.true_button.config(command=self.input_true)
        self.true_button.grid(column=1, row=2)
        # Todo 4b - False Button
        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0)
        self.false_button.config(command=self.input_false)
        self.false_button.grid(column=2, row=2)

        # Todo 5 - Create the scoreboard
        self.user_answer = None
        self.score_label = Label(text=f'Score: {self.quiz.score}', font=('Courier', 15, 'bold'))
        self.score_label.grid(column=1, row=0, columnspan=2)

        self.get_next_question()

        self.window.mainloop()

    # Todo 8 - Method to get the next question
    # How do we get the same Quizbrain instance that we created in our main.py?
    # Otherwise if we create another instance of Quizbrain here the questions might be different
    # You do it like this, in main.py -
    # quiz = QuizBrain(question_bank)
    # quiz_ui = QuizInterface(quiz)
    # So now the quiz_ui object has the same QuizBrain instance created in main.py
    # So this now means that the QuizInterface now takes a QuizBrain object as an argument

    def get_next_question(self):
        # canvas should turn back to white irrespective of questions left or not
        self.canvas.config(bg='White')
        if self.quiz.still_has_questions():
            # Todo 7 - Create the scoreboard function
            self.score_label.config(text=f'Score: {self.quiz.score}')
            new_question_text = self.quiz.next_question()
            # as you type this line above, nothing shows up
            # bcz tho we have passed in quiz_brain as an argument, QuizInterface still doesn't know what quiz_brain is
            # so to let it know we have to import QuizBrain
            # and then when we declare that quiz_brain is a QuizBrain object
            self.canvas.itemconfig(self.question_text, text=new_question_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz')
            # once we run out of questions, disable the buttons
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    # Todo 6 - Create the button functions

    def input_true(self):
        self.user_answer = 'True'
        is_right = self.quiz.check_answer(self.user_answer)
        print(self.quiz.score)
        self.give_feedback(is_right)
        # when the user presses a button the next question should generate

    def input_false(self):
        self.user_answer = 'False'
        is_right = self.quiz.check_answer(self.user_answer)
        print(self.quiz.score)
        self.give_feedback(is_right)
        # when the user presses a button the next question should generate

    # Todo 8 - Give the user some feedback in the canvas
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question)





