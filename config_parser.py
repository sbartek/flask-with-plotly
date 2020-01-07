import yaml

DEFAULT_CONFIG_FN = "default_config.yaml"

def parse_config(config_fn):
    with open(config_fn) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def parse_default_config(additional_config_fn=None):
    config = parse_config(DEFAULT_CONFIG_FN)
    if (additional_config_fn is not None) and (additional_config_fn != DEFAULT_CONFIG_FN):
        additional_config = parse_config(additional_config_fn)
        config = dict(config, **additional_config)
    return config
