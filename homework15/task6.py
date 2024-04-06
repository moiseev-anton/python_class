"""
Задание №6
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
 Соберите информацию о содержимом в виде объектов namedtuple.
 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
 (Логирование выполнено в задаче с банкоматом)
"""


import argparse
from collections import namedtuple
from pathlib import Path

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_directory_content(directory_path: str) -> list[FileInfo]:
    """
    Функция получает информацию о содержимом директории и возвращает список элементов FileInfo.
    """
    directory = Path(directory_path)
    content_info = []

    for item in directory.iterdir():
        # получаем имя без расширения
        name = item.stem
        # получаем расширение (если файл)
        extension = item.suffix if item.is_file() else None
        # флаг если каталог
        is_directory = item.is_dir()
        # получаем названия родительского каталога
        parent_directory = directory.name

        # создаем namedtuple
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        content_info.append(file_info)

    return content_info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Информация о содержимом директории')
    parser.add_argument('-p','--path', type=str, help='Путь к директории')
    args = parser.parse_args()

    # получение информации о содержимом директории
    directory_content = get_directory_content(args.path)

    # вывод содержимого
    for item in directory_content:
        if item.is_directory:
            print(f"Каталог:  {item.name}, Родительский каталог: {item.parent_directory}")
        else:
            print(f"Файл:  {item.name}{item.extension}, Родительский каталог: {item.parent_directory}")