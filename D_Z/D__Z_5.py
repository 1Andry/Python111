class Student:
    def __init__(self, name):
        self.name = name
        self.computer = self.Computer()

    def print_info(self):
        print(self.name, "=>", self.computer.model, self.computer.gpu, self.computer.ram)

    class Computer:
        def __init__(self):
            self.model = "HP"
            self.gpu = "i7"
            self.ram = "16"


name1 = Student("Roman")
name2 = Student("Vladimir")
name1.print_info()
name2.print_info()
