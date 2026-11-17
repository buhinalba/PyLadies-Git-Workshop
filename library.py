books = []

def add(title: str, author: str, pages: int) -> None:
    books.append({"Title": title, "Author": author, pages: pages})

if __name__ == '__main__':
    add(title="My first book", author="PyLadies", pages=23)


    print(books)