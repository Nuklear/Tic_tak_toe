import os


class BaseSave(object):
    def __init__(self, path):
        self._path = path

    def make_path(self):
        if not os.path.exists(self._path):
            try:
                os.mkdir(self._path)
            except OSError as e:
                print("Creation of the directory {} failed\n{}".format(self._path, e))
                return False
        return True

    def save(self, data:dict):
        pass

    def prepare_data(self, data):
        pass
