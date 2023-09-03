import helper as help

import os
print(os.name)

from os import name

from datetime import datetime, timezone
now = datetime.now()

import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")