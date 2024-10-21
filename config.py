import configparser

def create_config(config_file):
    """
    Creates a configuration file with user-provided API key.
    This function prompts the user to enter their API key, then writes this key
    to a configuration file specified by the `config_file` parameter.
    Args:
        config_file (str): The path to the configuration file to be created.
    Returns:
        None
    """
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'api_key': input('Enter your API key: ')}
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['DEFAULT']['api_key']