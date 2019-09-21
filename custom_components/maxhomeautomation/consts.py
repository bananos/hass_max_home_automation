from homeassistant.components.climate.const import (
    HVAC_MODE_AUTO, HVAC_MODE_HEAT_COOL, HVAC_MODE_HEAT, HVAC_MODE_OFF
    )
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_SCAN_INTERVAL

# version for pyupdate
VERSION='0.0.5'

# PLATFORM CONSTS
DOMAIN = 'maxhomeautomation'
DATA_KEY = 'maxhomeautomation'

#SCHEMA
CONF_GATEWAYS = 'gateways'
CONF_CUBES = 'cubes'
CONF_HEX_ADDRESS = 'hex_address'
CONF_NAME = 'name'
CONF_RADIATOR_THERMOSTATS = 'radiator_thermostats'
CONF_WALL_THERMOSTATS = 'wall_thermostats'
CONF_WINDOWS_SHUTTERS = 'window_shutters'
CONF_ECO_BUTTONS = 'eco_buttons'

#API_CONSTS
MHA_API_DEVICES = 'devices'
MHA_API_ADDRESS = 'address'
MHA_API_NAME = 'name'
MHA_API_TYPE = 'type'
MHA_API_TEMPERATURE = 'temperature'
MHA_API_SET_TEMPERATURE = 'set_temperature'
MHA_API_MODE = 'mode'
MHA_API_VALVE = 'valve'
MHA_API_OFFSET = 'offset'
MHA_API_ERROR = 'error'
MHA_API_INITIALIZED = 'initialized'
MHA_API_BATTERY = 'battery_low'
MHA_API_PANEL_LOCKED = 'panel_locked'
MHA_API_LINK_ERROR = 'link_error'
MHA_API_OPEN = 'open'

MHA_API_RADIATOR_THERMOSTAT = 'radiator thermostat'
MHA_API_WALL_THERMOSTAT = 'wall thermostat'
MHA_API_SHUTTER_CONTACT = 'shutter contact'
MHA_API_ECO_BUTTON = 'eco button'

MHA_STATE_AUTOMATIC = 'automatic'
MHA_STATE_MANUAL = 'manual'
MHA_STATE_BOOST = 'boost'
MHA_STATE_VACATION = 'vacation'

MAP_MHA_HVAC_MODE_HASS = {
    MHA_STATE_AUTOMATIC: HVAC_MODE_AUTO,
    MHA_STATE_MANUAL: HVAC_MODE_HEAT_COOL,
    MHA_STATE_BOOST: HVAC_MODE_HEAT,
    MHA_STATE_VACATION: HVAC_MODE_OFF,
    }

# sensor type constants
MHA_SENSOR_TYPE_TEMPERATURE = MHA_API_TEMPERATURE
MHA_SENSOR_TYPE_SET_TEMPERATURE = MHA_API_SET_TEMPERATURE
MHA_SENSOR_TYPE_VALVE = MHA_API_VALVE
MHA_SENSOR_TYPE_OFFSET = MHA_API_OFFSET
MHA_SENSOR_TYPE_ECO_BUTTON = MHA_API_MODE
MHA_SENSOR_TYPE_DUTY = 'duty'
# binary sensor type constants
MHA_SENSOR_TYPE_ERROR = MHA_API_ERROR
MHA_SENSOR_TYPE_INITIALIZED = MHA_API_INITIALIZED
MHA_SENSOR_TYPE_BATTERY = MHA_API_BATTERY
MHA_SENSOR_TYPE_PANEL_LOCKED = MHA_API_PANEL_LOCKED
MHA_SENSOR_TYPE_LINK_ERROR = MHA_API_LINK_ERROR
MHA_SENSOR_TYPE_SHUTTER_CONTACT = MHA_API_OPEN
