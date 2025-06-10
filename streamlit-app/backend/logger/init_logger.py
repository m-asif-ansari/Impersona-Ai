import logging


def init_logger(current_file) -> logging.Logger:
    """
    Function to initialize the logger for the application.

    Returns:
        logger (logging.Logger): Configured logger instance.
    """
    # Create a logger with the specified name
    logger = logging.getLogger(current_file)
    logging.basicConfig(
        filename="ChatBot.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger.setLevel(logging.INFO)
    return logger


if __name__ == "__main__":
    # Initialize the logger when the script is run directly
    logger = init_logger(__name__)
    logger.info("Logger initialized successfully.")
    print("Logger initialized successfully.")
