import streamlit as st
from graph import build_graph
from langchain.schema import HumanMessage

st.set_page_config(page_title="Agentic News Summarizer", layout="centered")

st.title("Agentic News Summarizer")
st.write("Enter a topic to get a concise news summary.")

app = build_graph()

topic = st.text_input("Topic")

if st.button("Summarize") and topic:
    with st.spinner("Searching and summarizing..."):
        result = app.invoke({
            "messages": [
                HumanMessage(
                    content=f"Find recent news about {topic} and summarize it."
                )
            ]
        })

    st.subheader("Summary")
    st.write(result["messages"][-1].content)
