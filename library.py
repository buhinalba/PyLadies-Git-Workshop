books = []

def get_authors(books):
    authors = []
    for book in books:
        authors.append(book["Author"])
    return authors

def add(title: str, author: str, pages: int) -> None:
    books.append({"Title": title, "Author": author, pages: pages})

if __name__ == '__main__':
    add(title="My first book", author="PyLadies", pages=23)
    add(title="The Hobbit", author="J.R.R. Tolkien", pages=310)
    add(title="Dune", author="Frank Herbert", pages=341)
    # print(books)

    authors = get_authors(books)
    print(authors)