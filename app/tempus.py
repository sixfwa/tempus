import os

from secretary import Secretary
import display
import commands


class Tempus:

    def __init__(self):
        self.secretary = Secretary()

    def welcome(self):
        """ Displays the welcome message to the user"""
        display.clear_terminal()
        display.print_header("👋\tWELCOME TO TEMPUS\t👋\n")

    def show_worksheets(self):
        """Shows all the worksheets"""
        worksheets = self.secretary.get_worksheets()
        display.print_bold("\nHere are your worksheets:\n")
        for worksheet in worksheets:
            display.print_okgreen(f"-\t{worksheet.title}")
        print("\n")

    def show_activities(self):
        """Shows the acitivities created for the user"""
        activities = self.secretary.get_activities()[1:]
        display.print_bold(
            f"\nActivities listed in {self.secretary.worksheet_name}:\n")
        for activity in activities:
            display.print_okgreen(f"-\t{activity}")
        print("\n")

    def show_selected_worksheet(self):
        """Prints the selected workedsheet to the user"""
        display.print_okgreen(f"\n({self.secretary.worksheet_name})\n")

    def show_commands(self):
        """Lists all the commands a user can make"""
        display.print_bold("\nHere are the commands you can perform:\n")
        for command in commands.commands:
            display.print_okgreen(f"-\t{command}")
        print("\n")

    def set_default(self):
        """Sets the default worksheet"""
        self.secretary.set_default_worksheet()

    def select_worksheet(self):
        """Selects the worksheet that a user has entered"""
        name = input("\nEnter the name of a worksheet:\t")
        self.secretary.select_worksheet(name)

    def create_worksheet(self):
        """Create a worksheet"""
        name = input("\nEnter the name of a worksheet:\t")
        self.secretary.create_worksheet(name)
        self.secretary.select_worksheet(name)
        display.print_warning("\nInitialising Worksheet\n")
        self.secretary.worksheet_initial_setup()

    def add_activity(self):
        """Create an activity and add to the worksheet"""
        if self.secretary.worksheet_name == "":
            display.print_warning("\nPlease select a worksheet!!!\n")
        else:
            activity_name = input("\nEnter name of the activity:\t")
            self.secretary.add_activity(activity_name)
        print("\n")
