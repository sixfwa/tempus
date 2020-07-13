from gspread.exceptions import WorksheetNotFound, CellNotFound
from connect import client
from datetime import date


class Secretary:
    """ Contains methods that will manage the Google Sheets"""

    def __init__(self):
        # Open the Tempus spreadsheet
        self.spreadsheet = client.open("tempus")
        self.worksheet = None
        self.today_created = False

    def create_work_sheet(self, name, rows="1000", cols="27"):
        # create a worksheet
        self.spreadsheet.add_worksheet(title=name, rows=rows, cols=cols)

    def select_work_sheet(self, name):
        # select worksheet if it exists
        try:
            self.worksheet = self.spreadsheet.worksheet(name)
        except WorksheetNotFound:
            print("Worksheet does not exist")

    def add_activity(self, activity_name):
        self.worksheet.append_column(activity_name)

    def today(self):
        # create the row for today if it doesn't exist
        try:
            today = [date.today().strftime('%Y-%m-%d'), ]
            cell = self.worksheet.find(today[0])
        except CellNotFound:
            self.worksheet.append_row(today, 'USER_ENTERED')


secretary = Secretary()
secretary.select_work_sheet("test")
secretary.add_activity("Date")
