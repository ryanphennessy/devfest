import yaml


def read_property(key):
		with open('pulse/config.yaml', 'r') as config_file:
			config = yaml.load(config_file)
		return config[key]