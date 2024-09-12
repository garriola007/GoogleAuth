import streamlit as st
from google_auth_st import add_auth

add_auth()

# 
st.success('Logged in!')
st.write(st.session_state.email)
