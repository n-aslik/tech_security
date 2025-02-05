from tkinter import *
from tkinter import ttk,messagebox
from instruction_types import instruction_type
from utests import pos_test
from dbconnect import get_db_connect


def add_ins():
    eins1=e1.get()
    eins2=e2.get()
    eins3=e3.get()
    eins4=e4.get()
    eins5=e5.get()
    eins6=e6.get()
    eins7=e7.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.instructions(name,type_id,nomer,create_date,expire_date,hyperlink,test_id) VALUES(%s,%s,%s,%s,%s,%s,%s);",(eins1,eins2,eins3,eins4,eins5,eins6,eins7))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
def upd_ins():
    eins1=e1.get()
    eins2=e2.get()
    eins3=e3.get()
    eins4=e4.get()
    eins5=e5.get()
    eins6=e6.get()
    eins7=e7.get()
    eins8=e8.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("UPDATE  techsec.instructions SET name=%s, type_id=%s, nomer=%s, create_date=%s, expire_date=%s, hyperlink=%s, test_id=%s WHERE id=%s;",(eins1,eins2,eins3,eins4,eins5,eins6,eins7,eins8))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
def del_ins():
    eins8=e8.get()
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.instructions WHERE id=%s;",(eins8))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        


def instruction():
    global e1,e2,e3,e4,e5,e6,e7,e8
    ins=Tk()
    ins.title("Добавить инструктаж")
    ins.resizable(False,False)
    Label(ins,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Вид инструктажа",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Номер",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Дата формирования",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Срок действия",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Гиперссылка\n на документ",font=("Arial",15),bg="green",fg="black").grid(row=6,column=0,sticky="wens",pady=6,padx=13)
    Label(ins,text="Ссылка на тест",font=("Arial",15),bg="green",fg="black").grid(row=7,column=0,sticky="wens",pady=6,padx=13)
   
    e1=Entry(ins)
    e1.grid(row=1,column=1,pady=6)
    e2=Entry(ins)
    e2.grid(row=2,column=1,pady=6)
    e3=Entry(ins)
    e3.grid(row=3,column=1,pady=6)
    e4=Entry(ins)
    e4.grid(row=4,column=1,pady=6)
    e5=Entry(ins)
    e5.grid(row=5,column=1,pady=6)
    e6=Entry(ins)
    e6.grid(row=6,column=1,pady=6)
    e7=Entry(ins)
    e7.grid(row=7,column=1,pady=6)
    
    Label(ins,text="ID:",bg="green",font=("Arial",15)).grid(row=11,column=0,sticky="wens",pady=6,padx=20)
    e8=Entry(ins)
    e8.grid(row=11,column=1,pady=6,padx=10)
    Button(ins,text="Найти",bg="green",font=("Arial",15)).grid(row=12,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(ins,text="Создать",font=("Arial",15),bg="green").grid(row=8,column=0,sticky="wens",pady=6,padx=10)
    Button(ins,text="Изменить",bg="green",font=("Arial",15)).grid(row=8,column=1,sticky="wens",pady=6,padx=10)
    Button(ins,text="Удалить",bg="green",font=("Arial",15)).grid(row=9,column=0,sticky="wens",pady=6,padx=10)
    Button(ins,text="Добавить вид\n инструктажа",bg="green",font=("Arial",15),command=instruction_type).grid(row=9,column=1,sticky="wens",pady=6,padx=10)
    Button(ins,text="Вернуться",font=("Arial",15),bg="green",command=ins.withdraw).grid(row=10,column=0,sticky="wens",pady=6,padx=10)
    Button(ins,text="Тесты",font=("Arial",15),bg="green",command=pos_test).grid(row=10,column=1,sticky="wens",pady=6,padx=10)
    ins.mainloop()



    

