# import streamlit as st
# from langchain.llms import OpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# import os

# os.environ['OPENAI_API_KEY'] = ""

# # Initialize the LangChain components
# llm = OpenAI(model_name="gpt-4o")
# memory = ConversationBufferMemory()
# conversation_chain = ConversationChain(llm=llm, memory=memory)

# # Streamlit App
# st.set_page_config(page_title="LangChain Chatbot", layout="wide")
# st.title("AI-QuizCraft-WebApp")

# # Sidebar for user input
# st.sidebar.header("Chat Settings")
# user_name = st.sidebar.text_input("Enter your name", "User")

# # Main Chat Interface
# if "conversation_history" not in st.session_state:
#     st.session_state.conversation_history = []

# st.header(f"Hello, {user_name}!")

# # Display conversation history
# for i, (user_input, response) in enumerate(st.session_state.conversation_history):
#     st.write(f"**{user_name}:** {user_input}")
#     st.write(f"**Bot:** {response}")

# # User input
# user_input = st.text_input(
#     "You: ", key="input", value="", on_change=None, args=None)

# # Process user input and get the response
# if user_input and st.session_state.get("last_user_input") != user_input:
#     response = conversation_chain.run(user_input)
#     st.session_state.conversation_history.append((user_input, response))
#     st.session_state.last_user_input = user_input
#     st.experimental_rerun()

# # Clear conversation history
# if st.sidebar.button("Clear Chat"):
#     st.session_state.conversation_history = []
#     st.session_state.last_user_input = ""
#     st.experimental_rerun()
