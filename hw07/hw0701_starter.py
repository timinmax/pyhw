import os


def create_structure(template, rootpath=None):
    if rootpath == "" or rootpath is None:
        rootpath = os.getcwd()
    if not os.path.exists(rootpath):
        print("Path does not exists: ", rootpath)
        return False
    for path in template:
        new_path = os.path.join(rootpath, path)
        if not os.path.exists(new_path):
            if template[path] is None:
                open(new_path, 'w', encoding='utf-8').close()
            else:
                os.mkdir(new_path)
                create_structure(template[path], new_path)
    return True


if __name__ == "__main__":
    test_struct1 = {
        'my_project': {'settings': {},
                      'mainapp': {},
                       'adminapp': {
                           'admin1': {
                               'admin11': {},
                               'admin12': {}
                           },
                           'admin2': {}
                       },
                       'authapp': {}}

    }
    create_structure(test_struct1)