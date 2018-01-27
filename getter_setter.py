class Song:
    def __init__(self, title, album, release_date=None):
        self.title = title
        self.album = album
        self._release_date = release_date

    @property
    def info(self):
        return f'{self.album} | {self.title}'

    @info.setter
    def info(self, args):
        if len(args) != 2:
            raise ValueError
        title, album = args
        self.title = title
        self.album = album

    @property
    def release_date(self)
        return f''