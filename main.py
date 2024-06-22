from tkinter import *
from Library.library import Library
# Приложение обладает следующим функционалом:
# -посмотреть список книг;
# -регистрация и авторизация читателя
#- забронировать книгу
def register_reader():
    # для считывания данных из поля ввода
    # используется метод get()
    last_name = entry_last_name.get()
    name = entry_name.get()
    middle_name = entry_middle_name.get()
    phone_number = entry_phone_number.get()
    title_of_book = entry_title_of_book.get()
    author = entry_author.get()
    year_of_publication = entry_year_of_publication.get()
    # создается объект
    library = (last_name, name, middle_name, phone_number,title_of_book, author, year_of_publication)
    # добавить объект в список
    list_book.append(library)
    # обновить ListBox
    list_book_var.set(list_book)
def rental():
    # получить индекс выбранного элемента
    index = library_listbox.curselection()
    # index[0] -  так как curselection()
    # возвращает список всех выбранных элементов
    # берем единственный, поэтому указываем индекс 0
    list_book[index[0]].to_rent()
    # и переопределяем ListBox
    list_book_var.set(list_book)
def cancel_rental():
    index = library_listbox.curselection()
    list_book[index[0]].cancel_rental()
    list_book_var.set(list_book)

if __name__ == '__main__':
    library = Library(" Иванов", "Петр"," Иванович", +79562348913, "Три товарища", "Эрих Мария Ремарк", 2008)
    print(library)
    root = Tk() # создаем корневой объект - окно
    root.title("Библиотека") # устанавливаем заголовок окна
    root.geometry("800x600") # устанавливаем размеры окна
    label_last_name = Label(text="Фамилия") # создаем текстовую метку
    label_last_name.pack() # размещаем метку в окне
    # поле ввода для фамилии
    entry_last_name = Entry() # создаем поле ввода
    entry_last_name.pack() # размещаем поле ввода в окне
    label_name = Label(text="Имя") # создаем текстовую метку
    label_name.pack() # размещаем метку в окне
    # поле ввода для имени
    entry_name = Entry() # создаем поле ввода
    entry_name.pack() # размещаем поле ввода в окне
    label_middle_name = Label(text="Отчество") # создаем текстовую метку
    label_middle_name.pack() # размещаем метку в окне
    # поле ввода для отчества
    entry_middle_name = Entry()  # создаем поле ввода
    entry_middle_name.pack()  # размещаем поле ввода в окне
    label_phone_number = Label(text="Номер телефона")# создаем текстовую метку
    label_phone_number.pack()  # размещаем метку в окне
    # поле ввода для номера телефона
    entry_phone_number = Entry() # создаем поле ввода
    entry_phone_number.pack()  # размещаем поле ввода в окне
    label_title_of_book = Label(text="Название книги") # создаем текстовую метку
    label_title_of_book.pack() # размещаем метку в окне
    # поле ввода для названия книги
    entry_title_of_book = Entry() # создаем поле ввода
    entry_title_of_book.pack() # размещаем поле ввода в окне
    label_author = Label(text="Автор") # создаем текстовую метку
    label_author.pack()# размещаем метку в окне
    # поле ввода для автора
    entry_author = Entry() # создаем поле ввода
    entry_author.pack() # размещаем поле ввода в окне
    label_year_of_publication = Label(text="Год издания") # создаем текстовую метку
    label_year_of_publication.pack() # размещаем метку в окне
    # поле ввода для года издания
    entry_year_of_publication = Entry() # создаем поле ввода
    entry_year_of_publication.pack()# размещаем поле ввода в окне
# кнопка для регистрации  читателя
    btn_register_reader = Button(text="Регистрация читателя", command=register_reader)
    btn_register_reader.pack()

list_book = [] # список для хранения книг
# создать объект "книга"
library = Library("Иванов ,", "Петр","Иванович", +79562348913, "Три товарища", "Эрих Мария Ремарк", 2008 )
# добавить объект в список
list_book.append(library)
# сохранить созданный и заполненный список в переменную типа Variable
list_book_var = Variable(value=list_book)
# создать ListBox, шириной 70 символов,
# в котором будет отображаться список list_book_var
library_listbox = Listbox(width=70, listvariable=list_book_var)
#добавить ListBox на форму
library_listbox.pack()
# кнопка для бронирования книги
btn_rent_book = Button(text="Забронировать книгу", command=rental)
btn_rent_book.pack()
# кнопка для возврата книги
btn_change_rent_book = Button(text="Вернуть книгу в библиотеку", command=cancel_rental)
btn_change_rent_book.pack()
root.mainloop()