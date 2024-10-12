import sys
from loguru import logger


logger.remove()
logger.add(sink = sys.stdout, format = "<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                       " | <level>{level: <8}</level>"
                                       " | <cyan><b>{file}</b>:{line}</cyan>"
                                       " - <white><b>{message}</b></white>")
logger.add("logs/npx.log", mode = "w", format = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {file}:{line} - {message}")
logger = logger.opt(colors = True)
