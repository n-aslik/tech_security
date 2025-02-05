from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect
import os

def open_cert(event):
    ce3=c3.get()
    os.startfile(ce3,"rb")

def add_cert():
    ce1=c1.get()
    ce2=c2.get()
    ce3=c3.get()
    ce4=c4.get()
    ce5=c5.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.certificate(cert_name,cert_no,hyperlink,hire_date,expire_date)VALUES(%s,%s,%s,%s,%s)",(ce1,ce2,ce3,ce4,ce5))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_cert():
    ce1=c1.get()
    ce2=c2.get()
    ce3=c3.get()
    ce4=c4.get()
    ce5=c5.get()
    ce6=c6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.certificate SET cert_name=%s,cert_no=%s,hyperlink=%s, hire_date=%s,expire_date=%s WHERE id=%s;",(ce1,ce2,ce3,ce4,ce5,ce6))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_cert():
    ce6=c6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.certificate WHERE id=%s;",(ce6))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()

def certificate():
    global c1,c2,c3,c4,c5,c6
    cert=Tk()
    cert.title("Добавить удостоверение")
    cert.resizable(False,False)
    Label(cert,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(cert,text="Номер",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(cert,text="Гиперссылка",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(cert,text="Дата получения",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(cert,text="Срок действия",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    
   
    c1=Entry(cert)
    c1.grid(row=1,column=1,pady=6)
    c2=Entry(cert)
    c2.grid(row=2,column=1,pady=6)
    c3=Entry(cert)
    c3.grid(row=3,column=1,pady=6)
    c4=Entry(cert)
    c4.grid(row=4,column=1,pady=6)
    c5=Entry(cert)
    c5.grid(row=5,column=1,pady=6)
    
    Label(cert,text="ID:",bg="green",font=("Arial",15)).grid(row=9,column=0,sticky="wens",pady=6,padx=20)
    c6=Entry(cert)
    c6.grid(row=9,column=1,pady=6,padx=10)
    Button(cert,text="Найти",bg="green",font=("Arial",15)).grid(row=10,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(cert,text="Открыть",font=("Arial",15),bg="green",width=16).grid(row=3,column=2,sticky="ns",pady=6)
    Button(cert,text="Создать",font=("Arial",15),bg="green",width=16).grid(row=7,column=0,sticky="ns",pady=6)
    Button(cert,text="Изменить",bg="green",font=("Arial",15)).grid(row=7,column=1,pady=6,padx=10)
    Button(cert,text="Удалить",bg="green",font=("Arial",15)).grid(row=8,column=0,pady=6,padx=10)
    Button(cert,text="Вернуться",font=("Arial",15),bg="green",width=16,command=cert.withdraw).grid(row=8,column=1,sticky="ns",pady=6)
    
    cert.bind("Button2",open_cert)
    cert.mainloop()
    
