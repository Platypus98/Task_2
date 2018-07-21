#Для определения координат используется бибилиотека geopy
#Установка модуля requests, pyttk
import requests
import webbrowser
from  tkinter import *
import ttk
from tkinter import messagebox
from geopy.geocoders import Nominatim

def coordinates():
    coordinates = ""
    try:

        if pos_1_entry.get() != "":
                location = geolocator.geocode(pos_1_entry.get())
                coordinates += "Пункт отправления: " + pos_1_entry.get() + "- ({0}, {1})".format(location.latitude, location.longitude) + "\n"

        if pos_2_entry.get() != "":
                location = geolocator.geocode(pos_2_entry.get())
                coordinates += "Промежуточный пункт 1: " + pos_2_entry.get() + "- ({0}, {1})".format(location.latitude, location.longitude) + "\n"

        if pos_3_entry.get() != "":
                location = geolocator.geocode(pos_3_entry.get())
                coordinates += "Промежуточный пункт 2: " + pos_3_entry.get() + "- ({0}, {1})".format(location.latitude, location.longitude) + "\n"

        if pos_4_entry.get() != "":
                location = geolocator.geocode(pos_4_entry.get())
                coordinates += "Пункт назначения: " + pos_4_entry.get() + "- ({0}, {1})".format(location.latitude, location.longitude) + "\n"

        if coordinates == "":
            coordinates = "Не введены точки маршрута"

    except AttributeError as ae:
        messagebox.showerror("Координаты", "Неправильно указан адрес одиного из пунктов")
        return

    messagebox.showinfo("Координаты", coordinates)


def distance():
    distance = ""
    coordinates = ""
    try:
        if pos_1_entry.get() != "":
                location = geolocator.geocode(pos_1_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)
        else:
            messagebox.showerror("Дистанция", "Не введен пункт отправления")
            return

        if pos_2_entry.get() != "":
                location = geolocator.geocode(pos_2_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)


        if pos_3_entry.get() != "":
                location = geolocator.geocode(pos_3_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)

        if pos_4_entry.get() != "":
                location = geolocator.geocode(pos_4_entry.get())
                coordinates += "{0},{1}".format(location.longitude, location.latitude)
        else:
            messagebox.showerror("Дистанция", "Не введен пункт назначения")
            return
    except AttributeError as ae:
        messagebox.showerror("Дистанция", "Неправильно указан адрес одиного из пунктов")
        return


    try:
        r = requests.get('http://router.project-osrm.org/route/v1/car/{0}?alternatives=false&overview=false'.format(coordinates),  headers = {'User-agent': 'your bot 0.1'})
        а = r.json()['routes']
    except Exception as e:
        messagebox.showerror("Дистанция", "Ошибка подключения к серверу. Слишком много запросов или адрес введен неточно. Попробуйте позже" )
        return

    if len(r.json()['routes'][0]['legs']) == 1:
        distance = float(r.json()['routes'][0]['legs'][0]['distance'])/1000
    elif len(r.json()['routes'][0]['legs']) == 2:
        distance = (float(r.json()['routes'][0]['legs'][0]['distance']) + float(r.json()['routes'][0]['legs'][1]['distance']))/1000
    elif len(r.json()['routes'][0]['legs']) == 3:
        distance = (float(r.json()['routes'][0]['legs'][0]['distance']) + float(r.json()['routes'][0]['legs'][1]['distance']) + float(r.json()['routes'][0]['legs'][2]['distance']))/1000

    distance = round(distance, 3)
    messagebox.showinfo("Дистанция", "Дистанция на маршруте: ~ " + str(distance) + "  км.")


def duration():
    duration = ""
    coordinates = ""
    try:

        if pos_1_entry.get() != "":
                location = geolocator.geocode(pos_1_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)
        else:
            messagebox.showerror("Время в пути", "Не введен пункт отправления")
            return

        if pos_2_entry.get() != "":
                location = geolocator.geocode(pos_2_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)

        if pos_3_entry.get() != "":
                location = geolocator.geocode(pos_3_entry.get())
                coordinates += "{0},{1};".format(location.longitude, location.latitude)

        if pos_4_entry.get() != "":
                location = geolocator.geocode(pos_4_entry.get())
                coordinates += "{0},{1}".format(location.longitude, location.latitude)
        else:
            messagebox.showerror("Время в пути", "Не введен пункт назначения")
            return

    except AttributeError as ae:
        messagebox.showerror("Время в пути", "Неправильно указан адрес одиного из пунктов")
        return

    try:
        r = requests.get('http://router.project-osrm.org/route/v1/car/{0}?alternatives=false&overview=false'.format(coordinates),  headers = {'User-agent': 'your bot 0.1'})
        а = r.json()['routes']
    except Exception as e:
        messagebox.showerror("Время в пути", "Ошибка подключения к серверу. Слишком много запросов или адрес введен неточно. Попробуйте позже" )
        return

    if len(r.json()['routes'][0]['legs']) == 1:
        duration = float(r.json()['routes'][0]['legs'][0]['duration'])/60
    elif len(r.json()['routes'][0]['legs']) == 2:
        duration = (float(r.json()['routes'][0]['legs'][0]['duration']) + float(r.json()['routes'][0]['legs'][1]['duration']))/60
    elif len(r.json()['routes'][0]['legs']) == 3:
        duration = (float(r.json()['routes'][0]['legs'][0]['duration']) + float(r.json()['routes'][0]['legs'][1]['duration']) + float(r.json()['routes'][0]['legs'][2]['duration']))/60

    if duration < 60:
        duration = round(duration, 1)
        messagebox.showinfo("Время в пути", "Время в пути: ~ " + str(duration) + "  мин.")
    else:
        duration = duration/60
        duration = round(duration, 1)
        messagebox.showinfo("Время в пути", "Время в пути: ~ " + str(duration) + "  час.")


