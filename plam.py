class Dish:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = int(price)
        self.weight = int(weight)

    def __str__(self):
        return f"Dish: {self.name}, Категория: {self.category}, Стоимость: {self.price}, Вес: {self.weight}"
class Menu:
    def __init__(self, f="aaaa.txt"):
        self.filename = f
        self.menu_dict = self.read_menu_from_file(f)
        self.count = len(self.menu_dict)

    def appendDish(self, line):
        parts = line.strip().split(', ')
        if len(parts) == 4:
            name, category, price, weight = parts
            try:
                price = int(price)
                weight = int(weight)
                self.menu_dict[name] = Dish(name, category, price, weight)
                self.count += 1
                print(f"Блюдо '{name}' добавлено.")
            except ValueError:
                print(f"Некорректная стоимость или вес для блюда: {name}")
        else:
            print(f"Некорректная строка: {line.strip()}")
    def deleteDish(self, name):
        if name in self.menu_dict:
            del self.menu_dict[name]
            self.count -= 1
            print(f"Блюдо '{name}' удалено.")
        else:
            print(f"Блюда '{name}' нет в меню.")

    def updateDish(self, old_name, new_name, new_category, new_price, new_weight):
        if old_name in self.menu_dict:
            dish = self.menu_dict.pop(old_name)  
            dish.name = new_name
            dish.category = new_category
            dish.price = int(new_price)
            dish.weight = int(new_weight)
            self.menu_dict[new_name] = dish   
            print(f"Блюдо '{old_name}' обновлено.")
            return True
        else:
            print(f"Блюда '{old_name}' нет в меню.")
            return False
    def read_menu_from_file(self, filename):
        menu_dict = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) == 4:
                        name, category, price, weight = parts
                        try:
                            price = int(price)
                            weight = int(weight)
                            menu_dict[name] = Dish(name, category, price, weight)
                        except ValueError:
                            print(f"Некорректная стоимость или вес для блюда: {name}")
                    else:
                        print(f"Некорректная строка: {line.strip()}")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        return menu_dict

