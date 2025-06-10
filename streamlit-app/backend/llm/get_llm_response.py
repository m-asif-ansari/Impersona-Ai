from langchain_groq import ChatGroq
from backend.logger.init_logger import init_logger

# Initialize the logger
logger = init_logger(__name__)


def get_llm_response(llm: ChatGroq, persona: str, prompt: list) -> str:
    """
    Function to get a response from the agent based on the provided prompt.

    Args:
        agent (create_react_agent): The initialized agent object capable of processing the prompt.
        prompt (str): The user input or query to be processed by the agent.

    Returns:
        str: The content of the agent's response.
    """
    logger.info(
        f"Getting response from LLM with persona: {persona} and prompt: {prompt}"
    )

    messages = [
        (
            "system",
            f"""You are an {persona} AI assistant. Your name is LUNA, you are helpful and knowledgeable. respond to the user in a friendly and professional manner.
            keep the conversation focused on the topic at hand and provide accurate information and brief responses.
            If the user asks a question that is not related to the topic, politely redirect them back to the topic.
            Your role is act as a {persona} and provide accurate and helpful responses to user behaving like a {persona}.
            **Do Not** answer any question which is not related to the persona- {persona}.""",
        ),
        ("human", str(prompt)),
    ]

    # Invoke the agent with the user prompt and retrieve the response
    response = llm.invoke(messages)

    logger.info(f"Response received from LLM: {response}")

    if "</think>" in response.content:
        # Handle the </think> tag in the response
        answer = str(response.content).split("</think>")[-1].strip()
    else:
        answer = str(response.content).strip()

    logger.info(f"This is the final response to the user: {answer}")
    # Return the content of the last message in the response
    return answer
