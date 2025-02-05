from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect

import os

def open_doc(event):
    ed7=e7.get()
    os.startfile(ed7,"rb")



def add_doc():
    ed1=e1.get()
    ed2=e2.get()
    ed3=e3.get()
    ed4=e4.get()
    ed5=e5.get()
    ed6=e6.get()
    ed7=e7.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.documents(doc_name,doc_num,hire_date,organ_id,employee_id,expire_date,file_path)VALUES(%s,%s,%s,%s,%s,%s,%s)",(ed1,ed2,ed3,ed4,ed5,ed6,ed7))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_doc():
    ed1=e1.get()
    ed2=e2.get()
    ed3=e3.get()
    ed4=e4.get()
    ed5=e5.get()
    ed6=e6.get()
    ed7=e7.get()
    ed8=e8.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.documents SET doc_num=%s, hire_date=%s, organ_id=%s, employee_id=%s, expire_date=%s, file_path=%s WHERE id=%s;",(ed1,ed2,ed3,ed4,ed5,ed6,ed7,ed8))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
        
def del_doc():
    ed8=e8.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.documents WHERE id=%s ;",(ed8))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        


def document():
    
    global e1,e2,e3,e4,e5,e6,e7,e8
    doc=Tk()
    doc.title("Добавить документ")
    doc.resizable(False,False)
    Label(doc,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Номер",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Дата приёма",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Организация",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Ответственный",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Срок действия",font=("Arial",15),bg="green",fg="black").grid(row=6,column=0,sticky="wens",pady=6,padx=13)
    Label(doc,text="Ссылка на документ",font=("Arial",15),bg="green",fg="black").grid(row=7,column=0,sticky="wens",pady=6,padx=13)
   
    e1=Entry(doc)
    e1.grid(row=1,column=1,pady=6)
    e2=Entry(doc)
    e2.grid(row=2,column=1,pady=6)
    e3=Entry(doc)
    e3.grid(row=3,column=1,pady=6)
    e4=ttk.Combobox(doc)
    e4.grid(row=4,column=1,pady=6)
    e5=ttk.Combobox(doc)
    e5.grid(row=5,column=1,pady=6)
    e6=Entry(doc)
    e6.grid(row=6,column=1,pady=6)
    e7=Entry(doc)
    e7.grid(row=7,column=1,pady=6)
    
    Label(doc,text="ID:",bg="green",font=("Arial",15)).grid(row=10,column=0,sticky="wens",pady=6,padx=20)
    e8=Entry(doc)
    e8.grid(row=10,column=1,pady=6,padx=10)
    Button(doc,text="Найти",bg="green",font=("Arial",15)).grid(row=11,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(doc,text="Открыть",font=("Arial",15),bg="green",width=16).grid(row=7,column=2,sticky="ns",pady=6)
    Button(doc,text="Создать",font=("Arial",15),bg="green",width=16).grid(row=8,column=0,sticky="ns",pady=6)
    Button(doc,text="Изменить",bg="green",font=("Arial",15)).grid(row=8,column=1,pady=6,padx=10)
    Button(doc,text="Удалить",bg="green",font=("Arial",15)).grid(row=9,column=0,pady=6,padx=10)
    Button(doc,text="Вернуться",font=("Arial",15),bg="green",width=16,command=doc.withdraw).grid(row=9,column=1,sticky="ns",pady=6)
    
    doc.bind("Button2",open_doc)
    doc.mainloop()

    