import pickle
import streamlit as st

model = pickle.load(open('Estimasi_Store.sav', 'rb'))

st.title('Estimasi Penjualan Supermarket')

Store_Sale = st.number_input('Input Penjualan Toko')
Daily_Customer_Count = st.number_input('Input pembeli harian')
Items_Available = st.number_input('Input barang yang tersedia')

predict = ''

if st.button('Estimasi Penjualan Supermarket'):
    predict = model.predict(
        [[Store_Sale, Daily_Customer_Count, Items_Available]]
    )
    st.write ('Estimasi Jumlah Store Area di Tiap Supermarket : ', predict)