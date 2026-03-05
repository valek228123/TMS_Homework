
import csv
import pathlib
import json

BASA_PATH = pathlib.Path(__file__).resolve().parent
path_json = BASA_PATH / "city.list.json"

with open(path_json, "r", encoding="utf-8") as file:
    data = json.load(file)
print(type(data))

# 1 Определить количество городов в файле.
def task_2() -> None:
    print(len(data))
task_2()

# 2 Создать словарь, где ключ — это код страны, а значение — количество
# городов.
def task_2() -> None:
    dict_country = {}

    for city in data:
        if dict_country.get(city["country"]) == None and dict_country.get(city["country"]) != '':
            dict_country[city["country"]] = 1
        else:
            dict_country[city["country"]] += 1

    for country, count in dict(sorted(dict_country.items())).items():
        print(f"{country}: {count}")


# 3 Подсчитать количество городов в северном полушарии и в южном.
def task_3() -> None:
    dict_quantity = {"Южное полушарие": 0, "Северное полушарие": 0}

    for city in data:
        if city["coord"]["lat"] > 0:
            dict_quantity["Южное полушарие"] += 1
        elif city["coord"]["lat"] < 0:
            dict_quantity["Северное полушарие"] += 1

    print(dict_quantity)


# 4 Перевести в CSV файл данные по городам (координаты представить в виде
# строки значений через запятую).

def task_4() -> None:
    with open("city.list.csv", "w", encoding="utf-8", newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=data[0].keys(), quotechar='"')
        csv_writer.writeheader()
        csv_writer.writerows(data)


# 5 Создать другой JSON файл, в который сохранить только города одной
# выбранной страны.

def task_5() -> list[dict[str, int]]:
    new_dict_ru = []
    for city in data:
        if city["country"] == "RU":
            new_dict_ru.append(city)

    # print(new_dict_ru)

    with open("city.list.ru.json", "w", encoding="utf-8") as file:
        json.dump(new_dict_ru, file, indent=4, ensure_ascii=False)
    return new_dict_ru


# 6 Для каждой страны создать свой файл JSON с данными городов. Лучше
# создать отдельную папку в PyCharm, и указать путь к новому файлу с этой
# папкой.

def task_6_1() -> None:
    path_city = BASA_PATH / "country"

    for city in data:
        name_city = city["country"].replace("/", "-") + ".json"
        path_city_json = path_city / name_city
        if path_city_json.exists():
            with open(path_city_json, "r", encoding="utf-8") as file:
                city_data = json.load(file)
            city_data.append(city)
            with open(path_city_json, "w", encoding="utf-8") as file:
                json.dump(city_data, file, indent=4, ensure_ascii=False)
        else:
            with open(path_city_json, "w", encoding="utf-8") as file:
                json.dump([city], file, indent=4, ensure_ascii=False)

def task_6_2() -> None:
    path_city = BASA_PATH / "country"
    countrys = {}
    for city in data:
        if countrys.get(city["country"]) is None and city["country"] != " " :
            countrys[city["country"]] = [city]
        else:
            countrys[city["country"]].append(city)

    for country, citys in countrys.items():
        name_country = country.replace("/", "-") + ".json"
        path_city_json = path_city / name_country
        with open(path_city_json, "w", encoding="utf-8") as file:
            json.dump(citys, file, indent=4, ensure_ascii=False)


# 7. ** Дополнительное задание
def task_7() -> None:
    geo = {
        "type": "FeatureCollection",
        "features": [],
    }
    index = 0
    for item in task_5():
        geo_template = {
            "type": "Feature",
            "id": "",
            "geometry": {
                "type": "Point",
                "coordinates": [],
            },
            "properties": {
                "iconCaption": "",
                "marker-color": "#b51eff",
            },
        }
        if item["country"] == "RU" and index <= 100:
            geo_template["id"] = item["id"]
            # print(item["id"])
            # print(item["name"])
            geo_template["properties"]["iconCaption"] = item["name"]
            coords = [item["coord"]["lon"], item["coord"]["lat"]]
            geo_template["geometry"]["coordinates"] = coords
            geo["features"].append(geo_template)
            index += 1
            # print(geo_template)
            print()
            print(geo)
        if index > 100:
            break

    with open("city.geojson", "w", encoding="utf-8") as f:
        json.dump(geo, f, indent=4, ensure_ascii=False)



