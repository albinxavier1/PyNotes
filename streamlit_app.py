import streamlit as st
from groq import Groq

# Implement API Key 
client = Groq(
    api_key="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",
)

st.title("PyNotes")
# Declaring the prompt 
prompt= st.text_input("Ask me anything:")
# Create a submit button
submit_button = st.button("Submit")
# Contextualizing the prompt
context_prompt = f"Act as an experienced technical trainer, who focuses in python and machine learning, give proper definitions, points to remember, code examples, summary, five practice questions and 10 interview questions on the topic  {prompt}"

# Creating Model and Testing Prompt
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": context_prompt,
        }
    ],
    model="llama3-70b-8192",
)

# If the submit button is clicked, display the chatbot's response
if submit_button:
    st.write(chat_completion.choices[0].message.content)
