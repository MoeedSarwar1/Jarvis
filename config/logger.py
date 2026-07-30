from loguru import logger

logger.add(
    "logs/shinkai.log",
    rotation="10 MB",
    retention="10 days",
)

logger.info("Logger ready.")
