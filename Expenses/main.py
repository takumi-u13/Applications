import tkinter as tk
import tkinter.ttk as ttk
from DAO import dao

dao = dao.DAO()


def insert(item_name):
    acc_date = entry1.get()
    # item = entry2.get()
    amount = entry3.get()

    dao.insert(acc_date, item_name, amount)


def create_item_name():
    item_list = dao.get_item_list()
    return tuple(item_list)


root = tk.Tk()
root.title('Household Expenses')
root.geometry('400x400')

frame = tk.LabelFrame(root,bd=2,relief='ridge',text='menu')
frame.pack(fill='x')

button1 = tk.Button(frame, text='input')
button1.pack(side='left')
button2 = tk.Button(frame, text='display')
button2.pack(side='left')
button3 = tk.Button(frame, text='exit')
button3.pack(side='right')

label1 = tk.Label(root, text='【Input】',font=('',16),height=2)
label1.pack(fill='x')
 
frame1 = tk.Frame(root,pady=10)
frame1.pack()
label2 = tk.Label(frame1, text='Date', font=('', 12))
label2.pack(side='left')
entry1 = tk.Entry(frame1,font=('', 12),justify='center',width=15)
entry1.pack(side='right')

frame2 = tk.Frame(root, pady=10)
frame2.pack()
label3 = tk.Label(frame2, text='Detail', font=('', 12))
label3.pack(side='left')
# entry2 = tk.Entry(frame2, font=('', 12), justify='center', width=15)
# entry2.pack(side='right')
combo = ttk.Combobox(frame2, state='readonly', font=('', 12), width=13)
combo['values'] = create_item_name()
combo.current(0)
combo.pack()

frame3 = tk.Frame(root, pady=10)
frame3.pack()
label4 = tk.Label(frame3, text='Amount', font=('', 12))
label4.pack(side='left')
entry3 = tk.Entry(frame3, font=('', 12), justify='center', width=15)
entry3.pack(side='right')

button4 = tk.Button(root, text='Entry', font=('', 16),width=10, bg='gray', command=lambda:insert(combo.get()))
button4.pack()

root.mainloop()



