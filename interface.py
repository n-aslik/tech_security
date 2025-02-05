from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import views
from dbconnect import get_db_connect
from utils import hash_password
def choose_instruction():
    ch_ins=Tk()
    ch_ins.title("Выбор инструктажа")
    ch_ins.geometry("300x400")
    ch_ins.resizable(False,False)
    Label(ch_ins,text="Выберите инструктаж",font=("Arial",15),bg="green",fg="black").grid(row=0,column=1,sticky="news",padx=6,pady=10)
    Button(ch_ins,text="Пожарная безопасность",font=("Arial",15),bg="green",command=views.instruction_view).grid(row=2,column=1,sticky="news",pady=10,padx=6)
    Button(ch_ins,text="Промышленная безопасность",font=("Arial",15),bg="green",command=views.instruction_view).grid(row=3,column=1,sticky="news",pady=10,padx=6)
    Button(ch_ins,text="ГоиЧс",font=("Arial",15),bg="green",command=views.instruction_view).grid(row=4,column=1,sticky="news",pady=10,padx=6)
    Button(ch_ins,text="Охрана труда",font=("Arial",15),bg="green",command=views.instruction_view).grid(row=5,column=1,sticky="news",pady=10,padx=6)
    Button(ch_ins,text="Вернуться",font=("Arial",15),bg="green",command=ch_ins.withdraw).grid(row=6,column=1,sticky="news",pady=10,padx=6)
    ch_ins.mainloop()
    

    
def add_com_ins():
    db=get_db_connect()
    curs=db.cursor()
    emi1=em1.get()
    emi2=em2.get()
    emi3=em3.get()
    emi4=em4.get()
    emi5=em5.get()
    emi6=em6.get()   
    emi7=em7.get()
    emi8=em8.get()
    try:
        curs.execute("INSERT INTO techsec.employees(name,surname,fathername,organ_id,hire_date,area_id,position_id,e_sign)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",emi1,emi2,emi3,emi4,emi5,emi6,emi7,emi8)
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
        Button(emp,text="Создать",font=("Arial",15),bg="green",width=16,command=choose_instruction).grid(row=14,column=0,sticky="ns",pady=6)
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        


def complete_instruction():
    global em1,em2,em3,em4,em5,em6,em7,em8,em9,em10,em11,em12,em13,emp
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
    
    
    # Button(cins,text="Открыть",font=("Arial",15),bg="green",width=16).grid(row=7,column=2,sticky="ns",pady=6)
    Button(emp,text="Создать",font=("Arial",15),bg="green",width=16,command=add_com_ins).grid(row=14,column=0,sticky="ns",pady=6)
    Button(emp,text="Вернуться",font=("Arial",15),bg="green",width=16,command=emp.withdraw).grid(row=14,column=1,sticky="ns",pady=6)
    emp.mainloop()
    
    

    



def admin_panel():
    admin=Tk()
    admin.title("Панель администратора")
    admin.resizable(False,False)
    Label(admin,text="Администратор",font=("Arial",15),bg="white",width=16).grid(row=0,column=1,sticky="ns",pady=7)
    Button(admin,text="Организации",font=("Arial",15),bg="green",width=16,command=views.organization_view).grid(row=1,column=0,pady=7,padx=7)
    Button(admin,text="Документы",font=("Arial",15),bg="green",width=16,command=views.document_view).grid(row=1,column=2,pady=7,padx=7)
    Button(admin,text="Участки",font=("Arial",15),bg="green",width=16,command=views.area_view).grid(row=2,column=0,pady=7,padx=7)
    Button(admin,text="Структура",font=("Arial",15),bg="green",width=16,command=views.structure_view).grid(row=2,column=2,pady=7,padx=7)
    Button(admin,text="Должности",font=("Arial",15),bg="green",width=16,command=views.position_view).grid(row=3,column=0,pady=7,padx=7)
    Button(admin,text="Удостоверения",font=("Arial",15),bg="green",width=16,command=views.certificate_view).grid(row=3,column=2,pady=7,padx=7)
    Button(admin,text="Сотрудники",font=("Arial",15),bg="green",width=16,command=views.employee_view).grid(row=4,column=0,pady=7,padx=7)
    Button(admin,text="Инструктажи",font=("Arial",15),bg="green",width=16,command=views.instruction_view).grid(row=4,column=2,pady=7,padx=7)
    Button(admin,text="Профили",font=("Arial",15),bg="green",width=16,command=views.profile_view).grid(row=5,column=0,pady=7,padx=7)
    Button(admin,text="Отрасли",font=("Arial",15),bg="green",width=16,command=views.industries_view).grid(row=5,column=2,pady=7,padx=7)
    Button(admin,text="Выйти",font=("Arial",15),bg="green",width=16,command=admin.withdraw).grid(row=6,column=1,pady=7)
    admin.mainloop()


def add_reg():
    ru1=r1.get()
    ru2=r2.get()
    db=get_db_connect()
    curs=db.cursor()
    h_r2=hash_password(ru2)
    try:
        curs.execute("SELECT * FROM techsec.users u WHERE u.username=%s and u.password=%s;",(ru1,h_r2))
        res=curs.fetchone()
        if  res:
            if ru1=="admin" and h_r2=="e9c322a62fbc0d47b9a80e67cddc661f4b111f5e9fc7af62e9cd909e79670f34":
                Button(reg,text="Войти",font=("Arial",15),bg="green",state=["active"],command=admin_panel).grid(row=3,column=1,sticky="news",pady=6)
            else:
                messagebox.showinfo("Сообщение","Только админ имеет доступ")
            
                
        else:
            curs.execute("INSERT INTO techsec.users(username,password)VALUES(%s,%s)",(ru1,h_r2))
            db.commit()
            messagebox.showinfo("Сообщение","Добавление прошло успешно!")
               
    except Exception as e:
        messagebox.showerror("Ошибка","Добавление прошло не успешно")
        print(e)
        db.rollback()
        db.close()
        
def register():
    global r1,r2,reg
    reg=Tk()
    reg.title("Вход")
    reg.geometry("300x300")
    reg.resizable(False,False)
    Label(reg,text="Вход",font=("Arial",15),bg="green",fg="black",width=16).grid(row=0,column=1,sticky="news",pady=6)
    Label(reg,text="Логин:",fg="black",bg="white").grid(row=1,column=0,sticky="news",pady=6)
    Label(reg,text="Пароль:",fg="black",bg="white").grid(row=2,column=0,sticky="news",pady=6)
    r1=Entry(reg)
    r1.grid(row=1,column=1)
    r2=Entry(reg,show="*")
    r2.grid(row=2,column=1)
    Button(reg,text="Войти",font=("Arial",15),bg="green",command=add_reg).grid(row=3,column=1,sticky="news",pady=6)
    Button(reg,text="Вернуться",font=("Arial",15),bg="green",command=reg.withdraw).grid(row=4,column=1,sticky="news",pady=6)
    reg.mainloop()
    
root=Tk()
root.title("Главная")
root.geometry("300x250")
root.config(bg="white")
root.resizable(False,False)
icon=PhotoImage(file="katodmin.png")
root.iconphoto(True,icon)
Label(root,image=icon).grid(row=0,column=0,sticky="news")
Label(root,text="КАТОД",font=("Arial",15),bg="white",width=16).grid(row=1,column=1,pady=10)
Button(root,text="Вход",font=("Arial",15),bg="green",width=16,command=register).grid(row=2,column=1,pady=10)
Button(root,text="Пройти инструктаж",font=("Arial",15),bg="green",width=16,command=complete_instruction).grid(row=3,column=1,pady=10)
root.mainloop()
