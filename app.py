import streamlit as st
import utils as utl
from views import home,about,analysis,options,configuration

st.set_page_config(page_title='LapakGimbal',
                   page_icon= ':snail:',
                   layout='wide' )
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    print(route)
    if route == "home":
        home.load_view()
    elif route == "transaction":
        about.load_view()
    elif route == "reward":
        analysis.load_view()
        
navigation()

st.markdown("""
            <style>
            header{visibility: hidden}
            footer{visibility: hidden}
            [data-testid=stMarkdownContainer]{
                                                text-align: center;
                                                display: block;
                                                margin-left: auto;
                                                margin-right: auto;
                                                width: 100%;
                                            }
         
            </style>
            """, unsafe_allow_html=True)

