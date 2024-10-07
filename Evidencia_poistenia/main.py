from main_screen import UserInterface

try:
    # spustenie_programu - metoda
    program = UserInterface()
    program.main_screen()
    print()

#vypinanie uzivatelom a test vstupu klavesy
except KeyboardInterrupt:
    print("\nProgram bol prerušený používateľom alebo prostredníctvom CTRL+C.")