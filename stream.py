import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("gambar/logo.gif")

    

st.header('E-Commerce :sparkles:')   
eng_productid_score= pd.read_csv("eng_productid_score.csv")

score_product = eng_productid_score.groupby(['product_category_name_english'])['review_score'].mean()
resetindex = score_product.sort_values(ascending=False).reset_index().head(5)
    
score_product = eng_productid_score.groupby(['product_category_name_english'])['review_score'].mean()
resettrue = score_product.sort_values(ascending=True).reset_index().head(5)


st.subheader("5 kategori produk terbaik dan terburuk berdasarkan skor tinjauan pembeli")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
colors = ["#6C0918", "#A90F26", "#D91331", "#F2969B", "#FFE4E1"]
 
sns.barplot(x="review_score", y="product_category_name_english", data=resetindex, palette=colors, ax=ax[0])
ax[0].set_ylabel('kategori produk', fontsize=30)
ax[0].set_xlabel('skor produk', fontsize=30)
ax[0].set_title("5 kategori produk terbaik", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=35)
ax[0].tick_params(axis ='x', labelsize=30)

sns.barplot(x="review_score", y="product_category_name_english", data=resettrue, palette=colors, ax=ax[1])
ax[1].set_ylabel('kategori produk', fontsize=30)
ax[1].set_xlabel('skor produk', fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("5 kategori produk terburuk", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
st.pyplot(fig)

qt_product = eng_productid_score.groupby(['product_category_name_english'])['product_photos_qty'].sum()
resetindex1 = qt_product.sort_values(ascending=False).reset_index().head(10)

st.subheader("Total jumlah pembelian 10 kategori produk terbanyak")
fig, ax = plt.subplots(figsize=(18,6))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="product_category_name_english", 
    y="product_photos_qty",
    data=resetindex1,
    palette=colors,
    ax=ax
)
ax.set_ylabel("Jumlah", fontsize=30)
ax.set_xlabel("Kategori produk", fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

