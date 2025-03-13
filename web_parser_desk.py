from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from tkinter import filedialog
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def parse_news():
    url = web_tf.get()
    element = webelement_tf.get()
    class_element = webelemclass_tf.get()
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all(element, class_element)
        result_text.delete(1.0, END)
        for title in titles:
            result_text.insert(END, title.text.strip() + "\n")
        input_frame.pack_forget() # Скрываем поля ввода
        result_frame.pack(expand=True, fill=BOTH) # Показываем результаты
    except requests.exceptions.RequestException as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"Ошибка при запросе: {e}")
    except Exception as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"Произошла ошибка: {e}")
def save_to_pdf():
    text = result_text.get(1.0, END)
    if not text.strip():
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not filepath:
        return

    try:
        c = canvas.Canvas(filepath)
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))  
        c.setFont('Arial', 12) 
        textobject = c.beginText()
        textobject.setTextOrigin(50, 750)  # Adjust position as needed
        lines = text.splitlines()
        for line in lines:
            textobject.textLine(line.encode('utf-8'))  # Ensure UTF-8 encoding
        c.drawText(textobject)
        c.save()
        print(f"Файл успешно сохранен: {filepath}")
    except Exception as e:
        print(f"Ошибка при сохранении в PDF: {e}")
def reset_interface():
    result_text.delete(1.0, END)  # Очищаем текстовое поле
    result_frame.pack_forget()    # Скрываем frame с результатами
    input_frame.pack(expand=True, fill=BOTH)
    web_tf.delete(0, END)
    webelement_tf.delete(0, END)
    webelemclass_tf.delete(0, END)

win = Tk()
win.title('Web_Parser')
win['bg'] = '#000000'
win.geometry('800x400')
win.resizable(False, False)

style = ttk.Style()
style.configure('RoundedButton.TButton',borderwidth=0, padding=6, background='#4CAF50', relief="flat", foreground='black', font=('Arial', 12))
style.map('RoundedButton.TButton', background=[('active', '#3e8e41')])

# Frame для полей ввода и кнопок
input_frame = Frame(win, padx=20, pady=20)
input_frame.pack(expand=True, fill=BOTH)

input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
input_frame.grid_columnconfigure(2, weight=1)
input_frame.grid_columnconfigure(3, weight=1)
input_frame.grid_rowconfigure(0, weight=0)
input_frame.grid_rowconfigure(1, weight=0)
input_frame.grid_rowconfigure(2, weight=0)

web_lb = Label(input_frame, text="Enter URL  ")
web_lb.grid(row=0, column=1, sticky="e", padx=3, pady=3)
webelement_lb = Label(input_frame, text="Enter html-element  ")
webelement_lb.grid(row=1, column=1, sticky="e", padx=3, pady=3)
webelemclass_lb = Label(input_frame, text="Enter class type of html-element  ")
webelemclass_lb.grid(row=2, column=1, sticky="e", padx=3, pady=3)

web_tf = Entry(input_frame)
web_tf.grid(row=0, column=2, sticky="ew", padx=3, pady=3)
webelement_tf = Entry(input_frame)
webelement_tf.grid(row=1, column=2, sticky="ew", padx=3, pady=3)
webelemclass_tf = Entry(input_frame)
webelemclass_tf.grid(row=2, column=2, sticky="ew", padx=3, pady=3)

# Frame для результатов
result_frame = Frame(win)
result_text = Text(result_frame, height=20, width=80)

# Текстовое поле для результатов
result_text.pack(pady=10)

# Frame для кнопок внизу
button_frame = Frame(win, padx=20, pady=20)
button_frame.pack(side=BOTTOM, fill=X)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

Parser_btn = ttk.Button(button_frame, text='Start parsing', style='RoundedButton.TButton', command=parse_news)
Parser_btn.grid(row=0, column=0, padx=5, pady=5)

Save = ttk.Button(button_frame, text="Save in PDF document", style='RoundedButton.TButton', command=save_to_pdf)
Save.grid(row=0, column=1, padx=5, pady=5)

New_Parsing = ttk.Button(button_frame, text="Start new parsing", style='RoundedButton.TButton', command=reset_interface)
New_Parsing.grid(row=0, column=2, padx=5, pady=5)

win.mainloop()