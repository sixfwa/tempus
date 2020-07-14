import os

from secretary import Secretary
import display
import commands


class Tempus:

    def __init__(self):
        self.secretary = Secretary()

    def welcome(self):
        display.clear_terminal()
        display.print_header("👋\tWELCOME TO TEMPUS\t👋\n")

    def show_worksheets(self):

        worksheets = self.secretary.get_worksheets()
        display.print_bold("\nHere are your worksheets:\n")
        for worksheet in worksheets:
            display.print_okgreen(f"-\t{worksheet.title}")
        print("\n")

    def show_activities(self):
        activities = self.secretary.get_activities()[1:]
        display.print_bold(
            f"\nActivities listed in {self.secretary.worksheet_name}:\n")
        for activity in activities:
            display.print_okgreen(f"-\t{activity}")
        print("\n")

    def show_selected_worksheet(self):
        display.print_okgreen(f"\n({self.secretary.worksheet_name})\n")

    def show_commands(self):
        display.print_bold("\nHere are the commands you can perform:\n")
        for command in commands.commands:
            display.print_okgreen(f"-\t{command}")
        print("\n")

    def set_default(self):
        self.secretary.set_default_worksheet()

    def select_worksheet(self):
        """
        User will enter the name of a worksheet to be selected
        """
        name = input("\nEnter the name of a worksheet:\t")
        self.secretary.select_worksheet(name)

    def create_worksheet(self):
        name = input("\nEnter the name of a worksheet:\t")
        self.secretary.create_worksheet(name)
        self.secretary.select_worksheet(name)
        display.print_warning("Initialising Worksheet\n")
        self.secretary.worksheet_initial_setup()

    def add_activity(self):
        if self.secretary.worksheet_name == "":
            display.print_warning("\nPlease select a worksheet!!!\n")
        else:
            activity_name = input("\nEnter name of the activity:\t")
            self.secretary.add_activity(activity_name)
        print("\n")

    def controller(self, command):
        command = command.lower()
        if command == commands.SHOW_WORKSHEETS:
            self.show_worksheets()
        elif command == commands.SHOW_COMMANDS:
            self.show_commands()
        elif command == commands.SHOW_SELECTED_WORKSHEET:
            self.show_selected_worksheet()
        elif command == commands.SHOW_ACTIVITIES:
            self.show_activities()
        elif command == commands.SELECT_WORKSHEET:
            self.select_worksheet()
        elif command == commands.CREATE_WORKSHEET:
            self.create_worksheet()
        elif command == commands.SET_DEFAULT:
            self.set_default()
        elif command == commands.ADD_ACTIVITY:
            self.add_activity()
        elif command == commands.CLEAR_SCREEN:
            display.clear_terminal()
        elif command == commands.BYE:
            display.print_okblue("\n✌️\tPeace Out Homie!!!\t✌️\n")
            exit()
        else:
            display.print_fail("\nNot a valid command\n")

    def launch(self):
        self.welcome()
        while True:
            if self.secretary.worksheet_name == "":
                self.controller(input(display.command_line()))
            else:
                self.controller(
                    input(display.command_line(self.secretary.worksheet_name)))


tempus = Tempus()

tempus.launch()
