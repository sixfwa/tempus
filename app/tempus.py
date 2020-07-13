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

    def show_commands(self):
        display.print_bold("\nHere are the commands you can perform:\n")
        for command in commands.commands:
            display.print_okgreen(f"-\t{command}")
        print("\n")

    def controller(self, command):
        command = command.lower()
        if command == commands.SHOW_WORKSHEETS:
            self.show_worksheets()
        elif command == commands.SHOW_COMMANDS:
            self.show_commands()
        elif command == commands.BYE:
            display.print_okblue("\n✌️\tPeace Out Homie!!!\t✌️\n")
            exit()

    def launch(self):
        self.welcome()
        while True:
            self.controller(input("command:\t"))


tempus = Tempus()

tempus.launch()
