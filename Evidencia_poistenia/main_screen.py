from class_Poistena_Osoba import PoistenaOsoba

list_pojistenych = []

def pridaj_zaznam(zaznamy, novy_zaznam):
    if novy_zaznam in zaznamy:
        print("Upozornenie: Tento záznam už existuje!")
    else:
        zaznamy.append(novy_zaznam)
        print("Záznam bol úspešne pridaný.")

#class UserInterface:
def main_screen():
    while True:
        print("------------------------------")
        print("Evidence pojistenych")
        print("------------------------------")
        print("Vyberte si akci:")
        print("1. Pridat nového pojisteného")
        print("2. Vypsat vsechny pojistené")
        print("3. Vyhledat pojisteného")
        print("4. Konec")

        try:
            vyber = input("Zadaj číslo: ")
            vyber = int(vyber)
        except ValueError:
            print("Neplatný výběr, zkuste to znovu.")
            continue
        """presunute do main.py
        except KeyboardInterrupt:
            print("\nProgram bol prerušený používateľom alebo prostredníctvom CTRL+C.")
            break"""

        match vyber:
            case 1:
                while True:
                    print("Zadajte jméno pojištěného")
                    jmeno = input().replace(" ", "")
                    if not jmeno:
                        print("Jméno nesmí být prázdné.")
                        continue
                    break

                while True:
                    print("Zadajte príjmení")
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
                    print("Zadajte vek")
                    vek = input().replace(" ", "")
                    if not vek.isdigit() or int(vek) > 150:
                        print("Zadaj správny vek, v rozpätí <0 - 150>.")
                        continue
                    else:
                        vek = int(vek)
                        break

                nova_osoba = PoistenaOsoba(jmeno=jmeno, prijmeni=prijmeni, cislo=cislo, vek=vek)
                pridaj_zaznam(list_pojistenych, nova_osoba)

                print("Data byla ulozena. Pokracujte klavesou ENTER...")
                input()

            case 2:
                print()
                for osoba in list_pojistenych:
                    print(osoba)
                input("Pokračujte klávesou ENTER")

            case 3:
                print("Vyhledat pojisteného")
                hledane_jmeno = input("Zadajte jméno pojisteného: ")
                hledane_prijmeni = input("Zadajte prijmeni: ")
                nalezeno = False
                for osoba in list_pojistenych:
                    if osoba.jmeno == hledane_jmeno and osoba.prijmeni == hledane_prijmeni:
                        print(osoba)
                        nalezeno = True
                if not nalezeno:
                    print("Pojistený nenalezen.")


                input("Pokračujte klávesou ENTER")

            case 4:
                print("Konec")
                break

