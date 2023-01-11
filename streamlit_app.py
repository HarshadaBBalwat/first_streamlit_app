import streamlit
streamlit.title('My parents new helthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Kale, spinach and rocket smothie')
streamlit.text('hard boiled free range egg')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['avocado','stroberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
