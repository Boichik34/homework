class Book:

    def __init__(self, name, autor, genre, date_of_publication, is_read):
        self.__name = name
        self.__autor = autor
        self.__genre = genre
        self.__date_of_publication = date_of_publication
        self.__is_read = is_read

    # def __str__(self) -> str:
    #     return f"{self.__name}, {self.__autor}, {self.__genre}, {self.__date_of_publication}, {self.is_read}"

    def get_name(self) -> str:
        return self.__name

    def get_autor(self) -> str:
        return self.__autor

    def get_genre(self) -> str:
        return self.__genre

    def get_date_of_publication(self) -> int:
        return self.__date_of_publication

    def get_is_read(self) -> bool:
        return self.__is_read

    def set_is_read(self, new_is_read: bool):
        self.is_read = new_is_read


# class BookList:
#     def __init__(self) -> None:
#         self.list = 
