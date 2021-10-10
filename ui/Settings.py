class Settings:
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self.file_name

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    def get_attributes(self):
        f = open(self._file_name, 'r')
        line = f.readline()
        tokens = line.strip().split(' ')
        dim = tokens[1]

        line = f.readline()
        tokens = line.strip().split(' ')
        apple_count = tokens[1]

        f.close()
        return [dim, apple_count]