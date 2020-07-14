from tempus import Tempus
import display
import commands

tempus = Tempus()


def controller(command):
    command = command.lower()
    if command == commands.SHOW_WORKSHEETS:
        tempus.show_worksheets()
    elif command == commands.SHOW_COMMANDS:
        tempus.show_commands()
    elif command == commands.SHOW_SELECTED_WORKSHEET:
        tempus.show_selected_worksheet()
    elif command == commands.SHOW_ACTIVITIES:
        tempus.show_activities()
    elif command == commands.SELECT_WORKSHEET:
        tempus.select_worksheet()
    elif command == commands.CREATE_WORKSHEET:
        tempus.create_worksheet()
    elif command == commands.SET_DEFAULT:
        tempus.set_default()
    elif command == commands.ADD_ACTIVITY:
        tempus.add_activity()
    elif command == commands.CLEAR_SCREEN:
        display.clear_terminal()
    elif command == commands.BYE:
        display.print_okblue("\n✌️\tPeace Out Homie!!!\t✌️\n")
        exit()
    else:
        display.print_fail("\nNot a valid command\n")


def launch():
    tempus.welcome()
    while True:
        if tempus.secretary == "":
            controller(input(display.command_line()))
        else:
            controller(input(display.command_line(
                tempus.secretary.worksheet_name)))


launch()
