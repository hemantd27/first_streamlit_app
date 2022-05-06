import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
try:
  streamlit.title('My Mom\'s Healthy Dinner')
  streamlit.header('Breakfast Menu')
  streamlit.text('🥣 Omega 3 & Blueberry Oatmeal ')
  streamlit.text('🥗 Kale,Spinach & rocket smoothie')
  streamlit.text('🐔Hard-Boiled Free-Range Egg')
  streamlit.text('🥑🍞Avocado Toast')
  streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
  my_fruit_list = my_fruit_list.set_index('Fruit')
  fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
  my_fruit_show = my_fruit_list.loc[fruits_selected]
  streamlit.dataframe(my_fruit_show)
  
  streamlit.header("The fruit load list containts:")
  
  # function to get list of fruits from snowflake db-table
  def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
  
  def add_fruit_to_list(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
      return "Thanks for adding a new fruit:"+new_fruit
  
  if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
  
  if streamlit.button('Add a Fruit to a List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = add_fruit_to_list("kiwi")
    streamlit.text(back_from_function)
    
    
  # function to get desired fruit from snowflake db-table
  # def get_fruityvice_data(this_fruit_choice):
   #  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
   #  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   #  return fruityvice_normalized
    
  
  
  
   #try:
    # fruit_choice = streamlit.text_input("what fruit would you like information about","kiwi")
    # if not fruit_choice:
    #   streamlit.error("Please select a fruit to get an information")
     #else:       
    #   fruityvice_normalized = get_fruityvice_data(fruit_choice)
     #  streamlit.dataframe(fruityvice_normalized)
      #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      #my_cur = my_cnx.cursor()
      #my_cur.execute("SELECT * from fruit_load_list")
      #my_data_rows = my_cur.fetchall()
      #streamlit.header("The fruit load list containts:")
      #streamlit.dataframe(my_data_rows)
      #fruit_choice = streamlit.text_input("what fruit do you like to add?","kiwi")
      #streamlit.write('The user entered',fruit_choice)
      #my_cur.execute("insert into fruit_load_list values ('from streamlit')")
      
   #except URLError as e:
     #streamlit.error()    
except:
  streamlit.text("exception found")
  
