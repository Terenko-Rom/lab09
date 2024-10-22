regions = {
    'Київська область': 28131,
    'Полтавська область': 28800,
    'Закарпатська область': 12777,
    'Львівська область': 21833,
    'Житомирська область': 29832
}
def add_region(name, area):
    regions[name] = area
    def find_area_by_name(name):
        return regions.get(name, "Область не знайдена")
    def delete_region(name):
        if name in regions:
            del regions[name]
        else:
            print(f"Область '{name}' не знайдена")
add_region('Харківська область', 31428)
print(f"Площа Харківської області: {find_area_by_name('Харківська область')} км**2")
delete_region('Житомирська область')
print(f"Словник після видалення: {regions}")