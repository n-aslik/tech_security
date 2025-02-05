from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect



def add_emp():
    emi1=em1.get()
    emi2=em2.get()
    emi3=em3.get()
    emi4=em4.get()
    emi5=em5.get()
    emi6=em6.get()   
    emi7=em7.get()
    emi8=em8.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.employees(name,surname,fathername,organ_id,hire_date,emp_id,position_id,e_sign)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(emi1,emi2,emi3,emi4,emi5,emi6,emi7,emi8))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_emp():
    emi1=em1.get()
    emi2=em2.get()
    emi3=em3.get()
    emi4=em4.get()
    emi5=em5.get()
    emi6=em6.get()   
    emi7=em7.get()
    emi8=em8.get()
    emi9=em9.get()
    emi10=em10.get()
    emi11=em11.get()
    emi12=em12.get()
    emi13=em13.get()
    emi14=em14.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.employees SET name=%s,surname=%s,fathername=%s, birth_day=%s, organ_id=%s, hire_date=%s, emp_id=%s, position_id=%s, chief=%s, e_sign=%s ,instruction_id=%s, cert_id=%s, training_id=%s  WHERE id=%s ;",(emi1,emi2,emi3,emi4,emi5,emi6,emi7,emi8,emi9,emi10,emi11,emi12,emi13,emi14))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_emp():
    emi14=em14.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.employees WHERE id=%s ;",(emi14))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def employee():
    global em1,em2,em3,em4,em5,em6,em7,em8,em9,em10,em11,em12,em13,em14
    emp=Tk()
    emp.title("Добавить сотрудника")
    emp.resizable(False,False)
    Label(emp,text="Фамилия",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Имя",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Отчество",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Дата рождения",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Организация",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Дата приёма",font=("Arial",15),bg="green",fg="black").grid(row=6,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Участок",font=("Arial",15),bg="green",fg="black").grid(row=7,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Должность",font=("Arial",15),bg="green",fg="black").grid(row=8,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Начальник",font=("Arial",15),bg="green",fg="black").grid(row=9,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Электронная подпись",font=("Arial",15),bg="green",fg="black").grid(row=10,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Инструктажи",font=("Arial",15),bg="green",fg="black").grid(row=11,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Удостоверение",font=("Arial",15),bg="green",fg="black").grid(row=12,column=0,sticky="wens",pady=6,padx=13)
    Label(emp,text="Обучение",font=("Arial",15),bg="green",fg="black").grid(row=13,column=0,sticky="wens",pady=6,padx=13)
    
    em1=Entry(emp)
    em1.grid(row=1,column=1,pady=6)
    em2=Entry(emp)
    em2.grid(row=2,column=1,pady=6)
    em3=Entry(emp)
    em3.grid(row=3,column=1,pady=6)
    em4=Entry(emp)
    em4.grid(row=4,column=1,pady=6)
    em5=Entry(emp)
    em5.grid(row=5,column=1,pady=6)
    em6=Entry(emp)
    em6.grid(row=6,column=1,pady=6)
    em7=ttk.Combobox(emp)
    em7.grid(row=7,column=1,pady=6)
    em8=ttk.Combobox(emp)
    em8.grid(row=8,column=1,pady=6)
    em9=ttk.Combobox(emp)
    em9.grid(row=9,column=1,pady=6)
    em10=Entry(emp)
    em10.grid(row=10,column=1,pady=6)
    em11=ttk.Combobox(emp)
    em11.grid(row=11,column=1,pady=6)
    em12=ttk.Combobox(emp)
    em12.grid(row=12,column=1,pady=6)
    em13=ttk.Combobox(emp)
    em13.grid(row=13,column=1,pady=6)
    
    Label(emp,text="ID:",bg="green",font=("Arial",15)).grid(row=16,column=0,sticky="wens",pady=6,padx=20)
    em14=Entry(emp)
    em14.grid(row=16,column=1,pady=6,padx=10)
    Button(emp,text="Найти",bg="green",font=("Arial",15)).grid(row=17,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(emp,text="Создать",font=("Arial",15),bg="green").grid(row=14,column=0,sticky="wens",pady=6,padx=10)
    Button(emp,text="Изменить",bg="green",font=("Arial",15)).grid(row=14,column=1,sticky="wens",pady=6,padx=10)
    Button(emp,text="Удалить",bg="green",font=("Arial",15)).grid(row=15,column=0,sticky="wens",pady=6,padx=10)
    Button(emp,text="Вернуться",font=("Arial",15),bg="green",command=emp.withdraw).grid(row=15,column=1,sticky="wens",pady=6,padx=10)
    
    emp.mainloop()

    
    