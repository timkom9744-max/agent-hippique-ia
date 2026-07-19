class Course:

    def __init__(self):
        self.reunion = ""
        self.course = ""
        self.hippodrome = ""
        self.heure = ""
        self.distance = ""
        self.discipline = ""
        self.allocation = ""
        self.partants = []

    def afficher(self):
        return (
            f"Réunion : {self.reunion}\n"
            f"Course : {self.course}\n"
            f"Hippodrome : {self.hippodrome}\n"
            f"Heure : {self.heure}\n"
            f"Distance : {self.distance}\n"
            f"Discipline : {self.discipline}\n"
            f"Allocation : {self.allocation}\n"
            f"Nombre de partants : {len(self.partants)}"
        )
