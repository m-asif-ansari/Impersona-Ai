from typing import Union
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

from backend.llm.init_llm import init_llm
from backend.llm.get_llm_response import get_llm_response
from backend.logger.init_logger import init_logger
from backend.llm_list.get_llm_list import get_llm_list

app = FastAPI()

class llm_payload(BaseModel):
    """
    Class to define the payload structure for LLM requests.
    """
    model_name: str
    persona: str
    prompt: Union[str, list]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Persona Chatbot!"}

@app.get("/health")
def read_health():
    """
    Health check endpoint to verify if the API is running.
    """
    return {"status": "ok"}

@app.get("/llm_list")
def fetch_llm_list() -> Union[list, dict]:
    """
    Function to get the list of available LLMs.

    Returns:
        list: A list of available LLM names.
    """
    return {'llm_list': get_llm_list()}

@app.post("/llm_response/")
def llm_response(payload: llm_payload) -> dict:
    """
    Endpoint to get a response from the LLM based on the provided model name, persona, and prompt.
    
    Args:
        model_name (str): The name of the LLM to be used.
        persona (str): The persona to be followed by the LLM.
        prompt (Union[str, list]): The user input or query to be processed by the LLM.
    
    Returns:
        dict: A dictionary containing the LLM's response.
    """
    llm = init_llm(payload.model_name)
    response = get_llm_response(llm, payload.persona, payload.prompt)
    return {"llm_response": response}