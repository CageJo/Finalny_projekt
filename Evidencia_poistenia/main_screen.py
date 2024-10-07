from poistena_osoba import PojistenaOsoba


class UserInterface:

    def __init__(self):
        self.list_pojistenych = []

    def pridaj_zaznam(self, zaznamy, novy_zaznam):
        if novy_zaznam in zaznamy:
            print("Upozornění: Tento záznam již existuje!")
        else:
            zaznamy.append(novy_zaznam)
            print("Záznam byl úspěšně přidán.")

    def main_screen(self):
        while True:
            print("------------------------------")
            print("Evidence pojištěných")
            print("------------------------------")
            print("Vyberte si akci:")
            print("1. Přidat nového pojištěného")
            print("2. Vypsat všechny pojištěné")
            print("3. Vyhledat pojištěného")
            print("4. Konec")

            try:
                vyber = input("Zadej číslo: ")
                vyber = int(vyber)
            except ValueError:
                print("Neplatný výběr, zkuste to znovu.")
                continue
            """opravuje error, ktory vyhadzuje pri force ukonceni, presunute do main.py
            except KeyboardInterrupt:
                print("\nProgram bol prerušený používateľom alebo prostredníctvom CTRL+C.")
                break"""

            match vyber:
                case 1:
                    while True:
                        print("Zadejte jméno pojištěného")
                        jmeno = input().replace(" ", "")
                        if not jmeno:
                            print("Jméno nesmí být prázdné.")
                            continue
                        break

                    while True:
                        print("Zadejte příjmení")
                        prijmeni = input().replace(" ", "")
                        if not prijmeni:
                            print("Příjmení nesmí být prázdné.")
                            continue
                        break

                    while True:
                        print("Zadajte telefonní číslo:")
                        cislo = input().strip().replace(" ", "")

                        if not cislo.isdigit() or len(cislo) < 6:
                            print("Zadajte platné telefonní číslo.")
                            continue
                        else:
                            cislo_upravene = int(cislo)
                            break

                    while True:
                        print("Zadejte věk")
                        vek = input().replace(" ", "")
                        if not vek.isdigit() or int(vek) > 150:
                            print("Zadejte správný věk, v rozmezí <0 - 150>")
                            continue
                        else:
                            vek = int(vek)
                            break

                    nova_osoba = PojistenaOsoba(jmeno=jmeno, prijmeni=prijmeni, cislo=cislo, vek=vek)
                    self.pridaj_zaznam(self.list_pojistenych, nova_osoba)

                    print("Data byla uložena. Pokračujte klávesou ENTER…")
                    input()

                case 2:
                    print()
                    for osoba in self.list_pojistenych:
                        print(osoba)
                    input("Pokračujte klávesou ENTER")

                case 3:
                    print("Vyhledat pojištěného")
                    hledane_jmeno = input("Zadejte jméno pojištěného: ")
                    hledane_prijmeni = input("Zadejte příjmení pojištěného: ")
                    nalezeno = False
                    for osoba in self.list_pojistenych:
                        if osoba.jmeno == hledane_jmeno and osoba.prijmeni == hledane_prijmeni:
                            print(osoba)
                            nalezeno = True
                    if not nalezeno:
                        print("Pojištěný nenalezen.")


                    input("Pokračujte klávesou ENTER")

                case 4:
                    print("Konec")
                    break

