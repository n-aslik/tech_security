from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect


def add_org():
    og1=o1.get()
    og2=o2.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.organizations(organ_name,gen_direc_id) VALUES(%s,%s)",(og1,og2))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_org():
    og1=o1.get()
    og2=o2.get()
    og3=o3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.organizations SET organ_name=%s, gen_direc_id=%s WHERE id=%s;",(og1,og2,og3))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_org():
    og3=o3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.organizations WHERE id=%s;",(og3))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def organization():
    global o1,o2,o3
    org=Tk()
    org.title("Добавить организацию")
    org.resizable(False,False)
    Label(org,text="Название",bg="green",font=("Arial",15)).grid(row=1,column=0,sticky="wens",pady=6,padx=10)
    Label(org,text="Ген.директор",bg="green",font=("Arial",15)).grid(row=2,column=0,sticky="wens",pady=6,padx=10)
    
    o1=Entry(org)
    o1.grid(row=1,column=1)
    o2=Entry(org)
    o2.grid(row=2,column=1)
    
    Label(org,text="ID:",bg="green",font=("Arial",15)).grid(row=5,column=0,sticky="wens",pady=6,padx=20)
    o3=Entry(org)
    o3.grid(row=5,column=1,pady=6,padx=10)
    Button(org,text="Найти",bg="green",font=("Arial",15)).grid(row=6,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(org,text="Добавить",bg="green",font=("Arial",15)).grid(row=3,column=0,sticky="wens",pady=6,padx=10)
    Button(org,text="Изменить",bg="green",font=("Arial",15)).grid(row=3,column=1,sticky="wens",pady=6,padx=10)
    Button(org,text="Удалить",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="wens",pady=6,padx=10)
    Button(org,text="Выйти",bg="green",font=("Arial",15)).grid(row=4,column=1,sticky="wens",pady=6,padx=10)
    org.mainloop()
    
