from tkinter import *
from tkinter import ttk,messagebox

from dbconnect import get_db_connect


def add_pos():
    po1=p1.get()
    po2=p2.get()
    po3=p3.get()
    po4=p4.get()
    po5=p5.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.positions(position,area_id,instruction_id,cert_id,training_id) VALUES(%s,%s,%s,%s,%s)",(po1,po2,po3,po4,po5))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_pos():
    po1=p1.get()
    po2=p2.get()
    po3=p3.get()
    po4=p4.get()
    po5=p5.get()
    po6=p6.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.positions SET  position=%s, area_id=%s, instruction_id=%s, cert_id=%s, training_id=%s WHERE id=%s;",(po1,po2,po3,po4,po5,po6))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_pos():
    po6=p6.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.positions WHERE id=%s;",(po6))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        


def position():
    global p1,p2,p3,p4,p5,p6
    pos=Tk()
    pos.title("Добавить должность")
    pos.resizable(False,False)
    Label(pos,text="Название",bg="green",font=("Arial",15)).grid(row=1,column=0,sticky="wens",pady=6,padx=20)
    Label(pos,text="Участок",bg="green",font=("Arial",15)).grid(row=2,column=0,sticky="wens",pady=6,padx=20)
    Label(pos,text="Инструктаж",bg="green",font=("Arial",15)).grid(row=3,column=0,sticky="wens",pady=6,padx=20)
    Label(pos,text="Удостоверение",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="wens",pady=6,padx=20)
    Label(pos,text="Обучение",bg="green",font=("Arial",15)).grid(row=5,column=0,sticky="wens",pady=6,padx=20)

    p1=Entry(pos)
    p1.grid(row=1,column=1,pady=6,padx=10)
    p2=Entry(pos)
    p2.grid(row=2,column=1,pady=6,padx=10)
    p3=Entry(pos)
    p3.grid(row=3,column=1,pady=6,padx=10)
    p4=Entry(pos)
    p4.grid(row=4,column=1,pady=6,padx=10)
    p5=Entry(pos)
    p5.grid(row=5,column=1,pady=6,padx=10)

    
    Label(pos,text="ID:",bg="green",font=("Arial",15)).grid(row=8,column=0,sticky="wens",pady=6,padx=20)
    p6=Entry(pos)
    p6.grid(row=8,column=1,pady=6,padx=10)
    Button(pos,text="Найти",bg="green",font=("Arial",15)).grid(row=9,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    
    Button(pos,text="Добавить",bg="green",font=("Arial",15)).grid(row=6,column=0,sticky="wens",pady=6,padx=10)
    Button(pos,text="Изменить",bg="green",font=("Arial",15)).grid(row=6,column=1,sticky="wens",pady=6,padx=10)
    Button(pos,text="Удалить",bg="green",font=("Arial",15)).grid(row=7,column=0,sticky="wens",pady=6,padx=10)
    Button(pos,text="Выйти",bg="green",font=("Arial",15)).grid(row=7,column=1,pady=6,sticky="wens",padx=10)
    pos.mainloop()

    
