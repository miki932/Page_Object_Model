import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Create a logger instance for use in other modules
logger = logging.getLogger(__name__)
