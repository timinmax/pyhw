import yaml

test_struct1 = {
    'my_project': {'settings': {
        '__init__.py': None,
        'dev.py': None,
        'prod.py': None
    },
        'mainapp': {
            '__init__.py': None,
            'models.py': None,
            'views.py': None,
            'templates': {
                'mainapp': {
                    'base.html': None,
                    'index.html': None
                }
            }
        },
        'authapp': {
            '__init__.py': None,
            'models.py': None,
            'views.py': None,
            'templates': {
                'authapp': {
                    'base.html': None,
                    'index.html': None
                }
            }
        }}

}

with open("config.yaml", 'w', encoding='utf-8') as yaml_data:
    yaml.dump(test_struct1, yaml_data)
