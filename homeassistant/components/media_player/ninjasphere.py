class MediaPlayer(dict):
    """ Class for creating a MediaPlayer from a mediaplayer-thing. """

    def __init__(self, thing):
        self.parse_mediaplayer_from_thing(thing)

    def add_field(self, key, item):
        self.__setitem__(key, item)

    def parse_mediaplayer_from_thing(self, thing):
        self.add_field('platform', 'cast')
