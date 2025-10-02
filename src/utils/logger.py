import logging
import sys


class ColorFormatter(logging.Formatter):
    """Кастомный форматтер с цветами для логов"""

    # Цвета для разных уровней логирования
    COLOR = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[41m",  # Red background
        "RESET": "\033[0m",  # Reset color
    }

    def format(self, record):
        # Добавляем цвет к уровню логирования
        levelname = record.levelname
        if levelname in self.COLOR:
            record.levelname = (
                f"{self.COLOR[levelname]}{levelname}{self.COLOR['RESET']}"
            )

        # Выделяем сообщение жирным шрифтом
        record.msg = f"\033[1m{record.msg}\033[0m"

        return super().format(record)


def setup_logging():
    """Настройка логирования с цветами"""

    # Создаем форматтер с цветами
    formatter = ColorFormatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Настраиваем хендлер для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Настраиваем корневой логгер
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Удаляем существующие хендлеры
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Добавляем наш цветной хендлер
    root_logger.addHandler(console_handler)

    # Для aiogram устанавливаем тот же уровень
    logging.getLogger("aiogram").setLevel(logging.INFO)
