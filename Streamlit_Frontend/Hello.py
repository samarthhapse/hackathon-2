import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write(" Hello we are team 404 NOT FOUND ! 👋")

st.sidebar.success("Welcome to Food Recommendation System.")
st.write("TRACK : FOOD & HEALTHCARE")
st.write("Problem Statement :")
st.markdown("Develop a solution that helps individuals track their daily nutritional intake and provides personalized recommendations for a healthier lifestyle.")
st.write("Solution : ")
st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on our [repo](https://github.com/samarthhapse/HM0034_404NOTFOUND).
    """
)

st.write("Team Members 👋")
st.write("Samarth Hapse")
st.write("Sarthak Mhase")
st.write("Om Bhosale")
st.write("Nishikant Dalavi")
