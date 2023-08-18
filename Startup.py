import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

df=pd.read_csv('Startup_Clean.csv')
df['Date'] = pd.to_datetime(df['Date'],errors='coerce')


def load_investor_details(Investors_Name):
    st.title('Investors_Name')
    last_5head=df[df['Investors Name'].str.contains(Investors_Name)].head()[['Date','Startup','Industry','City  Location','InvestmentnType','amount']]
    st.subheader('Most Recent Investment')
    st.dataframe(last_5head)
    
    col1, col2=st.columns(2)
    with col1:
     big_series=df[df['Investors Name'].str.contains(Investors_Name)].groupby('Startup')['amount'].sum().sort_values(ascending=False).head()
     st.subheader('Biggest Investment')
     fig, ax = plt.subplots()
     ax.bar(big_series.index,big_series.values)
     st.pyplot(fig)
    
    with col2:
        verti_series=df[df['Investors Name'].str.contains(Investors_Name)].groupby('Industry')['amount'].sum()
        st.subheader('Sector investe in')
        fig1, ax1 = plt.subplots()
        ax1.pie( verti_series,labels=verti_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col1,col2=st.columns(2)
    with col1:
     Industry=df[df['Investors Name'].str.contains(Investors_Name)].groupby('InvestmentnType')['amount'].sum().sort_values(ascending=False)
     st.subheader('Industry_Analysiis')
     fig2, ax2 = plt.subplots()
     ax2.bar(Industry.index,Industry.values)
     st.pyplot(fig2)

    with col2:
     City=df[df['Investors Name'].str.contains(Investors_Name)].groupby('City  Location')['amount'].sum().sort_values(ascending=False)
     st.subheader('City_Analysiis')
     fig3, ax3= plt.subplots()
     ax3.pie(City,labels=City.index,autopct="%0.01f%%")
     st.pyplot(fig3)

    df['Year']=df['Date'].dt.year
    YOY_invest=df[df['Investors Name'].str.contains(Investors_Name)].groupby('Year')['amount'].sum()
    st.subheader('YOY_Analysis')
    fig4, ax4 = plt.subplots()
    ax4.plot(YOY_invest.index,YOY_invest.values)
    st.pyplot(fig4)

st.sidebar.title('Startup Funding Analysis')

option=st.sidebar.selectbox('Select one',['overall Analysis','Startup','investor'])

if option =='overall analysis':
    st.title('overall analysis')
elif option=='Startup':
    st.sidebar.selectbox('select group',sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('startup analysis')
else:
    selected_Investors_Name=st.sidebar.selectbox('select group',sorted(set(df['Investors Name'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_Investors_Name)
   

