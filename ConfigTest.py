import configparser

config = configparser.ConfigParser()

config.add_section('rest_connection')
config.set('rest_connection', 'rest_url', 'https://airpurityzealand.azurewebsites.net')

config.add_section('sensor_local')
config.set('sensor_local', 'room_id', 'TR1')

with open (r'configfile.ini', 'w') as configfile:
    config.write(configfile)