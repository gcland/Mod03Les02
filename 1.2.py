library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
print(library)
while True:
    newbook = input("What book would you like to add to the library? ")
    newauthor = input("What is the author's name? ")
    list_library = list(library)
    list_library.append((newbook, newauthor))
    library = tuple(list_library)
    print(library)