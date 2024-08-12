import json
# collection=[]

# def addBook(title,author,year,gener):
#     d={}
#     d["tite"]=title
#     d["author"]=author
#     d['year']=year
#     d['gener']=gener
#     collection.append(d)
#     return collection

# t=input("enter the tilte to add: ")
# a=input("enter the author of book: ")
# y=input("enter the published year: ")
# g=input("grner of the book: ")
# (addBook(t,a,y,g))


# def Viewcollection(collection):
#     return collection
# (Viewcollection(collection))

# def savetojson(filename,collection):
#     f=open(filename)
#     data = json.load(f)
#     for i in collection:
#         data.append(i)
#     with open('books.json', 'w') as fp:
#         fp.write(
#             '[' +
#             ',\n'.join(json.dumps(i) for i in data) +
#             ']\n')
#     return data
# (savetojson('books.json',collection))

# def loadfromjson(filename):
#     jsoncollection=[]
#     f = open(filename)
#     data = json.load(f)
#     # print(data)
#     for i in data:
#         jsoncollection.append(i)
#     return jsoncollection
  
# # (loadfromjson('books.json'))

# def searchbyauthorortitle(f,name):
#     for i in f:
#         for k,v in i.items():
#             if i[k]==name:
#                 return i
#     else:
#         return "Not found"
# f=(loadfromjson('books.json'))
# searchbyauthorortitle(f,"The Handmaid's Tale")

# def removebook(file,title):
#     l=[]
#     for i in file:
#         if i["title"]!=title:
#             l.append(i)
#     return l
            
# f=(loadfromjson('books.json'))
# (removebook(f,"The Handmaid's Tale"))


    

# def main():
#     data = loadfromjson('books.json')

#     while True:
#         print('''
#             1. Display the collection of books
#             2. Add a book to the collection
#             3. Search book by author or title
            
#             4. Remove book from collection
#             5.Save to json
#             6. Exit
#         ''')
#         v = int(input("Enter option: "))
#         if v == 1:
#             print(Viewcollection(data))
#         elif v == 2:
#             t = input("Enter the title to add: ")
#             a = input("Enter the author of the book: ")
#             y = input("Enter the published year: ")
#             g = input("Enter the genre of the book: ")
#             data = addBook(t, a, y, g)
#             print("Book is added to our collection!")
#         elif v == 3:
#             i = input("Enter 'author' or 'book title' for searching: ")
#             print(searchbyauthorortitle(data,i))
#         elif v == 4:
#             titlename = input("Enter title name to delete that book: ")
#             data = removebook(data, titlename)
#             print("Removed successfully!")
#         elif v==5:
#             print(data)

#         elif v == 6:
#             print("Thank you for your collection!")
#             break
#         else:
#             print("Invalid option. Please choose again.")

# main()

            



# collection=[]

# def addbooks(title,author,year,gener):
#     book={}
#     book['title']=title
#     book['author']=author
#     book['year']=year
#     book['gener']=gener
#     collection.append(book)
#     return book


# def view_collection(colletion):
#     return collection

# def save_to_json(filename,collection):
#     f=open(filename)
#     filedata=json.load(filename)
#     for i in collection:
#         filedata.append(i)
#     with open(filename,'w') as fp:
#         for i in filedata:
#             fp.write(
#                 '[' +
#                 ',\n'.join(json.dumps(i))+
#                 ']\n')
            
#     return filedata


# def search_by_author_or_title(file,searchelement):
#     for i in file:
#         for k,v in i.items():
#             if searchelement==i[k]:
#                 return i
#     else:
#         print("No details found")

# def loadfromjson(filename):
#     json_collection=[]
#     f=open(filename)
#     data=json.load(f)
#     for i in data:
#         json_collection.append(i)
#     return json_collection

# def sort_by_key(book):
#     key=sort_by_key.sort_key
#     if key=='year':
#         return int(book[key])
#     return book[key]

# def sort_collections(books):
#     sort_key=input('you want to sort')
#     if sort_key in ['author','title','year','gener']:
#         sort_by_key.sort_key=sort_key
#         books.sort(key=sort_by_key)
#         print("collections are sorted")
#     else:
#         print("Invalid key")


import json

collection = []

def add_books(title, author, year, genre):
    # book = {
    #     'title': title,
    #     'author': author,
    #     'year': year,
    #     'genre': genre
    # }
    # collection.append(book)
    # return book
    
    book={}
    book['tilte']=title
    book['author']=author
    book['year']=year
    book['genre']=genre

    collection.append(book)
    return book





def view_collection():
    return collection


def save_to_json(filename):
    with open(filename, 'r') as f:
        filedata = json.load(f)

    filedata.extend(collection)

    with open(filename, 'w') as fp:
        json.dump(filedata, fp, indent=4)

    return filedata

    # with open(filename,'r') as data:
    #     fileData= json.load(data)

    # fileData.extend(collection)

    # with open(filename,'w') as fd:
    #     json.dump(fileData, fd, indent=4)
    # return fileData

def search_by_author_or_title(search_element):
    results = []
    for book in collection:
        if search_element == book['author'] or search_element == book['title']:
            results.append(book)
            return results
    else:
        print("No details found")
        


def load_from_json(filename):
    json_collection=[]
    f=open(filename)
    data=json.load(f)
    for i in data:
        json_collection.append(i)
    return json_collection

def sort_by_key(book):
    key = sort_by_key.sort_key
    if key == 'year':
        return int(book[key])
    return book[key]

def sort_collection():
    sort_key = input("Enter the key to sort by (title, author, year, genre): ")
    if sort_key in ['title', 'author', 'year', 'genre']:
        sort_by_key.sort_key = sort_key
        collection.sort(key=sort_by_key)
        print("Collection sorted successfully")
    else:
        print("Invalid key")

def main():
    filename = 'C:/Users/Venka/OneDrive/Desktop/CSPP/book/books.json'
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. View collection")
        print("3. Save collection to JSON")
        print("4. Load collection from JSON")
        print("5. Search by author or title")
        print("6. Sort collection")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            genre = input("Enter book genre: ")
            add_books(title, author, year, genre)
        
        elif choice == '2':
            for book in view_collection():
                print(book)
        
        elif choice == '3':
            save_to_json(filename)
            print("Collection saved to JSON.")
        
        elif choice == '4':
            load_from_json(filename)
            print("Collection loaded from JSON.")
        
        elif choice == '5':
            search_element = input("Enter author or title to search: ")
            results = search_by_author_or_title(search_element)
            for result in results:
                print(result)
        
        elif choice == '6':
            sort_collection()
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



