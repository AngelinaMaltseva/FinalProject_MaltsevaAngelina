class Library:
    # конструктор
    def __init__(self, last_name,name, middle_name,phone_number, title_of_book, author, year_of_publication):
        # статус
        self.status = "забронирована"
        # - фамилия
        self.last_name = last_name
        # - имя
        self.name = name
        # - отчество
        self.middle_name = middle_name
        # - номер телефона
        self.phone_number = phone_number
        # - название книги
        self.title_of_book = title_of_book
        # - автор
        self.author = author
        # - год публикации
        self.year_of_publication = year_of_publication

    def __str__(self):
        return self.status + "-- " + str(self.last_name) + " " + str(self.name) + " " + str(self.middle_name) + ", номер телефона: +" + str(self.phone_number) + ", название книги: " + str(self.title_of_book) + ", автор: " + str(self.author) + ", год публикации: " + str(self.year_of_publication)
    def to_rent(self):
        self.status = "на руках"
    def cancel_rental(self):
        self.status = "в библиотеке"