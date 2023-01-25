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
from PIL import Image
import plotly_express as px

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
rating_df = pd.read_csv("resources/data/ratings.csv")
movie_df = pd.read_csv("resources/data/movies.csv")

# Working on data
df_merge = pd.merge(movie_df, rating_df, on='movieId')
opt = g = df_merge[["title", "rating"]]
cnt = g.title.value_counts()
df_val_counts = pd.DataFrame(cnt)
df_v = df_val_counts.reset_index()
df_v.columns = ['Movie', 'counts']
matrix = df_v.pivot_table(columns=['Movie'], values='counts')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Home", "About Us", "Project", "Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Navigation", page_options)

    if page_selection == "Home": 
        # Creating header  
        m = st.markdown("""<p style="text-align: justify; font-size:12px">We're thrilled to have you on board. \n We at Alpha Analytics use data to solve real-world challenges. Movies mean different things to different people. At Alpha Analytics, we regard movies as a chance to escape reality and spend time with family, friends, and loved ones. We made the decision to make the experience Awesome! Navigate to the 'Recommender System' to begin your adventure with movies created for every type of journey you desire. We'd like to know if you enjoyed seeing these films.</p>""", unsafe_allow_html=True)
        st.header("Alpha Analytics")
        st.image("https://t.ly/-Rt-", width=800)
        st.write("--")


        # Creating "Why Choose Us columns"
        col1,col2 = st.columns([1,2.5])
        col2.markdown("## WHY CHOOSE US")
        a1,a2,a3 = st.columns([1,1,1])
        # Data
        a1.markdown("#### DATA")
        a1.write("Discover and analyse important information and trends in your data")
        # Technology
        a2.markdown("#### TECHNOLOGY")
        a2.write("Cutting edge technogy to keep your business ahead in the market")
        # Innovation
        a3.markdown("#### INNOVATION")
        a3.write("Bringing your ideas to life in the toughest conditions")
        st.write("--")

        # Creating clients columns
        v1,v2 = st.columns([23,1])
        v1.markdown("<h1 style='text-align: center; color: white;'> Our Clients</h1>", unsafe_allow_html=True)
        x1,x2,x3,x4 = st.columns([1,1,1,1])
        x1.image("https://t.ly/lGTT")
        x2.image("https://t.ly/UxE_2")
        x3.image("https://t.ly/96lZ")
        x4.image("https://t.ly/AvAQ")
        st.write("--")

        # Creating Contact columns
        col3,col4 = st.columns([1,2])
        col4.markdown("## Contact Us")
        col5 = st.text_input("Email", "Enter your email")
        col6 = st.text_area("Message", "Your Message")
        but11,but12,but13 = st.columns([1,4,1])

        # Submit button
        if but11.button("Submit"):
            st.write("We are glad to hear from you")

    elif page_selection == "About Us":
        # Adding logo and title
        logo, title = st.columns(2)
        
        logo.image("https://t.ly/vQtS")

        title.header("Alpha Analytics")

        title.markdown("""<p style="text-align: left;">Alpha Analytics is a team of data enthusiast driven by passion for innovation. The company is well experienced in the delivery of cutting edge and innovative AI applications. The team's experience and expertise spreads across different industries.</p>""", unsafe_allow_html=True)

        st.write("--")

        # Creating columns for images
        c1,c2,c3 = st.columns([3,6,1])
        c2.markdown("## Meet the Alphas")
        d1,d2,d3= st.columns([1,1,1])
        e1,e2,e3= st.columns([1,1,1])
        d1.image("https://bit.ly/3kGcGPs")
        d1.write("#### Francis Egah, CEO")
        d2.image("https://t.ly/o3IS4")
        d2.write("#### Olisa Clement,  Chief AI Engineer")
        d3.image("https://t.ly/o3IS4")
        d3.write("#### Abdulrasheed Musa, Product Manager")
        e1.image("https://t.ly/o3IS4")
        e1.write("#### Emmanuel Oraegbu,  Data Scientist")
        e2.image("https://t.ly/o3IS4")
        e2.write("#### Sibusiso Mashabela, Sales Manager")
        e3.image("https://t.ly/o3IS4")
        e3.write("#### Karabo Molema, Business Analyst")
        st.write("--")
        st.write("<h1 style='text-align: center; color: red;'>Alpha Analytics</h1>", unsafe_allow_html=True)


    elif page_selection == "Project":
        st.title("Movie Recommender")
        st.subheader("Project Overview")
        st.write("In today's technology-driven society, recommender systems are socially and economically vital for ensuring that individuals can make proper decisions about the information they interact with on a regular basis. One instance where this is especially true is in movie content recommendations, where clever algorithms may assist viewers identify exceptional titles among tens of thousands of possibilities.")
        st.video("https://youtu.be/DeGHnp_oJSQ")
        st.subheader("Project Information")
        st.write("We a love to enjoy good movies. Our aim in this project is to enhance your movie experience through a robust recommendation engine putting into consideration your preferences as well  those of many other movie lovers. You can use the 'Content-based' engine to get movies similar to your preferences or 'Collaborative' engine to see what other people are watching. Enjoy your experience!!")
        st.subheader("Interact with Our Data")
        #
        x_ax_val = st.selectbox("Select Movie", options=matrix.columns)
        
        rtin = opt[opt["title"] == x_ax_val].value_counts(opt["rating"])
        rect = pd.DataFrame(rtin)
        df_vn = rect.reset_index()
        df_vn.columns = ['Rating', 'Rating Count']
        
        fig = px.bar(df_vn, x=df_vn["Rating"], y=df_vn["Rating Count"], color=df_vn["Rating Count"], title=x_ax_val)
        st.plotly_chart(fig)
    
    
    elif page_selection == "Recommender System":
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

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
