# Task_2
Поиск маршрута движения автомобиля

## Инструкция по установке
Если у Вас не установлен Python 3.3 и выше, то необходимо его установить(https://www.python.org/downloads/). При установке обязательно выберите компоненты pip и tcl/tk IDLE.

Клонируйте репозиторий:

```
git clone https://github.com/Platypus98/Task_2.git
cd Task_2
```

Проверьте, установлен ли у Вас tkinter. Если при вводе команд открылось маленькое окошко, то значит, что он у Вас установлен. Если же нет - необходимо переустановить или модифицировать Python(https://www.python.org/downloads/), добавив компонент tcl/tk IDLE.

```
python
import tkinter
tkinter._test()
```

Закройте окошко и введите команду:

```
exit()
```

Создайте виртуальное окружение в папке venv:

```
python -m venv venv
```

Активируйте виртуальное окружение.

Для Windows:

```
venv\Scripts\activate
```
Для Linux:
```
. venv/bin/activate
```

Установите требуемые пакеты для python:

```
pip install -r requirements.txt
```

Запустите файл Task_2.py с помощью Python:

```
python Task_2.py
```

#### Готово!
