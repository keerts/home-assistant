class UnknownThing:

    def __init__(self, hass, thing):
        hass.states.set('unknown.' + thing.type + '_' +
                        self.get_qualified_name(thing), thing.name)

    def get_qualified_name(self, thing):
        return thing.name.replace(' ', '_').replace('.', '')\
            .replace('-', '').replace('\\', '').lower()
