import os
import shutil
root_dir = "my_project"
templates_dir = os.path.join(root_dir, 'all_templates')


def get_templates(root_path, search='.html'):
    template_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if search in file:
                template_list.append(os.path.join(root, file))
    return template_list


def copy_templates(template_list, templates_dir):
    for template in template_list:
        new_folder = os.path.join(templates_dir, os.path.basename(os.path.dirname(template)))
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        dst_file = os.path.join(new_folder, os.path.basename(template))
        if not os.path.exists(dst_file):
            shutil.copy(template, dst_file)


if not os.path.exists(templates_dir):
    os.mkdir(templates_dir)

template_list = get_templates(root_dir)
copy_templates(template_list, templates_dir)
