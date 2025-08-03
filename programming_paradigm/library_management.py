# 

class Book:
    def __init__(self):
        pass
        # self.title = title
        # self.author = author
        # self._is_checked_out = is_checked_out

    # def book(self):
    #     new_book = f"{self.title}, {self.author}"
    #     return new_book

    def return_book(self):
        return True

class Library(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self._books = []

    def add_book(self):
        book = {"title": self.title,"author": self.author}
        self._books.append(book)
    
    def check_out_book(self):
        book = self._books.get("title")
        if self.title == book.title:
            return f"{(self.title).title()} is {self.author}"

    def return_book(self):
        pass

    def list_available_books(self):
        pass