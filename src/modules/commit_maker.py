from src import request
from src.utilits import models

package_name = 'Конвертер коммитов в Conventional стиль'

def start():
    text = input('Введите текст коммита: ')
    systemPrompt = 'Преобразуй следующий текст в формат Conventional Commits.\n**Условия:**\n\n1.  Заголовок (Header): английский язык.\n2.  Тело коммита (Body): английский и русский языки.\n3.  Если заголовок описывает незначительное изменение (например, исправление опечатки, небольшая ошибка), тело коммита должно быть опущено.\n\n**Входной текст:**'
    
    request_ = {
        "text": text,
        "modelName": models['ge-2.5-p'],
        "systemPrompt": systemPrompt,
    }
    request.make_request(data=request_)

if __name__ == '__main__':
    start()