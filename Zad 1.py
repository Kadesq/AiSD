import os
import glob
import shutil

def main():
    source_dir = 'zadanie1'

    files = glob.glob(os.path.join(source_dir, '*'))

    for file in files:
        if os.path.isfile(file):
            file_name = os.path.basename(file)
            first_letter = file_name[0].upper()

            try:
                os.mkdir(os.path.join(source_dir, first_letter))
            except FileExistsError:
                pass

            new_path = os.path.join(source_dir, first_letter, file_name)

            try:
                shutil.move(file, new_path)
                print(f'Plik {file_name} został przeniesiony do katalogu {first_letter}')
            except Exception as e:
                print(f'Błąd przy przenoszeniu pliku {file_name}: {e}')

if __name__ == '__main__':
    main()
