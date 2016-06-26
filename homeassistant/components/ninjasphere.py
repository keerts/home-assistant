"""
Support for NinjaSphere.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/ninjasphere/
"""
import logging

import homeassistant.components.light as light
import homeassistant.components.media_player as media_player
from homeassistant.components.light.ninjasphere import Light
from homeassistant.components.media_player.ninjasphere import MediaPlayer
from homeassistant.components.unidentified.unknownthing import UnknownThing

# The domain of this component. This one's
# equal to the name of this component.
DOMAIN = 'ninjasphere'

# List of component names (string)
# this component depends upon.
DEPENDENCIES = ['mqtt']

DEFAULT_TOPIC = 'home-assistant/ninjasphere'
DEFAULT_IP = '127.0.0.1'
DEFAULT_HTTP_PORT = '8000'

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Initialize NinjaSphere platform."""

    # TODO:Config validation
    # Read all required variables from the config
    ip = config[DOMAIN].get('ip', DEFAULT_IP)
    rest_port = config[DOMAIN].get('http_port', DEFAULT_HTTP_PORT)

    _LOGGER.debug('ip for component ' + DOMAIN + ' is: ' + ip)

    # Import pyninjasphere library
    from pyninjasphere.services import service

    # Create the node and get the things from it
    node = service.Service(ip, rest_port=rest_port, debug=False)
    things = node.get_all_things()

    parse_things(hass, things)

    # Return boolean to indicate that initialization was successfully.
    _LOGGER.debug('Setup for component ' + DOMAIN + ' successful!')
    return True


def parse_things(hass, things):
    """ Create lists for all different kinds of things. """
    lights = []
    media_players = []

    for thing in things:
        # Mediaplayer is found
        # if thing.type == 'mediaplayer':
            # media_players.append(MediaPlayer(thing))

        # Light is found
        if thing.type == 'light':
            lights.append(Light(thing))

        # An unknown thing has been found
        else:
            UnknownThing(hass, thing)

    # Create configs
    light_config = {'light': lights}
    media_player_config = {'media_player': media_players}

    # Run setups of things
    light.setup(hass, light_config)
    media_player.setup(hass, media_player_config)
