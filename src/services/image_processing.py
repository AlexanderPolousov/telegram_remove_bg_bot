from rembg import new_session, remove


class ImageProcessor:
    """
    Класс для обработки изображений и удаления фона.
    Поддерживает multiple модели для разных типов изображений.
    """

    # Доступные модели
    AVAILABLE_MODELS: list[dict[str, str]] = [
        {
            "name": "u2net_human_seg",
            "description": "Специально для фотографий людей (рекомендуется)",
            "best_for": ["портреты", "селфи", "групповые фото"],
        },
        {
            "name": "u2net",
            "description": "Универсальная модель для любых объектов",
            "best_for": ["люди", "животные", "предметы"],
        },
        {
            "name": "isnet-general-use",
            "description": "Точная модель на основе ISNet",
            "best_for": ["люди", "высокая точность"],
        },
        {
            "name": "u2netp",
            "description": "Облегченная версия для быстрой обработки",
            "best_for": ["простые объекты", "скорость"],
        },
    ]

    def __init__(self, model_name: str = "u2net_human_seg"):
        """
        Инициализирует процессор с выбранной моделью.

        Args:
            model_name (str): Название модели из AVAILABLE_MODELS
        """
        self.model_name = model_name
        self.session = None
        self._initialize_session()

    def _initialize_session(self):
        """Инициализирует сессию нейросети с выбранной моделью"""
        try:
            self.session = new_session(self.model_name)
            print(f"✅ Сессия инициализирована с моделью: {self.model_name}")
        except Exception as e:
            print(f"❌ Ошибка инициализации модели {self.model_name}: {e}")
            # Fallback на модель по умолчанию
            self.session = new_session("u2net")
            self.model_name = "u2net"
            print("✅ Используется резервная модель: u2net")

    def get_available_models(self) -> list[dict[str, str]]:
        """Возвращает список доступных моделей"""
        return self.AVAILABLE_MODELS

    def get_model_info(self, model_name: str) -> dict[str, str]:
        """Возвращает информацию о конкретной модели"""
        for model in self.AVAILABLE_MODELS:
            if model["name"] == model_name:
                return model
        return {}

    def set_model(self, model_name: str) -> bool:
        """
        Переключает модель обработки.

        Args:
            model_name (str): Название новой модели

        Returns:
            bool: True если успешно, False если ошибка
        """
        if model_name == self.model_name:
            return True  # Уже установлена эта модель

        try:
            new_session_instance = new_session(model_name)
            self.session = new_session_instance
            self.model_name = model_name
            print(f"✅ Модель изменена на: {model_name}")
            return True
        except Exception as e:
            print(f"❌ Ошибка смены модели на {model_name}: {e}")
            return False

    async def remove_background(self, image_path: str, output_path: str) -> bool:
        """
        Удаляет фон с изображения используя текущую модель.

        Args:
            image_path (str): Путь к исходному изображению
            output_path (str): Путь для сохранения результата

        Returns:
            bool: True если успешно, False если ошибка
        """
        try:
            print(f"🔄 Обработка изображения моделью: {self.model_name}")

            with open(image_path, "rb") as input_file:
                image_bytes = input_file.read()
                output_bytes = remove(image_bytes, session=self.session)

                with open(output_path, "wb") as output_file:
                    output_file.write(output_bytes)

            print(f"✅ Фон удален успешно (модель: {self.model_name})")
            return True

        except Exception as e:
            print(f"❌ Ошибка обработки изображения моделью {self.model_name}: {e}")
            return False


# Создаем глобальный экземпляр с моделью по умолчанию
image_processor = ImageProcessor("u2net_human_seg")
