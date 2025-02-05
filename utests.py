from tkinter import *
from tkinter import ttk,messagebox
from dbconnect import get_db_connect



def add_quiz():
    qt1=q1.get()
    qt2=q2.get()
    db=get_db_connect()    
    curs=db.cursor()
    curs.execute("INSERT INTO techsec.tests(question,trueans,mark)VALUES(%s,%s,%s)",(qt1,qt2))
    try:
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_quiz():
    qt1=q1.get()
    qt2=q2.get()
    qt3=q3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.tests SET question=%s, trueans=%s, mark=%s WHERE id=%s ;",(qt1,qt2,qt3))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_quiz():
    qt3=q3.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.tests WHERE id=%s;",(qt3))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def pos_test():
    global q1,q2,q3
    quiz=Tk()
    quiz.title("Добавить тесты")
    quiz.resizable(False,False)
    Label(quiz,text="Вопрос",fg="black",bg="white",font=("Arial",15)).grid(row=1,column=0,sticky="news",pady=6)
    Label(quiz,text="ответ",fg="black",bg="white",font=("Arial",15)).grid(row=2,column=0,sticky="news",pady=6)
    q1=Entry(quiz)
    q1.grid(row=1,column=1)
    q2=Entry(quiz)
    q2.grid(row=2,column=1)
    
    Label(quiz,text="ID:",bg="green",font=("Arial",15)).grid(row=5,column=0,sticky="wens",pady=6,padx=20)
    q3=Entry(quiz)
    q3.grid(row=5,column=1,pady=6,padx=10)
    Button(quiz,text="Найти",bg="green",font=("Arial",15)).grid(row=6,column=0,columnspan=2,sticky="wens",pady=6,padx=10)

    Button(quiz,text="Создать",font=("Arial",15),bg="green").grid(row=3,column=0,sticky="news",pady=6,padx=6)
    Button(quiz,text="Изменить",bg="green",font=("Arial",15)).grid(row=3,column=1,sticky="news",pady=6,padx=10)
    Button(quiz,text="Удалить",bg="green",font=("Arial",15)).grid(row=4,column=0,sticky="news",pady=6,padx=10)
    Button(quiz,text="Вернуться",font=("Arial",15),bg="green",command=quiz.withdraw).grid(row=4,column=1,sticky="news",pady=6,padx=6)
    quiz.mainloop()



