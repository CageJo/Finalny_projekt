from main_screen import main_screen

#vypinanie uzivatelom a test vstupu klavesy
try:
    # spustenie_program
    main_screen()
    print()
except KeyboardInterrupt:
    print("\nProgram bol prerušený používateľom alebo prostredníctvom CTRL+C.")