import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(layout="wide")
#Load dataset
hour = pd.read_csv("hour.csv")
hour.head()

day = pd.read_csv("day.csv")
day.head()

bike_sharing = day.merge(hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Membuat judul
st.title('Bike Sharing Dashboard 🚲')

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    st.subheader('Keterkaitan antara Musim dengan Jumlah Peminjaman Sepeda')
    seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean()
    season_names = ['Spring', 'Summer', 'Fall', 'Winter']
    plt.bar(season_names, seasonal_data)
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Sewa Harian')
    plt.title('Keterkaitan Musim Terhadap Jumlah Sewa Sepeda Harian')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    st.subheader('Perbedaan dalam Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur')
    sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing, ax=ax)
    ax.set_title("Perbedaan Jumlah Peminjaman Sepeda Harian Hari Kerja dan Hari Libur")
    ax.set_xlabel("Hari Kerja")
    ax.set_ylabel("Jumlah Sewa Sepeda Harian")
    st.pyplot(fig)