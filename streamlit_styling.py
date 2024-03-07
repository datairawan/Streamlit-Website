import streamlit as st
import base64
from PIL import Image, ImageOps, ImageDraw

def markdown_text_style(text, color=None, font_size=None):
    text_style = f"""
                  <div style="text-align: center; color: {color}; font-size: {font_size}"> 
                  {text} 
                  </div>
                  """
    text_markdown = st.markdown(text_style, unsafe_allow_html=True)
    return text_markdown

def image_resizer(image,size_x, size_y):
    image = Image.open(image)
    resize_image = image.resize((size_x, size_y))

    color = "WhiteSmoke"
    border = (10, 10, 10, 10)
    border_image = ImageOps.expand(resize_image, border=border, fill=color) 
    
    return st.image(border_image)

def markdown_image(image, landing_page="https://www.lapakgaming.com/", width=200):

    result_image = st.markdown(
                                """
                                <a href={}>
                                <img src="data:image/png;base64,{}" width={}>
                                </a>
                                """.format(landing_page,
                                    base64.b64encode(open(image, "rb").read()).decode(), width
                                ),
                                unsafe_allow_html=True,
                            )
    return result_image
