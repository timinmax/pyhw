import json
import os


def zip_files(users_path, hobby_path, output_folder):
    user_hobby_json_full_path = os.path.join(output_folder, "user_hobby_full.json")
    user_hobby_json_rows_path = os.path.join(output_folder, "user_hobby_rows.json")

    if not os.path.exists(users_path) or not os.path.exists(hobby_path) or not os.path.exists(output_folder):
        print("wrong parameters")
        exit(3)

    user_hobbies = {}
    with open(users_path, "r", encoding='utf-8') as users_csv, open(hobby_path, "r", encoding='utf-8') as hobby_csv, \
            open(user_hobby_json_full_path, 'w', encoding='utf-8') as user_hobby_json_full, \
            open(user_hobby_json_rows_path, 'w', encoding='utf-8') as user_hobby_json_rows:
        users_rec_count = sum(1 for line in users_csv)
        hobby_rec_count = sum(1 for line in hobby_csv)
        if hobby_rec_count > users_rec_count:
            exit(1)
        users_csv.seek(0)
        hobby_csv.seek(0)
        for user in users_csv:
            hobby = hobby_csv.readline().strip()
            cred_key = user.strip().lower().replace(',', ' ')
            user_hobbies.setdefault(cred_key, [])
            record_to_append = {'credentials': user.strip().split(','),
                                'hobby': None if hobby == "" else hobby.split(",")}
            user_hobbies[cred_key].append(record_to_append)
            # задача 4 - случай, когда файлы-исходники большие: сбрасываем строку json сразу в файл.
            # формат файла: каждая строка - отдельный json
            user_hobby_json_rows.write(f'{json.dumps(record_to_append)}\n')

        # задача 3 - случай, когда файлы-исходники маленькие: можно собрать словарь и после целиком записать
        json.dump(user_hobbies, user_hobby_json_full)


if __name__ == "__main__":
    zip_files(os.path.join("sourcecsv", "users.csv"), os.path.join("sourcecsv", "hobby.csv"), "outputcsv")