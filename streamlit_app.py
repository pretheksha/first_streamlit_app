import streamlit
import pandas

streamlit.title("Pretheksha is a beautiful, confident and strong person")
streamlit.header("Breakfast Menu")
streamlit.caption(" 🥣 Omega 3 and blueberry oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket smoothie")
streamlit.text(" 🐔 Hard Boiled Free Range eggs")
streamlit.text("🥑🍞 avacado Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),["Avacado" , "Strawberries"])
streamlit.dataframe(my_fruit_list)
              
