"""
Support for TTS on a Bluetooth Speaker

"""
import voluptuous as vol

from homeassistant.components.media_player import (
    SUPPORT_PLAY_MEDIA,
    PLATFORM_SCHEMA,
    MediaPlayerDevice)
from homeassistant.const import (
    CONF_NAME, STATE_OFF, STATE_PLAYING)
import homeassistant.helpers.config_validation as cv

import subprocess 

import logging

DEFAULT_NAME = 'Bluetooth Speaker'

# This is the path where the script is located
SCRIPT_DIR = '/volume1/@appstore/HomeAssistant/config/programs/'

# This is the name of the script
SCRIPT_NAME = SCRIPT_DIR + 'play_url_bluetooth.sh' 

SUPPORT_BLU_SPEAKER = SUPPORT_PLAY_MEDIA 

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Bluetooth Speaker platform."""
    name = config.get(CONF_NAME)

    add_devices([BluetoothSpeakerDevice(name)])
    return True

class BluetoothSpeakerDevice(MediaPlayerDevice):
    """Representation of a Bluetooth Speaker on the network."""

    def __init__(self, name):
        """Initialize the device."""
        self._name = name
        self._is_standby = True
        self._current = None
        
    def update(self):
        """Retrieve latest state."""
        if self._is_standby:
            self._current = None
        else:
            self._current = True

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    # MediaPlayerDevice properties and methods
    @property
    def state(self):
        """Return the state of the device."""
        if self._is_standby:
            return STATE_OFF
        else:
            return STATE_PLAYING

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_BLU_SPEAKER

    def play_media(self, media_type, media_id, **kwargs):
        """Send play commmand."""
        _LOGGER.info('play_media: %s',media_id)
        self._is_standby = False
        subprocess.call(SCRIPT_NAME + ' ' + media_id, shell=True) 
        self._is_standby = True
