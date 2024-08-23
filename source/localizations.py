import os
import json
from .logger import UCLogger, get_logger


class Localizations:
    """
    This class is responsible for loading localization resources from the disk.
    """

    def __init__(self, localizations_dir: str = "localizations"):
        self.logger: UCLogger = get_logger(self.__class__.__name__)
        self.dir: str = localizations_dir
        if not os.path.isdir(localizations_dir):
            msg = f"Directory '{localizations_dir}' not found."
            self.logger.error(msg)
            raise FileNotFoundError(msg)
        self.logger.info("Initialized.")
        self.data: dict = {}

    def load_all_localizations(self) -> None:
        """
        Load all localization files from the disk.
        """
        for file in os.listdir(self.dir):
            if file.endswith(".json"):
                language_code = file.split(".")[0]
                self.load_localization(language_code)

    def load_localization(self, language_code: str) -> dict:
        """
        Load a specific localization file.
        """
        localization_file = os.path.join(self.dir, f"{language_code}.json")
        if not os.path.isfile(localization_file):
            self.logger.error(f"Localization file not found: {localization_file}")
            return {}

        with open(localization_file, "r", encoding="utf-8", errors="ignore") as file:
            self.data[language_code] = json.load(file)

        self.logger.info(f"Loaded successfully: {language_code}")
        return self.data[language_code]

    def get_key(self, key: str, language_code: str) -> str:
        """
        Get a specific key from the localization data.
        Eg: get_key("planets", "es")
        """
        try:
            return self.data[language_code][key]
        except KeyError:
            self.logger.error(f"Key not found: {key}")
            return key