def map():
    coordinates = ""
    try:
        if pos_1_entry.get() != "":
                location = geolocator.geocode(pos_1_entry.get())
                coordinates += "ll={0}%2C{1}&z=10&mode=routes&rtext={2}%2C{3}~".format(location.longitude, location.latitude, location.latitude, location.longitude)

        if pos_2_entry.get() != "":
                location = geolocator.geocode(pos_2_entry.get())
                coordinates += "{0}%2C{1}~".format(location.latitude, location.longitude)

        if pos_3_entry.get() != "":
                location = geolocator.geocode(pos_3_entry.get())
                coordinates += "{0}%2C{1}~".format(location.latitude, location.longitude)

        if pos_4_entry.get() != "":
                location = geolocator.geocode(pos_4_entry.get())
                coordinates += "{0}%2C{1}".format(location.latitude, location.longitude)

        if coordinates == "":
            coordinates = "Не введены точки маршрута"
            messagebox.showerror("Карта", coordinates)
            return

    except AttributeError as ae:
        messagebox.showerror("Карта", "Неправильно указан адрес одиного из пунктов")
        return

    webbrowser.open("https://yandex.ru/maps/?{0}&rtt=auto".format(coordinates))


def map_osrm():
    coordinates = ""
    try:
        if pos_1_entry.get() != "":
                location = geolocator.geocode(pos_1_entry.get())
                coordinates += "center={0}%2C{1}&loc={2}%2C{3}".format(location.latitude, location.longitude, location.latitude, location.longitude)

        if pos_2_entry.get() != "":
                location = geolocator.geocode(pos_2_entry.get())
                coordinates += "&loc={0}%2C{1}".format(location.latitude, location.longitude)

        if pos_3_entry.get() != "":
                location = geolocator.geocode(pos_3_entry.get())
                coordinates += "$loc={0}%2C{1}".format(location.latitude, location.longitude)

        if pos_4_entry.get() != "":
                location = geolocator.geocode(pos_4_entry.get())
                coordinates += "&loc={0}%2C{1}".format(location.latitude, location.longitude)

        if coordinates == "":
            coordinates = "Не введены точки маршрута"
            messagebox.showerror("Карта", coordinates)
            return

    except AttributeError as ae:
        messagebox.showerror("Карта", "Неправильно указан адрес одиного из пунктов")
        return

    webbrowser.open("http://map.project-osrm.org/?z=11&{0}&hl=en&alt=0".format(coordinates))



geolocator = Nominatim()
root = Tk()
root.geometry("660x400+300+250")
root.title("Поиск маршрута движения автомобиля")

ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

#Заголовки и поля ввода
pos_1 = ttk.Label(root, text = "Пункт отправления:", font = "Helvetica 12 bold")
pos_1_entry = ttk.Entry(root, width = 30, font = "Helvetica 11")
pos_2 = ttk.Label(root, text = "Промежуточный пункт 1:", font = "Helvetica 12 bold")
pos_2_entry = ttk.Entry(root, width = 30, font = "Helvetica 11")
pos_3 = ttk.Label(root, text = "Промежуточный пункт 2:", font = "Helvetica 12 bold")
pos_3_entry = ttk.Entry(root, width = 30, font = "Helvetica 11")
pos_4 = Label(root, text = "Пункт назначения:", font = "Helvetica 12 bold")
pos_4_entry = ttk.Entry(root, width = 30, font = "Helvetica 11")
prim = Label(root, text = "*При частых запросах на OSRM не всегда рисуется линия между точками, поэтому я добавил еще Яндекс.Карты", font = "Helvetica 9")


#Кнопки
button_coordinate = ttk.Button(root, width = 15, text = "Координаты", command=coordinates)
button_distance = ttk.Button(root, width = 15, text = "Дистанция", command = distance)
button_duration = ttk.Button(root, width = 15, text = "Время в пути", command = duration)
button_map = ttk.Button(root, width = 30, text = "Показать на Яндекс.Карты*", command = map)
button_map_1 = ttk.Button(root, width = 20, text = "Показать на OSRM", command = map_osrm)


pos_1.place(x = "10", y = "20")
pos_1_entry.place(x = "230", y = "20")

pos_2.place(x = "10", y = "70")
pos_2_entry.place(x = "230", y = "70")

pos_3.place(x = "10", y = "120")
pos_3_entry.place(x = "230", y = "120")

pos_4.place(x = "10", y = "170")
pos_4_entry.place(x = "230", y = "170")

prim.place(x = "10", y = "330")

button_coordinate.place(x = "10", y = "220")
button_distance.place(x = "140", y = "220")
button_duration.place(x = "270", y = "220")
button_map.place(x = "10", y = "280")
button_map_1.place(x = "230", y = "280")


root.mainloop()
