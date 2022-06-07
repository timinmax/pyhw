import hw06_34_zip_files
import sys

if len(sys.argv) != 4:
    print("insufficient parameters")
    exit(2)

users_path = sys.argv[1]
hobby_path = sys.argv[2]
output_folder = sys.argv[3]

hw06_34_zip_files.zip_files(users_path, hobby_path, output_folder)

# python .\hw06_5_zipfiles_cli.py .\sourcecsv\users.csv .\sourcecsv\hobby.csv .\outputcsv\
