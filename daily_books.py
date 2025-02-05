from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect



def add_daily():
    d_b1=d1.get()
    d_b2=d2.get()
    d_b3=d3.get()
    d_b4=d4.get()
    d_b5=d5.get()
    d_b6=d6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.daily_book(title,dhire_date,dedline,compl_date,employee_id,status) VALUES(%s,%s,%s,%s,%s,%s)",(d_b1,d_b2,d_b3,d_b4,d_b5,d_b6))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
def upd_daily():
    d_b1=d1.get()
    d_b2=d2.get()
    d_b3=d3.get()
    d_b4=d4.get()
    d_b5=d5.get()
    d_b6=d6.get()
    d_b7=d7.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.daily_book SET title=%s,dhire_date=%s,dedline=%s,compl_date=%s,employee_id=%s,status=%s WHERE id=%s;",(d_b1,d_b2,d_b3,d_b4,d_b5,d_b6,d_b7))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
def del_daily():
    d_b7=d7.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.daily_book WHERE id=%s;",(d_b7))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()

def daily_book():
    global d1,d2,d3,d4,d5,d6,d7    
    day=Tk()
    day.title("Добавить ежедневник")
    day.geometry("380x270")
    day.resizable(False,False)
    Label(day,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(day,text="Дата получения",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(day,text="Сроки",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(day,text="Дата выполнения",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(day,text="Сотрудник",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    Label(day,text="Статус",font=("Arial",15),bg="green",fg="black").grid(row=6,column=0,sticky="wens",pady=6,padx=13)
    
    d1=Entry(day)
    d1.grid(row=1,column=1,pady=6)
    d2=Entry(day)
    d2.grid(row=2,column=1,pady=6)
    d3=Entry(day)
    d3.grid(row=3,column=1,pady=6)
    d4=Entry(day)
    d4.grid(row=4,column=1,pady=6)
    d5=Entry(day)
    d5.grid(row=5,column=1,pady=6)
    d6=Entry(day)
    d6.grid(row=6,column=1,pady=6)
    
    Label(day,text="ID:",bg="green",font=("Arial",15)).grid(row=9,column=0,sticky="wens",pady=6,padx=20)
    d7=Entry(day)
    d7.grid(row=9,column=1,pady=6,padx=10)
    Button(day,text="Найти",bg="green",font=("Arial",15)).grid(row=10,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    

    Button(day,text="Создать",font=("Arial",15),bg="green",width=16).grid(row=7,column=0,sticky="ns",pady=6)
    Button(day,text="Изменить",bg="green",font=("Arial",15)).grid(row=7,column=1,pady=6,padx=10)
    Button(day,text="Удалить",bg="green",font=("Arial",15)).grid(row=8,column=0,pady=6,padx=10)
    Button(day,text="Вернуться",font=("Arial",15),bg="green",width=16,command=day.withdraw).grid(row=8,column=1,sticky="ns",pady=6)
    
    day.mainloop()
    