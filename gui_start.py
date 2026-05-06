from tkinter import ttk    
import tkinter as tk    
from tkinter import messagebox
def check_password():   
    password = entry.get()    
    black_list = ["password123", "admin777", "qwertyuiop", "12345678"]  
    score = 0   
    if len(password) >=8: score +=20    
    if password.lower() not in black_list: score += 20  
    if any(c.isupper() for c in password): score += 20  
    if any(c.islower() for c in password): score += 20  
    if not password.isalnum(): score += 20  
    progress['value'] = score
    if len(password) < 8:     
        result_label.config(text="Ошибка: Слишком короткий!", fg="red")         
    elif password.lower() in black_list:  
        result_label.config(text="Заблокировано: Популярный пароль!", fg="red")     
    elif password.isdigit():                          
        result_label.config(text="Опасно: Только цифры!", fg="orange")  
    elif password.lower() == password:                                                                                  
        result_label.config(text="Слабо: Добавьте заглавные!", fg="orange")    
    elif password.upper() == password:                          
        result_label.config(text="Слабо: Добавьте маленькие буквы!", fg="orange")    
    elif password.isalnum():  
        result_label.config(text="Средне: Добавьте спецсимвол!", fg="blue")
    else:   
        result_label.config(text="Идеально: Максимальная защита", fg="green")    
root = tk.Tk()                                      
root.title("Security Analyzer v1.0")    
root.geometry("400x250")    
label = tk.Label(root, text="Введите пароль для анализа:", font=("Arial", 12))   
label.pack(pady=10) 
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)  
entry.pack(pady=5)  
check_button = tk.Button(root, text="Проверить надёжность", command=check_password, bg="#2ecc71", fg="white")   
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")   
progress.pack(pady=10)   
check_button.pack(pady=20)  
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"))  
result_label.pack() 
root.mainloop()