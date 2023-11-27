import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv(r"C:\Users\maraw\OneDrive\Desktop\final project\maro_cleand.csv")
st.title('gkc')

def main2():
    plt.figure(figsize=(15, 8))
    x = df["Learned About Genius From"].value_counts()
    plt.bar(x.index, x.values, color='skyblue')
    plt.xlabel("the number")
    plt.ylabel("the site ")
    plt.title("tha most palces that gkc known from")
    plt.xticks(rotation=70)
    st.pyplot(plt)

urt = st.button("click me")
if urt:
    main2()

def part2():
    global labels, values
    choice = st.radio("Select one option:", df["Learned About Genius From"].unique())
    target_value = choice

    if choice in ["Facebook", "friend"]:
        matching_rows_df = df.loc[df['Learned About Genius From'] == target_value]

        German = matching_rows_df.loc[matching_rows_df['German Language Course'] == 1, 'German Language Course'].count()
        Specialized_Programming = matching_rows_df['Specialized Programming Diploma'].value_counts().iloc[0]
        Reader = matching_rows_df.loc[matching_rows_df['Cultured Reader'] == 1, 'Cultured Reader'].count()
        Mathematics = 0  # Adjust as needed
        Fundamentals_of_Programming = matching_rows_df.loc[matching_rows_df['Fundamentals of Programming'] == 1, 'Fundamentals of Programming'].count()
        German_Explorer = 0  # Adjust as needed
        Online_School = matching_rows_df.loc[matching_rows_df['Online School'] == 1, 'Online School'].count()
        Digital_Marketing_Diploma = matching_rows_df.loc[matching_rows_df['Digital Marketing Diploma'] == 1, 'Digital Marketing Diploma'].count()
        Graphics_Diploma = matching_rows_df.loc[matching_rows_df['Graphics Diploma'] == 1, 'Graphics Diploma'].count()
        Little_Explorer = matching_rows_df.loc[matching_rows_df['Little Explorer'] == 1, 'Little Explorer'].count()

        values = [German, Specialized_Programming, Reader, Mathematics, Fundamentals_of_Programming, German_Explorer, Online_School, Digital_Marketing_Diploma, Graphics_Diploma, Little_Explorer]
        labels = ["German Language Course", "Specialized Programming Diploma", "Cultured Reader", "Mathematics (Matific)", "Fundamentals of Programming", "German Explorer", "Online School", "Digital Marketing Diploma", "Graphics Diploma", "Little Explorer"]

    elif choice == "social media":
        matching_rows_df = df.loc[df['Learned About Genius From'] == target_value]

        German = 0
        Specialized_Programming = matching_rows_df['Specialized Programming Diploma'].value_counts().iloc[0]
        Reader = matching_rows_df.loc[matching_rows_df['Cultured Reader'] == 1, 'Cultured Reader'].count()
        Mathematics = 0  # Adjust as needed
        Fundamentals_of_Programming = matching_rows_df.loc[matching_rows_df['Fundamentals of Programming'] == 1, 'Fundamentals of Programming'].count()
        German_Explorer = 0  # Adjust as needed
        Online_School = matching_rows_df.loc[matching_rows_df['Online School'] == 1, 'Online School'].count()
        Digital_Marketing_Diploma = matching_rows_df.loc[matching_rows_df['Digital Marketing Diploma'] == 1, 'Digital Marketing Diploma'].count()
        Graphics_Diploma = matching_rows_df.loc[matching_rows_df['Graphics Diploma'] == 1, 'Graphics Diploma'].count()
        Little_Explorer = matching_rows_df.loc[matching_rows_df['Little Explorer'] == 1, 'Little Explorer'].count()

        values = [German, Specialized_Programming, Reader, Mathematics, Fundamentals_of_Programming, German_Explorer, Online_School, Digital_Marketing_Diploma, Graphics_Diploma, Little_Explorer]
        labels = ["German Language Course", "Specialized Programming Diploma", "Cultured Reader", "Mathematics (Matific)", "Fundamentals of Programming", "German Explorer", "Online School", "Digital Marketing Diploma", "Graphics Diploma", "Little Explorer"]

    elif choice == "youtube":
        matching_rows_df = df.loc[df['Learned About Genius From'] == target_value]

        German = 0
        Specialized_Programming = matching_rows_df['Specialized Programming Diploma'].value_counts().iloc[0]
        Reader = 0
        Mathematics = 0  # Adjust as needed
        Fundamentals_of_Programming = 0
        German_Explorer = 0
        Online_School = 0
        Digital_Marketing_Diploma = 0
        Graphics_Diploma = 0
        Little_Explorer = 0

        values = [German, Specialized_Programming, Reader, Mathematics, Fundamentals_of_Programming, German_Explorer, Online_School, Digital_Marketing_Diploma, Graphics_Diploma, Little_Explorer]
        labels = ["German Language Course", "Specialized Programming Diploma", "Cultured Reader", "Mathematics (Matific)", "Fundamentals of Programming", "German Explorer", "Online School", "Digital Marketing Diploma", "Graphics Diploma", "Little Explorer"]

    

part2()
urt = st.button("click    me")
if urt:
    plt.bar(labels, values)
    plt.xlabel('Courses')  # Add x-axis label
    plt.ylabel('Count')  # Add y-axis label
    plt.title('Course Enrollment')  # Add title
    plt.xticks(rotation=90)
    st.pyplot(plt)

def part3():
    global labels, values

    matching_rows_df = df.loc[(df['Country'] != "eygpt") & (df['Country'] != "na")]

    German = matching_rows_df.loc[matching_rows_df['German Language Course'] == 1, 'German Language Course'].count()
    Specialized_Programming = matching_rows_df['Specialized Programming Diploma'].value_counts().iloc[0]
    Reader = matching_rows_df.loc[matching_rows_df['Cultured Reader'] == 1, 'Cultured Reader'].count()
    Mathematics = 0  # Adjust as needed
    Fundamentals_of_Programming = matching_rows_df.loc[matching_rows_df['Fundamentals of Programming'] == 1, 'Fundamentals of Programming'].count()
    German_Explorer = 0  # Adjust as needed
    Online_School = matching_rows_df.loc[matching_rows_df['Online School'] == 1, 'Online School'].count()
    Digital_Marketing_Diploma = matching_rows_df.loc[matching_rows_df['Digital Marketing Diploma'] == 1, 'Digital Marketing Diploma'].count()
    Graphics_Diploma = matching_rows_df.loc[matching_rows_df['Graphics Diploma'] == 1, 'Graphics Diploma'].count()
    Little_Explorer = matching_rows_df.loc[matching_rows_df['Little Explorer'] == 1, 'Little Explorer'].count()

    values = [German, Specialized_Programming, Reader, Mathematics, Fundamentals_of_Programming, German_Explorer, Online_School, Digital_Marketing_Diploma, Graphics_Diploma, Little_Explorer]
    labels = ["German Language Course", "Specialized Programming Diploma", "Cultured Reader", "Mathematics (Matific)", "Fundamentals of Programming", "German Explorer", "Online School", "Digital Marketing Diploma", "Graphics Diploma", "Little Explorer"]

    return labels, values

part3()
urt = st.button("click   me")
if urt:
    plt.bar(labels, values)
    plt.xlabel('Courses')  # Add x-axis label
    plt.ylabel('Count')  # Add y-axis label
    plt.title('Course Enrollment')  # Add title
    plt.xticks(rotation=90)
    st.pyplot(plt)

