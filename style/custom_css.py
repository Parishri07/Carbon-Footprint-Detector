import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 8px;
            font-size: 16px;
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            background-color: #45a049;
            color: white;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)
