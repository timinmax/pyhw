import hw0701_starter
import yaml

with open("config.yaml", 'r', encoding='utf-8') as yaml_data:
    config = yaml.load(yaml_data, Loader=yaml.Loader)
    hw0701_starter.create_structure(config)