from tkinter import *
from tkinter import messagebox
from dbconnect import get_db_connect

def add_area():
    ar1=a1.get()
    ar2=a2.get()
    ar3=a3.get()
    ar4=a4.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.areas(area_name,boss_id,director_id,emp_id)VALUES(%s,%s,%s,%s)",(ar1,ar2,ar3,ar4))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
def upd_area():
    ar1=a1.get()
    ar2=a2.get()
    ar3=a3.get()
    ar4=a4.get()
    ar5=a5.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.areas SET area_name=%s, boss_id=%s, director_id=%s, emp_id=%s WHERE id=%s  ;",(ar1,ar2,ar3,ar4,ar5))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
def del_area():
    ar5=a5.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.areas WHERE id=%s;",(ar5))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()

def area():
    global a1,a2,a3,a4,a5
    area=Tk()
    area.title("Добавить участок")
    area.resizable(False,False)
    Label(area,text="Название",bg="green",font=("Arial",15)).grid(row=1,column=0,sticky="wens",pady=6,padx=20)
    Label(area,text="Начальник",bg="green",font=("Arial",15)).grid(row=2,column=0,sticky="wens",pady=6,padx=20)
    Label(area,text="Высшее руководство",bg="green",font=("Arial",15)).grid(row=3,column=0,sticky="wens",pady=6,padx=20)
    Label(area,text="Сотрудник",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="wens",pady=6,padx=20)
    
    a1=Entry(area)
    a1.grid(row=1,column=1,pady=6,padx=10)
    a2=Entry(area)
    a2.grid(row=2,column=1,pady=6,padx=10)
    a3=Entry(area)
    a3.grid(row=3,column=1,pady=6,padx=10)
    a4=Entry(area)
    a4.grid(row=4,column=1,pady=6,padx=10)
    
    Label(area,text="ID:",bg="green",font=("Arial",15)).grid(row=7,column=0,sticky="wens",pady=6,padx=20)
    a5=Entry(area)
    a5.grid(row=7,column=1,pady=6,padx=10)
    Button(area,text="Найти",bg="green",font=("Arial",15)).grid(row=8,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    

    Button(area,text="Добавить",bg="green",font=("Arial",15)).grid(row=5,column=0,sticky="wens",pady=6,padx=10)
    Button(area,text="Изменить",bg="green",font=("Arial",15)).grid(row=5,column=1,sticky="wens",pady=6,padx=10)
    Button(area,text="Удалить",bg="green",font=("Arial",15)).grid(row=6,column=0,sticky="wens",pady=6,padx=10)
    Button(area,text="Выйти",bg="green",font=("Arial",15)).grid(row=6,column=1,sticky="wens",pady=6,padx=10)
    area.mainloop()

    
