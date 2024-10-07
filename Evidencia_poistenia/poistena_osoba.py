class PojistenaOsoba:
    def __init__(self, jmeno, prijmeni, cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = cislo
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno}  {self.prijmeni}  {self.vek}      {self.cislo}"

    def __eq__(self, other):
        return (self.jmeno == other.jmeno and self.prijmeni == other.prijmeni and
                self.cislo == other.cislo and self.vek == other.vek)

    def __hash__(self):
        return hash((self.jmeno, self.prijmeni, self.cislo, self.vek))
