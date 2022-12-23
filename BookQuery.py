import requests

#display the available queries
print("select your query: ",end = "\n\n")
print("1. Author of the book.\n2. first published.\n3. languages available.\n4. common subjects between two books.")

#take input from user
N = input("Please enter your query number: ")
print()

#function to return a book info
def book_info(book):
    
    #change the input according to url
    book_name = book.lower().replace(" ","+")
    
    #get the responce from open library
    resp = requests.get(f"http://openlibrary.org/search.json?title={book_name}")
    
    #use JavaScript Object Notation to access the response 
    info = resp.json()
    return info['docs'][0]

#conditions according to given input
if(N == '1'):
    book = input("Enter book name: ")
    try:
        book_info = book_info(book)
        author = book_info['author_name'][0]
        print(f"Author of '{book}' is {author}.")
        
    except(IndexError):
        print("Sorry, the book you are trying is not found!")

elif(N == '2'):
    book = input("Enter book name: ")
    try:
        book_info = book_info(book)
        year = book_info['first_publish_year']
        print(f"The '{book}' book was first published in {year}.")
        
    except(IndexError):
        print("Sorry, the book you are trying is not found!")

elif(N == '3'):
    book = input("Enter book name: ")
    try:
        book_info = book_info(book)
        lang = book_info['language']
        print(f"The '{book}' book is available in:")
        print("  ", *lang)
        
    except(IndexError):
        print("Sorry, the book you are trying is not found!")

elif(N == '4'):
    book1 = input("Enter book name: ")
    book2 = input("Enter another book name: ")
    
    try:
        book1_info = book_info(book1)
        book2_info = book_info(book2)
        
        book1_subs = set(book1_info['subject'])
        book2_subs = set(book2_info['subject'])
        
        common = book1_subs & book2_subs

        print("Common subjects are: ")
        print()
        for i in common:
            print(i)
        
    except(IndexError):
        print("Sorry, the book you are trying is not found!")

else:
    print("Please enter any number only from above list!")