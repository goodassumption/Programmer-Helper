import importlib

from .utilits import get_modules_from_package

def choose_module():
    print('Для начала выберите модуль для запуска')
    package_name = 'modules'
    modules = get_modules_from_package(package_name)
    
    package_access_map = {}
    
    if not modules:
        print("Модули не найдены.")
        return package_access_map

    for i, module_name in enumerate(modules):
        module = importlib.import_module(module_name)
        try:
            # Импортируем модуль, чтобы получить доступ к его содержимому
            module = importlib.import_module(module_name)
            
            # Пытаемся получить значение переменной package_name из модуля
            extracted_package_name = getattr(module, 'package_name', None)
            
            display_name = f"{i} - {extracted_package_name}" if extracted_package_name else f"{i+1} - <package_name не найден>"
            if i != 0:
                print(display_name)
            
            # Сохраняем ссылку на модуль для последующего доступа
            # Используем полное имя модуля как ключ
            package_access_map[module_name] = module
            
        except ImportError:
            # Пропускаем, если модуль не удается импортировать (например, битые ссылки)
            print(f"{i} - Ошибка импорта модуля: {module_name}")
        except AttributeError:
            # Если переменной package_name нет в модуле
            print(f"{i} - <package_name не найден в модуле {module_name}>")
        except Exception as e:
            print(f"{i} - Непредвиденная ошибка при обработке {module_name}: {e}")

    try: del package_access_map['modules']
    except KeyError: pass
    print('0 - Выйти из приложения')
    packages = []
    for key in package_access_map.keys():
        packages.append(key)
    try: inp = int(input('Введите номер выбраного модуля: '))
    except TypeError: inp = 0
    if inp == 0 or inp > len(packages): return 'Вась, всё фигня, давай по новой'
    module = importlib.import_module(packages[inp-1])
    module.start()

if __name__ == '__main__':
    choose_module()