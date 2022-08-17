import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import plotly.express as px
from PIL import Image
import os

@st.cache
def load_image(img):
    im = Image.open(os.path.join(img))
    return im

html_temp = """
            <div style="background-color:{};padding:10px;border-radius:10px;">
            <h1 style="color:{};text-align:center;">Programming Langages Trend App </h1>
            </div> """

LANG = {"python":"Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. This versatility, along with its beginner-friendliness, has made it one of the most-used programming languages today. A survey conducted by industry analyst firm RedMonk found that it was the second-most popular programming language among developers in 2021",
        "java":"Java is a programming language and computing platform first released by Sun Microsystems in 1995. It has evolved from humble beginnings to power a large share of today’s digital world, by providing the reliable platform upon which many services and applications are built. New, innovative products and digital services designed for the future continue to rely on Java, as well.",
        "javascript":"JavaScript is a programming language for the web. Its syntax is based on Java and C languages. Used in both the front-end and back-end of many platforms, JavaScript has become a standard. For every animated or interactive object you see online, chances are JavaScript is involved.",
        "julia":"Julia is a high-level, high-performance, dynamic programming language. While it is a general-purpose language and can be used to write any application, many of its features are well suited for numerical analysis and computational science.",
        "go":"Go (also called Golang or Go language) is an open source programming language used for general purpose. Go was developed by Google engineers to create dependable and efficient software. Most similarly modeled after C, Go is statically typed and explicit.",
        "R":"R is a language and environment for statistical computing and graphics. It is a GNU project which is similar to the S language and environment which was developed at Bell Laboratories (formerly AT&T, now Lucent Technologies) by John Chambers and colleagues. R can be considered as a different implementation of S. There are some important differences, but much code written for S runs unaltered under R."}

def main():

    st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)
    menu = ["Home","Trends","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.image(load_image('data/images/langages.png'), width=700)
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Python"):
                st.write(LANG["python"])
            with st.expander("R"):
                st.write(LANG["R"])
            with st.expander("Julia"):
                st.write(LANG["julia"])

        with col2:
            with st.expander("Java"):
                st.write(LANG["java"])
            with st.expander("JavaScript"):
                st.write(LANG["javascript"])
            with st.expander("Go"):
                st.write(LANG["go"])

    elif choice == "Trends":
        st.subheader("Programming Lang Trends")
        df = pd.read_csv("data/clean_with_dates.csv")
        st.dataframe(df.head())

        all_columns = df.columns.tolist()
        lang_choice = st.multiselect("Langage", all_columns, default='Python')
        new_df = df[lang_choice]

        c1, c2 = st.columns([3,1])
        with c1:
            with st.expander("Line Chart"):
                st.line_chart(new_df)

        with c2:
            with st.expander("Stats"):
                st.write(new_df.describe().T)


        with st.expander("Area Chart"):
            st.area_chart(new_df)

        with st.expander("Pie Chart"):
            sum_df = pd.read_csv("data/lang_sum_num_data.csv")
            #st.dataframe(sum_df.head())
            fig_pie = px.pie(sum_df,values='Sum',names='lang',title='Total Langage Searches')
            st.plotly_chart(fig_pie)

        df2 = pd.read_csv("data/clean_with_dates.csv", parse_dates=['Week'], index_col=['Week'])
        all_columns_for_df2 = df2.columns.tolist()
        lang_choice_by_year = st.multiselect("Programming Langage",all_columns_for_df2, default='Python')
        year_interval = st.selectbox("Year",["2015","2016","2017","2018","2019","2020","All"])

        if year_interval == "All":
            ts = df2
        else:
            ts = df2[year_interval]

        fig_line = px.line(ts,x=ts.index,y=lang_choice_by_year)
        st.plotly_chart(fig_line)
    else:
        st.subheader("About")



if __name__ == '__main__':
    main()

