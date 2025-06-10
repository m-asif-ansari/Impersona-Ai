import subprocess
import sys
import os

from backend.logger.init_logger import init_logger

# Initialize the logger
logger = init_logger(__name__)


def run_streamlit():
    logger.info("Running Streamlit...")
    return subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "streamlit_app.py"]
    )


def run_fastapi():
    logger.info("Running FastAPI...")
    return subprocess.Popen(
        [sys.executable, "-m", "fastapi", "run", "backend/api/main.py"]
    )


if __name__ == "__main__":
    try:
        print("Starting FastAPI backend...")
        fastapi_process = run_fastapi()

        print("Starting Streamlit frontend...")
        streamlit_process = run_streamlit()

        # Wait for both processes
        fastapi_process.wait()
        streamlit_process.wait()

    except (KeyboardInterrupt, Exception) as e:
        print("Shutting down due to error...")
        print("""
            Facing an issue while starting the application automatically. 
            Follow the instructions below to start the backend and frontend manually:
              
            Please start the backend first using:
            python -m fastapi run ChatBot/streamlit-app/backend/api/main.py
            
            then start the frontend using:
            python -m streamlit run ChatBot/streamlit-app/streamlit_app.py

            Please ensure that the backend is running before starting the frontend.
              """)
        logger.info(f"Terminating FastAPI and Streamlit processes due to error... {e} ")
        fastapi_process.terminate()
        streamlit_process.terminate()
