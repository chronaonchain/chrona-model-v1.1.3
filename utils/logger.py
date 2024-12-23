# logger.py

import logging

class Logger:
    """Utility class for configuring and using a logger."""

    @staticmethod
    def get_logger(name: str, level: str = "INFO") -> logging.Logger:
        """
        Creates and returns a configured logger.
        
        Args:
            name (str): Name of the logger.
            level (str): Logging level (e.g., DEBUG, INFO, WARNING).
        
        Returns:
            logging.Logger: Configured logger instance.
        """
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # Avoid duplicate handlers
        if not logger.hasHandlers():
            logger.addHandler(ch)

        return logger

# Usage example:
# from logger import Logger
# logger = Logger.get_logger("Chrona", "DEBUG")
# logger.info("Logger is set up.")
