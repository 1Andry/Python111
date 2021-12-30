class Book:
    name = ""
    date = ""
    publisher = ""
    gener = ""
    autor = ""
    price = ""

    def print_data(self):
        print("название книги: ", self.name)
        print("дата выпуска : ", self.date)
        print("издатель: ", self.publisher)
        print("жанр: ", self.gener)
        print("автор: ", self.autor)
        print("цена: ", self.price)

    def input_book(self, name, date, publisher, gener, autor, price):
        self.name = name
        self.date = date
        self.publisher = publisher
        self.gener = gener
        self.autor = autor
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_date(self, date):
        self.date = date

    def get_date(self):
        print(self.date)

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        print(self.publisher)

    def set_gener(self, gener):
        self.gener = gener

    def get_gener(self):
        print(self.gener)

    def set_autor(self, autor):
        self.autor = autor

    def get_autor(self):
        print(self.autor)

    def set_price(self, price):
        self.price = price

    def get_price(self):
        print(self.price)


h1 = Book()
h1.input_book("Искусство программирования", "2017", "Вильямс", " no", "Дональд Э. Кнут", "")
# h1.print_data()
h1.set_price("1500")
h1.set_gener("науки и техника")
h1.print_data()