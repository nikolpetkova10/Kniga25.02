import streamlit as st
st.title("Book")
if "books" not in st.session_state:
  st.session_state.books = []
  st.header("Add a book")
  title = st.text_input("Title")
  author = st.text_input("Author")
  price = st.number_input("Price")
if st.button("Add the book"):
  book = {
    "Title": title,
    "Author": author,
    "Price": price
  }
  st.session_state.books.append(book)
  st.success("The book is added")
if st.button("Show all books"):
  if len(st.session_state.books) ==0:
    st.write("There's no books added.")
  else:
    for book in st.session_state.books:
      st.write("Title", book["Title"])
      st.write("Author", book["Author"])
      st.write("Price", book["Price"])
      st.write("-----------------------")
st.header("Find by author")
search_author = st.text_input("Enter the name of the author")
if st.button("Find by author"):
  found = False
for books in st.session_state.books:
  if book["author"] == search_author:
    st.write(book)
    found = True
  if found == False:
    st.write("There's no books by this author.")
             
      
      




             
  
