# Importing Additional Python Libraries
import streamlit as st
import time
import requests

# Importing Local Python Modules
from backend.llm.init_llm import init_llm
from backend.llm.get_llm_response import get_llm_response
from backend.llm_list.get_llm_list import get_llm_from_groq, get_llm_list
from backend.logger.init_logger import init_logger

# Initialize the logger
logger = init_logger(__name__)

# Customizing the Streamlit Page
st.set_page_config(
    page_title="Impersona-AI",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/m-asif-ansari/",
        "About": "# This is a ChatBot. Made by- Asif Ansari",
    },
)

# Displaying the logo

st.logo(
    "https://mintlify.s3.us-west-1.amazonaws.com/agentai/logo/light.png", size="large"
)

# Page Title and Subtitle
st.title("Impersona-AI")
st.subheader("Select the AI Chatbot Persona and Ask your questions")

# Sidebar customization
st.sidebar.title("AI Chat-Bot")
st.sidebar.write(
    "This is a Personified AI ChatBot that can talk to you based on the persona you choose."
)


# Sidebar options for LLM personas
st.sidebar.divider()
st.sidebar.write("Select the Chat-bot persona")
persona_list = [
    "storyteller",
    "science-nerd",
    "tech-guru",
    "history-buff",
    "philosopher",
    "financial-advisor",
    "health-expert",
    "travel-guide",
    "fitness-coach",
]
selected_persona = st.sidebar.selectbox("Select a persona", persona_list, on_change=lambda: st.toast(f"Persona changed"))

# Initialize the selected LLM
st.sidebar.divider()
model_list = get_llm_list()
st.sidebar.write("Select the Base LLM to be used as the Chat-Bot's brain")
model_name = st.sidebar.selectbox("Select a model", model_list, on_change=lambda: st.toast(f"Model changed"))
llm = init_llm(model_name)



def reset_history():
    """
    Reset the chat history to the initial state.
    """
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I assist you?"}
    ]
    st.toast("Chat history has been reset. You can start a new conversation now.")


st.sidebar.divider()
st.sidebar.button(
    "Reset Chat",
    on_click=reset_history,
    icon="🔄",
    help="Reset the chat history to start a new conversation",
    type="primary",
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I assist you?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.empty()


# Function to generate a response with a delay for streaming effect
def response_generator(response):
    """
    Generate a response word by word with a delay for a streaming effect.

    Args:
        response (str): The full response to be streamed.

    Yields:
        str: The next word in the response.
    """
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.03)


# React to user input
if prompt := st.chat_input("Enter your query here!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Generating Response...", show_time=True):
            try:
                # Get the response from the LLM
                response = get_llm_response(llm, selected_persona, prompt)
                # response = requests.post(
                #     "http://127.0.0.1:8000/llm_response/",
                #     json={"model_name": model_name, "persona": selected_persona, "prompt": prompt}
                # ).json().get("llm_response")
            except Exception as e:
                response = (
                    f"Facing issues with LLM. Try using a different Base LLM. Error: {e}"
                )
        st.write_stream(response_generator(response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
