from connect import client
from datetime import date


class Secretary:
    """ Contains methods that will manage the Google Sheets"""

    def __init__(self):
        # Open the Tempus spreadsheet
        self.spreadsheet = client.open("tempus")

    def create_work_sheet(self, name, rows, cols):
        # create a worksheet
        self.spreadsheet.add_worksheet(title=name, rows=rows, cols=cols)

    def today(self):
        # create the row for today
        today = [date.today().strftime('%Y-%m-%d'), ]
        self.spreadsheet.append_row(today, 'USER_ENTERED')


secretary = Secretary()
secretary.create_work_sheet("test", rows="1000", cols="27")
