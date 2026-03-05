import pathlib
import datetime

base_dir_path_1 = pathlib.Path.cwd() / "work_with_files.py"
base_dir_path_2 = pathlib.Path(__file__).parent.resolve()
home_dir = pathlib.Path.home()


def cheack_path(path: pathlib.Path) -> str:
    text = str(path)
    if path.is_file():
        text += " | is a file"
    elif path.is_dir():
        text += " | is a directory"
    if path.is_absolute():
        text += " | is absolute"

    if path.exists():
        text += " | exists"
    else:
        text += " | does not exist"
    return text


print(cheack_path(base_dir_path_1))
print(cheack_path(base_dir_path_2))
print(cheack_path(home_dir))
print(base_dir_path_1 == base_dir_path_2)

print(base_dir_path_1.name)
print(base_dir_path_1.stem)
print(base_dir_path_1.suffix)
print(base_dir_path_1.parts)

print(base_dir_path_1.parents[2])

new_dir = base_dir_path_2 / "new_dir"
new_dir.mkdir(parents=True, exist_ok=True)

text = "Првиет ну как ты там вообще"
path_with_text = pathlib.Path(new_dir / "file.txt")
path_with_text.write_text(text, encoding="utf-8")

read_text = path_with_text.read_text(encoding="utf-8")
print(read_text)

if path_with_text.exists():
    path_with_text.unlink()

if new_dir.exists():
    new_dir.rmdir()

path_new = pathlib.Path(__file__).parent
# py_file_gen = path_new.rglob("*.py")
# for path in py_file_gen:
#     print(path)

for path in path_new.iterdir():
    if path.is_file():
        print(path)
print(path_new)
print(path_new.stat().st_mtime)
# / 216000


# Директория для поиска (например, домашняя)
search_dir = pathlib.Path("C:\Projects")

# 1. Используем rglob для рекурсивного поиска всех файлов
# 2. Фильтруем, оставляя только файлы (на случай, если попадется ссылка на директорию)
# 3. Создаем список кортежей (размер_файла, путь_к_файлу)
all_files = [
    (p.stat().st_size, p)
    for p in search_dir.rglob('*')
    if p.is_file()
]
# 4. Сортируем список по убыванию размера и берем первые 10
all_files.sort(key=lambda x: x[0], reverse=True)

print("Топ-10 самых больших файлов:")
for size, path in all_files[:10]:
    # Приводим размер к мегабайтам для читаемости
    print(f"  {path.name:-<40} | {size / 1024 / 1024:.2f} MB")

print(datetime.datetime.fromtimestamp(search_dir.stat().st_ctime))

# #Создайте объект Path для воображаемого пути 'project/src/utils/helpers.py'. Выведите на экран три строки:
# 1 Родительскую директорию этого файла.
# 2 Имя файла с расширением.
# 3 Только расширение файла.

some_path = pathlib.Path("project/src/utils/helpers.py")

print(some_path.parent)
print(some_path.name)
print(some_path.suffix)

# Напишите скрипт, который создает в текущей директории файл
# с именем info.txt и записывает в него строку "Pathlib is awesome!".
# Сразу после этого скрипт должен прочитать содержимое этого файла
# и вывести его в консоль. Все операции (запись и чтение) должны быть
# выполнены в одну строку каждая


path = pathlib.Path(__file__).resolve().parent
new_file = path / "info.txt"
text = "Pathlib is awesome!"
new_file.write_text(text, encoding="utf-8")
text = new_file.read_text(encoding="utf-8")
print(text)

# Напишите код,
# который создает в текущей директории
# вложенную структуру папок: data/raw/logs.
# Ваше решение должно работать в одну команду и не
# вызывать ошибку, если какая-либо из этих директорий уже существует.


path = pathlib.Path(__file__).resolve().parent
new_dir = path / "data" / "raw" / "logs"
new_dir.mkdir(parents=True, exist_ok=True)

# Представьте, что в вашей текущей директории есть файлы main.py,
# test_main.py, config.json и README.md. Напишите скрипт, который найдет
# и выведет имена всех файлов с расширением .py, находящихся только в
# этой директории (без рекурсивного поиска).

path = pathlib.Path(__file__).resolve().parent

for i in path.glob("*.py"):
    print(i.name)

# Сначала создайте
# несколько пустых файлов для теста: report-2025-01.txt, report-2025-02.txt
# и image.jpg. Напишите скрипт, который найдет все файлы,
# начинающиеся со слова report-, и добавит к их имени суффикс .old.
# В результате файлы должны быть переименованы в report-2025-01.txt
# и report-2025-02.txt

path = pathlib.Path(__file__).resolve().parent

for i in path.glob("report-*"):
    if i.is_file():
        i.rename(i.with_name(i.name + ".old"))
