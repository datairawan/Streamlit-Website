import streamlit as st
from utils import markdown_text_style, image_resizer, markdown_image

def load_view():
    markdown_text_style("🔥 Lagi Populer 🔥",font_size="20px")
    st.markdown('')

    col0, col1, col2, col3, col4, col5 = st.columns(spec=6)

    with col1:
        
        markdown_text_style("Mobile Legends",font_size="20px")
        markdown_image("assets/images/mobile_legends.png","https://www.lapakgaming.com/id-id/mobile-legends")

    with col2:
        markdown_text_style("Free Fire",font_size="20px")
        markdown_image("assets/images/free_fire.jpg","https://www.lapakgaming.com/id-id/free-fire")

    with col3:
        markdown_text_style("PUBG Mobile",font_size="20px")
        markdown_image("assets/images/pubg_mobile.jpg","https://www.lapakgaming.com/id-id/pubg-mobile")

    with col4:
        markdown_text_style("Genshin Impact",font_size="20px")
        markdown_image("assets/images/genshin_impact.webp","https://www.lapakgaming.com/id-id/genshin-impact")
