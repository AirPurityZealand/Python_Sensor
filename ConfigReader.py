import configparser


def get_from_config(section_name, key_name, file_name='configfile.ini'):
    config_obj = configparser.ConfigParser()
    config_obj.read(file_name)
    section = config_obj[section_name]
    return section[key_name]