from datetime import datetime
import logging
import os
from pathlib import Path

LOG_DIR = Path(os.getenv("chemprop2_LOG_DIR", "chemprop2_logs"))
LOG_LEVELS = {0: logging.INFO, 1: logging.DEBUG, -1: logging.WARNING, -2: logging.ERROR}
NOW = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
chemprop2_TRAIN_DIR = Path(os.getenv("chemprop2_TRAIN_DIR", "chemprop2_training"))
