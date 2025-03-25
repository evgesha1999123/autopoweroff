import os
import time
import tkinter
import customtkinter as ctk
from tkinter import messagebox as mb
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageTk
from CTkSpinbox import *

def call_accept_window(dialog_text, converted_seconds, need_to_cancel_previous_command):
    res=mb.askquestion('Требуется подтверждение', dialog_text)
    if res == 'yes' :
        if need_to_cancel_previous_command == False:
            os.system(f'shutdown /s /t {converted_seconds}')
        else:
            os.system('shutdown /a')
    else :
        mb.showinfo('Информация', 'ОПЕРАЦИЯ ОТМЕНЕНА!')


def convert_to_seconds(hours, minutes, seconds):
    converted_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds) 
    if converted_seconds < 60 : 
        return 60, True
    else:
        return converted_seconds, False

def validate_user_data(val1, val2, val3):
    if val1 == None or val1 == '' : val1 = 0
    if val2 == None or val2 == '' : val2 = 0
    if val3 == None or val3 == '' : val3 = 0
    try:
        if int(val1).is_integer() and int(val2).is_integer() and int(val3).is_integer() == True : 
            return True, val1, val2, val3
        else : return False, val1, val2, val3
    except:
        return False, val1, val2, val3

def on_button_accept_click_event():
    hours_value = entry_hours.get()
    minutes_value = entry_minutes.get()
    seconds_value = entry_seconds.get()

    is_valid, hours_value, minutes_value, seconds_value = validate_user_data(hours_value, minutes_value, seconds_value)

    print(f'{hours_value}:{minutes_value}:{seconds_value}')
    
    if is_valid == True:
        converted_seconds, is_defence_triggered = convert_to_seconds(hours_value, minutes_value, seconds_value)
        print(f'Converted_seconds = {converted_seconds}')

        common_dialog_text = f'Компьютер будет выключен через {hours_value} : {minutes_value} : {seconds_value}'
        
        if is_defence_triggered == False : call_accept_window(common_dialog_text, converted_seconds, False)
        else : call_accept_window('Ваш комьютер выключится через минуту', converted_seconds, False)
    else:
        mb.showerror('Ошибка ввода', 'Введите время в корректном формате!')

def on_button_cancel_click_event():
    call_accept_window('Хотите отменить отключение?', 0, True)


# def quit_window(icon, item):
#     icon.stop()
#     root.destroy()

# def show_window(icon, item):
#     icon.stop()
#     root.after(0, root.deiconify)

# def withdraw_window(root, icon):    
#     root.withdraw()
#     icon = pystray.Icon("MGMT", image, menu = pystray.Menu(
#             pystray.MenuItem("Развернуть", show_window),
#             pystray.MenuItem("Выйти", quit_window)
                        
#     ))
#     icon.run()


#image = Image.open('icon.ico')

root = ctk.CTk()
root.geometry('400x200')
root.resizable(width = False, height = False)
#root.protocol("WM_DELETE_WINDOW", lambda : withdraw_window(root, image))
root.title('Poweroff manager')


button_accept = ctk.CTkButton(root, text = 'Подтвердить выключение', command = on_button_accept_click_event)
button_accept.place(relx = 0.5, rely = 0.8)

button_cancel_command = ctk.CTkButton(root, text = 'Отменить выключение', command = on_button_cancel_click_event)
button_cancel_command.place(relx = 0.1, rely = 0.8)

spinbox_for_hours = CTkSpinbox(root, start_value = 0, min_value = 0, max_value = 23, step_value = 1)
spinbox_for_hours.place(relx = 0.1, rely = 0.35)

spinbox_for_minutes = CTkSpinbox(root, start_value = 0, min_value = 0, max_value = 50, step_value = 5)
spinbox_for_minutes.place(relx = 0.4, rely = 0.35)

spinbox_for_seconds = CTkSpinbox(root, start_value = 0, min_value = 0, max_value = 50, step_value = 10)
spinbox_for_seconds.place(relx = 0.7, rely = 0.35)

# division_label_1 = ctk.CTkLabel(root, text = ':'); division_label_1.place(relx = 0.45, rely = 0.4)
# division_label_2 = ctk.CTkLabel(root, text = ':'); division_label_2.place(relx = 0.65, rely = 0.4)

# entry_hours = ctk.CTkEntry(root, width = 40); entry_hours.place(relx = 0.3, rely = 0.4)
# entry_minutes = ctk.CTkEntry(root, width = 40); entry_minutes.place(relx = 0.5, rely = 0.4)
# entry_seconds = ctk.CTkEntry(root, width = 40); entry_seconds.place(relx = 0.7, rely = 0.4)

info_label_about = ctk.CTkLabel(root, text = 'Введите время ЧЧ:ММ:СС, чтобы запланировать отключение')
info_label_about.place(relx = 0.03, rely = 0.2)

if __name__ == "__main__":

    root.mainloop()