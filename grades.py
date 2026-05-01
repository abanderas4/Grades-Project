import csv
from PyQt6.QtWidgets import *
from gui import *
import os

class Grades(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """method that initializes the UI and
        creates csv file if csv file doesn't exist"""
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)

        self.hidden()

        self.Enter_button.clicked.connect(lambda: self.enter())
        self.submit_button.clicked.connect(lambda: self.submit())

        if not os.path.isfile('grades.csv'):
            with open('grades.csv', 'w', newline= '') as grades_file:
                writer = csv.writer(grades_file)
                writer.writerow(["Name", "Score1", "Score2", "Score3", "Score4", 'Final'])


    def hidden(self) -> None:
        """method that hides score labels, input boxes, and clears text
        inside input boxes"""
        self.Score_1.hide()
        self.Score1_input.hide()
        self.Score1_input.clear()

        self.Score_2.hide()
        self.Score2_input.hide()
        self.Score2_input.clear()

        self.Score_3.hide()
        self.Score3_input.hide()
        self.Score3_input.clear()

        self.Score_4.hide()
        self.Score4_input.hide()
        self.Score4_input.clear()

        self.submit_button.hide()

    def submit(self) -> None:
        """method that validates and appends data to csv file"""
        with open('grades.csv', 'a', newline= '') as grades_file:
            writer = csv.writer(grades_file)

            store_values = []

            scores = [self.Score1_input, self.Score2_input, self.Score3_input, self.Score4_input]

            try:
                for score in scores:
                    if score.isVisible():
                        text = score.text().strip()
                        if text == '':
                            raise ValueError
                        value = int(text)
                        if not (0 <= value <= 100):
                            raise ValueError

                        store_values.append(value)

                    else:
                        store_values.append(0)

            except ValueError:
                self.Message.setText("Enter a valid input (1-100)")
                return

            student_name = self.input_name.text()

            final_score = max(store_values)

            writer.writerow([student_name] + store_values + [final_score])

            self.Message.setText('Successfully submitted scores')
            self.input_name.clear()
            self.input_attempt.clear()

            self.hidden()

    def enter(self) -> None:
        """method that validates student name, number of attempts, and shows
         corresponding input boxes for the number of attempts"""
        self.hidden()

        if self.Message != "":
            self.Message.setText('')

        try:
            student_name = self.input_name.text().strip()
            number_of_attempts = int(self.input_attempt.text().strip())

            if not student_name.isalpha():
                raise ValueError

            if not (0 <= number_of_attempts <= 4):
                raise ValueError


            if number_of_attempts >= 1:
                self.Score_1.show()
                self.Score1_input.show()


            if number_of_attempts >=2:
                self.Score_2.show()
                self.Score2_input.show()


            if number_of_attempts >=3:
                self.Score_3.show()
                self.Score3_input.show()

            if number_of_attempts == 4:
                self.Score_4.show()
                self.Score4_input.show()


            self.submit_button.show()


        except ValueError:
            self.Message.setText("Enter a valid input")


