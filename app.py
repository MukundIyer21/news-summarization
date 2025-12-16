import streamlit as st
from graphs.graph import news_graph

st.title("AI News Summarizer")

topic = st.text_input("News Topic")
timeframe = st.selectbox("Timeframe", ["daily", "weekly", "monthly"])

if st.button("Generate Summary"):
    if topic:
        result = news_graph.invoke(
            {"topic": topic, "timeframe": timeframe}
        )
        st.markdown(result["final_output"])
