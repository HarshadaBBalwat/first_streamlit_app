import streamlit
streamlit.title('My parents new helthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Kale, spinach and rocket smothie')
streamlit.text('hard boiled free range egg')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




