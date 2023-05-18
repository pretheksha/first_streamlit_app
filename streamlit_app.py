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
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#new section to display fruity vice response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
              
