
import pandas as pd
 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv(r"maro_cleand.csv")
st.title('gkc')
popi= df[df[["Place of Residence"]] != "na" ]
yui=popi["Place of Residence"].value_counts().sort_values(ascending=False)
xc=yui.sort_values(ascending=False)
x=xc.head(7)





def delivery(nmo):
    global values, labels
   
    values = []
    labels = []
    German = [ahmsd_mphsen("German Language Course"),'German Language Course']
    Specialized_Programming = [ahmsd_mphsen("Specialized Programming Diploma"),"Specialized Programming Diploma"]
    Reader = [ahmsd_mphsen("Cultured Reader"),"Cultured Reader"]
    Mathematics = [ahmsd_mphsen("Mathematics (Matific)"),"Mathematics (Matific)"]

    Fundamentals_of_Programming = [ahmsd_mphsen("Fundamentals of Programming"),"Fundamentals_of_Programming"]
    German_Explorer = [ahmsd_mphsen("German Explorer"),"German Explorer"]

    Online_School = [ahmsd_mphsen("Online School"),"Online School"]
    Digital_Marketing_Diploma = [ahmsd_mphsen("Digital Marketing Diploma"),"Digital Marketing Diploma"]
    Graphics_Diploma = [ahmsd_mphsen("Graphics Diploma"),"Graphics Diploma"]
    Little_Explorer = [ahmsd_mphsen("Little Explorer"),"Little Explorer"]
    namy=[German,Specialized_Programming,Reader,Mathematics,Fundamentals_of_Programming,German_Explorer,Online_School,Digital_Marketing_Diploma
         ,Graphics_Diploma,Little_Explorer]
    for i in namy:

        if i[0] > nmo:
        
            values.append(i[0])
            labels.append(i[1])



# ##############################################









def main2():
   
    plt.figure(figsize=(15, 8))
    plt.bar(x.index,x.values , color='skyblue')
    plt.xlabel("the number")
    plt.ylabel("the site ")
    plt.title("tha most palces that gkc known from")
    plt.xticks(rotation=70)
    st.pyplot(plt)
tab1, tab2, tab3 , tab4, tab5 = st.tabs(["Cat", "Dog", "Owl", "Rabbit", "Horse"])

with tab1:
    st.header("tha most palces that gkc known from")
    urt=st.button("click           me")
    if urt:
    
        main2()


with tab2:
    choice = st.radio("Select one option:", xc.index)
    def ahmsd_mphsen(hmasa):
        x=df[df["Place of Residence"] == choice ]
        y=x[x["Place of Residence"] != "na" ]
        return y[f"{hmasa}"].sum()
    st.header("A dog")
    delivery(0.75)
    urt2=st.button("click            me")
    if urt2:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)
        plt.show()
        st.pyplot(plt)

with tab3:
    st.header("the top 5 courses by month")
    moto=8
    def ahmsd_mphsen(hmasa):
    
        y=df[df["month"] == moto ]
        return y[f"{hmasa}"].sum()
    delivery(25)
    urt3=st.button("click              me")
    if urt3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('the top 5 courses by month ')  # Add title
        plt.xticks(rotation=90)


        st.pyplot(plt)
with tab4:
    st.header("the most interesting courses outside Egypt")
    def ahmsd_mphsen(hmasa):
        x=df[df["Country"] != "eygpt" ]
        y=x[x["Country"] != "na" ]
        return y[f"{hmasa}"].sum()
    delivery(1.5)
    ur3=st.button("click               me")
    if ur3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)

    
        st.pyplot(plt)
with tab5:
    st.header("percentage of people are interested in distance learning")
    r3=st.button("click                me")
    if r3:
        homa=df["Is Online Education Useful?"].value_counts()

    # Create the pie chart
        plt.pie(homa.values, labels=homa.index, autopct='%1.1f%%')

        # Add a title
        plt.title('Pie Chart')

        # Display the chart
        st.pyplot(plt)
