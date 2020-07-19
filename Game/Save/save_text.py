from Game.Base.base_save import BaseSave
from Game.const import DATA_FILE_NAME_JSON


class SaveText(BaseSave):
    def __init__(self, path):
        super().__init__(path)

    def save(self, data: dict):
        if self.make_path():
            with open(DATA_FILE_NAME_JSON, "w") as file:
                file.write(self.prepare_data(data))

    def prepare_data(self, data: dict):
        return str(data)
