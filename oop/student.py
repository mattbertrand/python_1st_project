class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house
        # self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    # match not available with this version of Python
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦫"
    #         case "Jack Russel terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"

def main():
    student = get_student()
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student.name} from {student.house}")
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return Student(name, house)

if __name__ == "__main__":
    main()