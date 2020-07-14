from gspread.exceptions import WorksheetNotFound, CellNotFound
from datetime import date
import os

from connect import client
import display


class Secretary:
    """ Contains methods that will manage the Google Sheets"""

    def __init__(self):
        """
        The constructor, where the spreadsheet is selected.
        """
        self.spreadsheet = client.open("tempus")
        self.worksheet = None
        self.worksheet_name = ""
        if self.default_exists():
            file = open("default.txt", "r")
            self.select_worksheet(file.read())
            file.close()
        print(self.worksheet_name)

    def default_exists(self):
        return os.path.isfile("./default.txt")

    def create_worksheet(self, name, rows="1000", cols="27"):
        """
        Create the worksheet given the name and the number  of rows and columns.
        """
        self.spreadsheet.add_worksheet(title=name, rows=rows, cols=cols)

    def get_worksheets(self):
        return self.spreadsheet.worksheets()

    def select_worksheet(self, name):
        """
        Select the worksheet if it exists
        """
        try:
            self.worksheet = self.spreadsheet.worksheet(name)
            self.worksheet_name = name
            display.print_okgreen(f"\nWorksheet {name} selected\n")
        except WorksheetNotFound:
            display.print_fail("\nWorksheet does not exist\n")

    def set_default_worksheet(self):
        if self.worksheet_name:
            file = open("default.txt", "w")
            file.write(self.worksheet_name)
            file.close()
        else:
            display.print_fail("\nSelect a worksheet first\n")

    def worksheet_initial_setup(self):
        self.worksheet.update_cell(1, 1, "DATE")

    def get_activities(self):
        return self.worksheet.row_values(1)

    def add_activity(self, activity_name):
        """
        Add activity to the spreadsheet.
        """
        if activity_name.lower() in map(lambda x: x.lower(), self.get_activities()):
            display.print_fail("\nActivity already exists.")
        else:
            # Get the number of activities
            number_of_activities = len(self.get_activities())
            # Append to the row of activities
            self.worksheet.update_cell(
                1, number_of_activities + 1, activity_name.upper())

    def today(self):
        # create the row for today if it doesn't exist
        try:
            today = [date.today().strftime('%Y-%m-%d'), ]
            cell = self.worksheet.find(today[0])
        except CellNotFound:
            self.worksheet.append_row(today, 'USER_ENTERED')


# secretary = Secretary()
# secretary.select_work_sheet("test")
# secretary.add_activity("health")
# secretary.today()
