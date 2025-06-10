from langchain_groq import ChatGroq
from dotenv import load_dotenv
from backend.logger.init_logger import init_logger

# Initialize the logger
logger = init_logger(__name__)


def init_llm(model_name: str) -> ChatGroq:
    """
    Function to initialize the LLM model to be used as the base LLM for the SQL Agent.

    Args:
        model_name (str): Name of the LLM to initialize as the base LLM.

    Returns:
        llm (ChatGroq): A ChatGroq runnable object for the given LLM name input.
    """

    logger.info(f"Initializing LLM with model name: {model_name}")
    # Load environment variables from the .env file to access the Groq API key
    load_dotenv()
    logger.info("Environment variables loaded successfully.")

    # Initialize the LLM runnable with the specified model name
    llm = ChatGroq(model=model_name)

    logger.info("LLM initialized successfully.")
    return llm
