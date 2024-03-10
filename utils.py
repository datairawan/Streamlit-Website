#reference: https://github.com/BugzTheBunny/streamlit-navbar-flaskless/tree/main
import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS

def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_current_route():
    try:
        return st.query_params["nav"]
    except:
        return None

def navbar_component():
    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                {navbar_items}
                </ul>
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }
    </script>
    '''
    html(js)
    
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
