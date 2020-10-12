

class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    @classmethod
    def organize_event(cls):
        return 'hires an artist to perform for the people'
