import streamlit
import pandas
import requests
import snowflake.connector

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
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) #take the json version of the data and normalize it
streamlit.dataframe(fruityvice_normalized) #display the data in tabular format
#snowflake connector code
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The food load list contains:")
streamlit.dataframe(my_data_rows)

#Adding additional text box for secondary fruit input from user
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'Kiwi')
streamlit.write('Thanks for adding', add_my_fruit)

              
