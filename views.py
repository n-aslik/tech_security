from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from areas import area
from certificates import certificate
from industries import industry
from employees import employee
from organizations import  organization
from positions import position
from profiles import profile
from trainings import training
from documents import document
from daily_books import daily_book
from utests import pos_test
from instructions import instruction
from dbconnect import get_db_connect


# "users": ["id", "username", "curs.execute("""""")
        # res=curs.fetchall()
        # for i in res:
        #     tree.insert("","end",values=i)word", "organ_id", "employee_id", "permission"],
        
def select_area():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT a.id aid ,a.area_name area_name, CONCAT_WS(' ',e.name,e.surname,e.fathername)as boss,
                     CONCAT_WS(' ',e.name,e.surname,e.fathername)as director,
                     CONCAT_WS(' ',e.name,e.surname,e.fathername)as empl
                     FROM techsec.areas a
                     JOIN techsec.employees e ON a.boss_id=e.id or a.director_id=e.id or a.emp_id=e.id
                     JOIN techsec.positions p ON e.position_id=p.id
                     WHERE p.position in ('ген.директор','начальник','сотрудник');""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    
def area_view():
    global tree
    av=Tk()
    av.title("Участок")
    av.resizable(False,False)
    column=("id", "area_name", "boss_id", "director_id", "emp_id")
    tree=ttk.Treeview(av,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("area_name",text="Участок")
    tree.heading("boss_id",text="Начальник")
    tree.heading("director_id",text="Директор")
    tree.heading("emp_id",text="Сотрудник")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(av,text="Добавить",command=area).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(av,text="Показать",command=select_area).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    av.mainloop()


def select_certificate():
    
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT c.id c_id, c.cert_name certname,c.cert_no certno, c.hyperlink hyperlink,c.hire_date hiredate,c.expire_date expiredate
FROM techsec.certificate c;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
        
def certificate_view():
    cv=Tk()
    cv.title("Удостоверение")
    cv.resizable(False,False)
    column=("id", "cert_name", "cert_no", "hyperlink", "hire_date", "expire_date")
    tree=ttk.Treeview(cv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("cert_name",text="Название")
    tree.heading("cert_no",text="Номер")
    tree.heading("hyperlink",text="Гиперссылка")
    tree.heading("hire_date",text="Дата получения")
    tree.heading("expire_date",text="Срок действия")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(cv,text="Добавить",command=certificate).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(cv,text="Показать",command=select_certificate).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    cv.mainloop()

def select_daily_book():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT d_b.id id, d_b.title title,d_b.dhire_date hiredate,  
CONCAT_WS(' ',e.name,e.surname,e.fathername)as director,
CONCAT_WS(' ',e.name,e.surname,e.fathername)as emp,
CONCAT_WS(' ',e.name,e.surname,e.fathername)as emp1,
d_b.deadline deadline,
d_b.compl_date compldate,
d_b.status status
FROM  techsec.daily_book d_b
JOIN techsec.employees e ON d_b.employee_id=e.id
JOIN techsec.positions p ON e.position_id=p.id
WHERE p.position in ('ген.директор','начальник','сотрудник');
END;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
        
def daily_books_view():
    dv=Tk()
    dv.title("Ежедневник")
    dv.resizable(False,False)
    column=("id", "title", "dhire_date", "deadline_date", "compl_date", "employee_id", "status")
    tree=ttk.Treeview(dv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("title",text="Название")
    tree.heading("dhire_date",text="Дата выдачи")
    tree.heading("deadline_date",text="Срок")
    tree.heading("compl_date",text="Дата выполнения")
    tree.heading("employee_id",text="Сотрудник")
    tree.heading("status",text="Статус")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(dv,text="Добавить",command=daily_book).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(dv,text="Показать",command=select_daily_book).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    dv.mainloop()

def select_document():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT d.id id, d.doc_num doc_num,d.hire_date hiredate,o.organ_name organ_name,
CONCAT_WS(' ',e.name,e.surname,e.fathername)as emp,
d.expire_date expiredate,
d.file_path filepath
FROM  techsec.documents d
JOIN techsec.employees e ON d.employee_id=e.id
JOIN techsec.organizations o ON d.organ_id=o.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()

def document_view():
    dcv=Tk()
    dcv.title("Документ")
    dcv.resizable(False,False)
    column=("id","doc_name", "doc_num", "hire_date", "organ_id", "employee_id", "expire_date", "file_path")
    tree=ttk.Treeview(dcv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("doc_name",text="Название")
    tree.heading("doc_num",text="Номер")
    tree.heading("hire_date",text="Дата приёма")
    tree.heading("organ_id",text="Организация")
    tree.heading("employee_id",text="Сотрудник")
    tree.heading("expire_date",text="Срок действия")
    tree.heading("file_path",text="Ссылка на документ")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(dcv,text="Добавить",command=document).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(dcv,text="Показать",command=select_document).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    dcv.mainloop()

def select_employee():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT e.id id, CONCAT_WS(' ',e.name,e.surname,e.fathername) emp,o.organ_name organ_name,
e.hire_date hiredate, a.area_name areaname, p.position post, CONCAT_WS(' ',e.name,e.surname,e.fathername) emp1, e.e_sign esign,
ins.name iname, c.cert_name certname, tr.title title
FROM techsec.employees e
JOIN techsec.organizations o ON e.organ_id=o.id
JOIN techsec.positions p ON e.position_id=p.id
JOIN techsec.instructions ins ON e.instruction_id=ins.id
JOIN techsec.certificate c ON e.cert_id=c.id
JOIN techsec.areas a ON e.area_id=a.id
JOIN techsec.training tr ON e.training_id=tr.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    
def employee_view():
    ev=Tk()
    ev.title("Сотрудника")
    ev.resizable(False,False)
    column=("id", "name", "surname", "fathername", "birth_day", "organ_id", "hire_date", "area_id", "position_id", "chief", "e_sign", "instruction_id", "cert_id", "training_id")
    tree=ttk.Treeview(ev,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("name",text="Имя")
    tree.heading("surname",text="Фамилия")
    tree.heading("fathername",text="Отчество")
    tree.heading("birth_day",text="Дата рождения")
    tree.heading("organ_id",text="Организация")
    tree.heading("hire_date",text="Дата приёма")
    tree.heading("area_id",text="Участок")
    tree.heading("position_id",text="Должность")
    tree.heading("chief",text="Начальник")
    tree.heading("e_sign",text="Электронная\n подпись")
    tree.heading("instruction_id",text="Инструктаж")
    tree.heading("cert_id",text="Удостоверение")
    tree.heading("training_id",text="Обучение")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(ev,text="Добавить",command=employee).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(ev,text="Показать",command=select_employee).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    ev.mainloop()

def select_industry():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT  ind.id id, ind.industry industry,
CONCAT_WS(' ',e.name,e.surname,e.fathername)as emp
FROM  techsec.industies ind
JOIN techsec.employees e ON ind.responsible_id=e.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
    
    
def industries_view():
    indv=Tk()
    indv.title("Отрасль")
    indv.resizable(False,False)
    column=("id", "industry", "responsible_id")
    tree=ttk.Treeview(indv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("industry",text="Название")
    tree.heading("responsible_id",text="Ответственный")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(indv,text="Добавить",command=industry).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(indv,text="Показать",command=select_industry).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    indv.mainloop()

def select_instruction():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT ins.id id, ins.name name, inst.type_name type_name
FROM  techsec.instructions ins
JOIN techsec.instruction_type inst ON ins.type_id=inst.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()

def instruction_view():
    insv=Tk()
    insv.title("Инструктаж")
    insv.resizable(False,False)
    column=("id", "name", "type_id", "nomer", "create_date", "expire_date", "hyperlink", "test_id")
    tree=ttk.Treeview(insv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("name",text="Название")
    tree.heading("type_id",text="Вид")
    tree.heading("nomer",text="Номер")
    tree.heading("create_date",text="Дата\n формирования")
    tree.heading("expire_date",text="Срок действия")
    tree.heading("hyperlink",text="Гипперссылка")
    tree.heading("test_id",text="Ссылка на тест")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(insv,text="Добавить",command=instruction).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(insv,text="Показать",command=select_instruction).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    insv.mainloop()

def select_organization():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT  o.id id, o.organ_name organname,
CONCAT_WS(' ',e.name,e.surname,e.fathername)as emp
FROM techsec.organizations o
JOIN techsec.employees e ON o.gen_direc_id=e.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()

def organization_view():
    ov=Tk()
    ov.title("Организацию")
    ov.resizable(False,False)
    column=("id", "organ_name", "gen_direc_id")
    tree=ttk.Treeview(ov,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("organ_name",text="Название")
    tree.heading("gen_direc_id",text="Ген. директор")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(ov,text="Добавить",command=organization).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(ov,text="Показать",command=select_organization).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    ov.mainloop()

def select_position():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""ELECT  p.id id, p.position post,a.area_name areaname, i.name iname,c.cert_name certname,t.title tname
FROM  techsec.positions p
JOIN techsec.areas a ON p.area_id=a.id
JOIN techsec.instructions i ON p.instruction_id=i.id
JOIN techsec.certificate c ON p.cert_id=c.id
JOIN techsec.training t ON p.training_id=t.id;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()


def position_view():
    pv=Tk()
    pv.title("Должность")
    pv.resizable(False,False)
    column=("id", "position", "area_id", "instruction_id", "cert_id", "training_id")
    tree=ttk.Treeview(pv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("position",text="Название")
    tree.heading("area_id",text="Участок")
    tree.heading("instruction_id",text="Инструктаж")
    tree.heading("cert_id",text="Удостоверение")
    tree.heading("training_id",text="Обучение")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(pv,text="Добавить",command=position).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(pv,text="Показать",command=select_position).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    pv.mainloop()

def select_test():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT  t.id id, t.question question, t.trueans trueans, t.mark mark FROM  techsec.tests t;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()

def tests_view():
    tv=Tk()
    tv.title("Тесты")
    tv.resizable(False,False)
    column=("id", "question", "trueans", "mark")
    tree=ttk.Treeview(tv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("question",text="Вопрос")
    tree.heading("trueans",text="Ответ")
    tree.heading("mark",text="Оценка")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(tv,text="Добавить",command=pos_test).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(tv,text="Показать",command=select_test).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    tv.mainloop()

def select_training():
    db=get_db_connect()
    curs=db.cursor()
    try:
        curs.execute("""SELECT trn.id id, trn.title title,trn.number nomer, trn.hyper_link hyperlink,trn.hire_date hiredate,trn.expire_date expiredate
FROM techsec.training trn;""")
        res=curs.fetchall()
        for i in res:
            tree.insert("","end",values=i)
    except Exception as e:
        print(e)
        db.rollback()
        db.close()

def training_view():
    trv=Tk()
    trv.title("Обучения")
    trv.resizable(False,False)
    column=("id", "title", "number", "hyper_link", "hire_date", "expire_date")
    tree=ttk.Treeview(trv,columns=column,show="headings")
    tree.heading("id",text="№")
    tree.heading("title",text="Название")
    tree.heading("number",text="Номер")
    tree.heading("hyper_link",text="Гипперссылка\n на документ")
    tree.heading("hire_date",text="Дата приёма")
    tree.heading("expire_date",text="Срок действия")
    tree.grid(row=0,column=0,sticky="wens", columnspan=2,padx=10,pady=6)
    Button(trv,text="Добавить",command=training).grid(row=1,column=0,sticky="wens",padx=10,pady=6)
    Button(trv,text="Показать",command=select_training).grid(row=1,column=1,sticky="wens",padx=10,pady=6)
    trv.mainloop()
    




def profile_view():
    # Создаём основное окно
    root1 = tk.Tk()
    root1.title("Система управления персоналом")
    root1.geometry("600x400")

    # Создаём вкладки
    notebook = ttk.Notebook(root1)
    notebook.pack(fill="both", expand=True)

    # Вкладка "Профиль"
    frame_profile = ttk.Frame(notebook)
    notebook.add(frame_profile, text="Профиль")

    Label(frame_profile, text="Фамилия Имя Отчество:").pack(anchor="w", padx=10, pady=2)
    Entry(frame_profile).pack(fill="x", padx=10, pady=2)

    Label(frame_profile, text="Должность:").pack(anchor="w", padx=10, pady=2)
    Entry(frame_profile).pack(fill="x", padx=10, pady=2)

    Label(frame_profile, text="Начальник:").pack(anchor="w", padx=10, pady=2)
    Entry(frame_profile).pack(fill="x", padx=10, pady=2)

    Label(frame_profile, text="Подчиненные:").pack(anchor="w", padx=10, pady=2)
    Listbox(frame_profile, height=5).pack(fill="both", padx=10, pady=2, expand=True)

    # Вкладка "Уведомления"
    frame_notifications = ttk.Frame(notebook)
    notebook.add(frame_notifications, text="Уведомления")

    notification_list = tk.Listbox(frame_notifications)
    notification_list.pack(fill="both", expand=True, padx=10, pady=10)

    # Добавляем тестовые уведомления
    today = datetime.today()
    dates = [
        ("Инструктаж по технике безопасности", today + timedelta(days=7)),
        ("Медосмотр", today + timedelta(days=3)),
        ("Повторный инструктаж", today + timedelta(days=1)),
    ]

    for text, date in dates:
        days_left = (date - today).days
        if days_left <= 3:
            notification_list.insert("end", f"❗ {text} - {date.strftime('%d.%m.%Y')}")
        else:
            notification_list.insert("end", f"⚠ {text} - {date.strftime('%d.%m.%Y')}")

    # Вкладка "Ежедневник"
    frame_todo = ttk.Frame(notebook)
    notebook.add(frame_todo, text="Ежедневник")

    task_list = tk.Listbox(frame_todo)
    task_list.pack(fill="both", expand=True, padx=10, pady=10)

    def add_task():
        task = task_entry.get()
        date = date_entry.get()
        if task and date:
            task_list.insert("end", f"{task} - {date}")

    frame_add_task = ttk.Frame(frame_todo)
    frame_add_task.pack(fill="x", padx=10, pady=5)

    task_entry = ttk.Entry(frame_add_task)
    task_entry.pack(side="left", expand=True, fill="x")

    date_entry = ttk.Entry(frame_add_task, width=10)
    date_entry.pack(side="left", padx=5)

    Button(frame_add_task, text="Добавить", command=add_task).pack(side="right")

    # Запуск приложения
    root1.mainloop()

def employee_card():
    win=Tk()
    win.title("Карточка сотрудника")
    navbar=Menu()
    header=Menu(tearoff=0)
    header.add_command()
    header.add_command()
    header.add_command()
    search=Menu(tearoff=0)
    search.add_command()
    logout=Menu(tearoff=0)
    logout.add_command()
    navbar.add_cascade(label="Главная",menu=header)
    navbar.add_cascade(label="Поиск",menu=search)
    navbar.add_cascade(label="Выйти",menu=logout) 
    
    win.option_add("*tearoff",False) 
    icon=PhotoImage(file="katodmin.png")
    win.iconphoto(True,icon)
    win.config(menu=navbar)
    win.mainloop()

    
    
def structure_view():
    pass