import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(message):
    print(f"{bcolors.HEADER}{message}{bcolors.ENDC}")


def print_okblue(message):
    print(f"{bcolors.OKBLUE}{message}{bcolors.ENDC}")


def print_okgreen(message):
    print(f"{bcolors.OKGREEN}{message}{bcolors.ENDC}")


def print_warning(message):
    print(f"{bcolors.WARNING}{message}{bcolors.ENDC}")


def print_fail(message):
    print(f"{bcolors.FAIL}{message}{bcolors.ENDC}")


def print_bold(message):
    print(f"{bcolors.BOLD}{message}{bcolors.ENDC}")


def clear_terminal():
    os.system("clear")
