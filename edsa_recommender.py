"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Data Visulization
import matplotlib.pyplot as plt

# Custom Libraries

from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Loading a css stylesheet
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css("resources/CSS/Styling.css")#

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Introduction", "Exploratory Data Analysis", "Recommender System", "Solution Overview","About"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------
    if page_selection == "Introduction":
       
        st.markdown("<h2 style='text-align: center;'>Team CW1 TheAlpha's</h1>", unsafe_allow_html=True)
        
        info_pages = ["Select Option", "General Information", "Contributors"]
        info_page_selection = st.selectbox("", info_pages)
        
        if info_page_selection == "Select Option":
            st.info("Welcome! Select an option from the menu above.")
            
        if info_page_selection == "General Information":
            st.info("Read more about the project and the data that was used to solve the problem at hand.")
            st.markdown(open('resources/markdown/introduction/intro.md').read(), unsafe_allow_html=True)
              
            definitions = st.checkbox("Show definitions")
    
            
            if definitions:
                st.write(open('resources/markdown/introduction/data_definition.md', encoding='utf8').read(), unsafe_allow_html=True)
                
        if info_page_selection == "Contributors":
            st.info("Meet the amazing team members that contributed to this project.")
    
            # Abdulrasheed
            st.markdown("<h3 style='text-align: center;'>Abdulrasheed Musa</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>job title</p>", unsafe_allow_html=True)
            
            # Francis 
            st.markdown("<h3 style='text-align: center;'>Francis Egah</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'> job title</p>", unsafe_allow_html=True)
        
    
            # Karabo 
            st.markdown("<h3 style='text-align: center;'>Karabo Molema</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>job title</p>", unsafe_allow_html=True)
        
    
            # Olisa 
            st.markdown("<h3 style='text-align: center;'>Olisa Clement</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>job title</p>", unsafe_allow_html=True)
            
    
            # Sibusiso 
            st.markdown("<h3 style='text-align: center;'>Sibusiso Mashabela</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>job title</p>", unsafe_allow_html=True)
            
    
            # Emmanuel 
            st.markdown("<h3 style='text-align: center;'>Emmanuel Oraegbu</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>job title</p>", unsafe_allow_html=True)
                
                # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
    
    if page_selection == "Home":
        
        st.sidebar.markdown(open('resources/markdown/introduction/Page_Description.md').read(), unsafe_allow_html=True)
        st.image('resources/imgs/Banner.png',use_column_width=True)

        html_temp = """
     <div style="background-color:{};padding:10px;border-radius:10px;margin:10px;border:3px; border-style:solid; border-color:#000000; padding: 1em;">
     <h1 style="color:{};text-align:center;">UNSUPERVISED LEARNING</h1>
     </div>
     """
       
        title_temp = """
     <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
     <h1 style="color:black;text-align:center;">Recommender System</h1>
     <h2 style="color:black;text-align:center;">Team-CW1</h2>
     <h2 style="color:black;text-align:center;">January 2023</h3>
     </div>
     """
        st.markdown(html_temp.format('#D2691E00','black'), unsafe_allow_html=True)
        st.markdown(title_temp, unsafe_allow_html=True)
    
    
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
