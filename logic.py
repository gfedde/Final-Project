from PyQt6.QtWidgets import *
from vote_gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Method to set default of values of Logic object

        self.felicia_votes = Number of votes for Felicia
        self.edward_votes = Number of votes for Edward
        self.bianca_votes = Number of votes for Bianca
        """
        super().__init__()
        self.setupUi(self)
        self.submit_push.clicked.connect(self.submit)
        self.result_push.clicked.connect(self.result)
        self.id_collection = {}

        self.felicia_votes = 0
        self.edward_votes = 0
        self.bianca_votes = 0

    def submit(self) -> None:
        """
        Method to create submit button logic and store voters in file
        :return: none
        """
        try:
            id_num = self.id_input.text()
            id_num = int(id_num)
            vote_error_text = (
            f"Must use different id in order to vote again"
            )
            vote_success_text = (
                f"Vote counted"
            )
            vote = ''

            if self.felicia_radio.isChecked():
                vote = 'Felicia'
            if self.bianca_radio.isChecked():
                vote = 'Bianca'
            if self.edward_radio.isChecked():
                vote = 'Edward'
            self.output_text_label.setText(vote_success_text)

            if id_num in self.id_collection:
                self.output_text_label.setText(vote_error_text)
            else:
                if self.felicia_radio.isChecked():
                    self.felicia_votes += 1
                    self.id_collection[id_num] = vote
                elif self.edward_radio.isChecked():
                    self.edward_votes += 1
                    self.id_collection[id_num] = vote
                elif self.bianca_radio.isChecked():
                    self.bianca_votes += 1
                    self.id_collection[id_num] = vote
                else:
                    radio_error_text = (
                        f"Please select a candidate"
                    )
                    self.output_text_label.setText(radio_error_text)

                header = 'ID - Vote'
                with open('vote.csv', 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([header])
                    for id_num, vote in self.id_collection.items():
                        csvwriter.writerow([f"{id_num} - {vote}"])

        except ValueError:
            error_text = (
                "ID must be a series of integers"
            )
            self.output_text_label.setText(error_text)

    def result(self) -> None:
        """
        Method to display results of the election
        :return: None
        """
        winner = ''
        if self.felicia_votes > 0 or self.edward_votes > 0 or self.bianca_votes > 0:
            if self.felicia_votes > self.edward_votes and self.felicia_votes > self.bianca_votes:
                winner = 'Winner is Felicia'
            elif self.edward_votes > self.felicia_votes and self.edward_votes > self.bianca_votes:
                winner = 'Winner is Edward'
            elif self.bianca_votes > self.felicia_votes and self.bianca_votes > self.edward_votes:
                winner = 'Winner is Bianca'
            elif self.bianca_votes == self.felicia_votes or self.bianca_votes == self.edward_votes or self.felicia_votes == self.edward_votes:
                winner = 'Tie'
            self.output_text_label.setText(winner)
        else:
            radio_error_text = (
                f"Please select a candidate"
            )
            self.output_text_label.setText(radio_error_text)




