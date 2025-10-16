#1
n=input()
if len(n)<8:
    print("Слищком короткий пароль")
else:
    print("Пароль принят")

#2
status=input()
if status=="online":
    print("Связь установлена")
else:
    print("Связь потеряна")

#3
n=int(input())
if 1<=n<=30:
    print("Низкий уровень угрозы")
elif 31<=n<=70:
    print("Средний уровень угрозы")
elif 71<=n<=100:
    print("Критический уровень угрозы")
else:
    print("Ошибка ввода")

#4
checksum_original=input()
checksum_current=input()
status="Файл не изменён" if checksum_original==checksum_current else "Файл повреждён"
print(status)

#5
event_code = input()
match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")