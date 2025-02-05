from tkinter import *
from tkinter import ttk,messagebox

from dbconnect import get_db_connect


def add_inst():
    ein1=ei1.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.instruction_type(type_name)VALUES(%s)",(ein1))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_inst():
    ein1=ei1.get()
    ein2=ei2.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.instruction_type SET type_name=%s WHERE id=%s;",(ein1,ein2))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_inst():
    ein2=ei2.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.instruction_type  WHERE id=%s;",(ein2))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def instruction_type():
    global ei1,ei2
    inst=Tk()
    inst.title("Добавить инструктаж")
    inst.resizable(False,False)
    Label(inst,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
   
    ei1=Entry(inst)
    ei1.grid(row=1,column=1,pady=6)
    
    Label(inst,text="ID:",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="wens",pady=6,padx=20)
    ei2=Entry(inst)
    ei2.grid(row=4,column=1,pady=6,padx=10)
    Button(inst,text="Найти",bg="green",font=("Arial",15)).grid(row=5,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(inst,text="Создать",font=("Arial",15),bg="green").grid(row=2,column=0,sticky="wens",pady=6,padx=10)
    Button(inst,text="Изменить",bg="green",font=("Arial",15)).grid(row=2,column=1,sticky="wens",pady=6,padx=10)
    Button(inst,text="Удалить",bg="green",font=("Arial",15)).grid(row=3,column=0,sticky="wens",pady=6,padx=10)
    Button(inst,text="Вернуться",font=("Arial",15),bg="green",command=inst.withdraw).grid(row=3,column=1,sticky="wens",pady=6,padx=10)
    inst.mainloop()




    

