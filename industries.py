from tkinter import *
from tkinter import ttk,messagebox

from dbconnect import get_db_connect



def add_ind():
    inda1=in1.get()
    inda2=in2.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.industies(industry,responsible_id) VALUES(%s,%s)",(inda1,inda2))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
    
        
def upd_ind():
    inda1=in1.get()
    inda2=in2.get()
    inda3=in3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.industies SET industry=%s, responsible_id=%s WHERE id=%s ;",(inda1,inda2,inda3))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_ind():
    inda3=in3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.industies WHERE id=%s;",(inda3))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def industry():
    global in1,in2,in3
    ind=Tk()
    ind.title("Добавить отрасль")
    ind.geometry("300x200")
    ind.resizable(False,False)
    Label(ind,text="Название",fg="black",bg="white",font=("Arial",15)).grid(row=1,column=0,sticky="news",pady=6)
    Label(ind,text="Ответственный",fg="black",bg="white",font=("Arial",15)).grid(row=2,column=0,sticky="news",pady=6)
    in1=Entry(ind)
    in1.grid(row=1,column=1)
    in2=Entry(ind)
    in2.grid(row=2,column=1)
    
    Label(ind,text="ID:",bg="green",font=("Arial",15)).grid(row=5,column=0,sticky="wens",pady=6,padx=20)
    in3=Entry(ind)
    in3.grid(row=5,column=1,pady=6,padx=10)
    Button(ind,text="Найти",bg="green",font=("Arial",15)).grid(row=6,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(ind,text="Создать",font=("Arial",15),bg="green").grid(row=3,column=0,sticky="news",pady=6,padx=6)
    Button(ind,text="Изменить",bg="green",font=("Arial",15)).grid(row=3,column=1,sticky="news",pady=6,padx=10)
    Button(ind,text="Удалить",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="news",pady=6,padx=10)
    Button(ind,text="Вернуться",font=("Arial",15),bg="green",command=ind.withdraw).grid(row=4,column=1,sticky="news",pady=6,padx=6)
    ind.mainloop()

