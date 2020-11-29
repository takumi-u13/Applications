import tkinter as tk
import tkinter.ttk as ttk
from DAO import dao

dao = dao.DAO()

def select(start_date, end_date):
    tree.delete(*tree.get_children())

    if start_date == '':
        start_date = '1900/01/01'
    if end_date == '':
        end_date = '2200/01/01'
    i = 0
    for r in dao.select_acc_data(start_date, end_date):
        r = (r[0], r[1], "¥{:,d}".format(r[2]))
        tree.insert('', 'end', tags=i, values=r)
        if i & 1:
            tree.tag_configure(i, background='#CCFFFF')
        i += 1
        
        
root = tk.Tk()
root.title('Household Expenses')
root.geometry('400x400')

frame = tk.LabelFrame(root, bd=2, relief='ridge', text='menu')
frame.pack(fill='x')

button1 = tk.Button(frame, text='input')
button1.pack(side='left')
button2 = tk.Button(frame, text='display')
button2.pack(side='left')
button3 = tk.Button(frame, text='exit')
button3.pack(side='right')

label1 = tk.Label(root, text='【Display】', font=('', 16), height=2)
label1.pack(fill='x')

frame1 = tk.Frame(root, pady=15)
frame1.pack()
label2 = tk.Label(frame1, text='Duration', font=('', 14))
label2.pack(side='left')
entry1 = tk.Entry(frame1, font=('', 14), justify='center', width=12)
entry1.pack(side='left')
label3 = tk.Label(frame1, text='〜', font=('', 14))
label3.pack(side='left')
entry2 = tk.Entry(frame1, font=('', 14), justify='center', width=12)
entry2.pack(side='left')

button4 = tk.Button(root, text='Display', font=('', 16),width=10,bg="gray",command=lambda:select(entry1.get(),entry2.get()))
button4.pack()
tree = ttk.Treeview(root)

tree['column'] = (1,2,3)
tree['show'] = 'headings'

tree.column(1,width=75)
tree.column(2, width=75)
tree.column(3, width=100)

tree.heading(1,text='Date')
tree.heading(2, text='Detail')
tree.heading(3, text='Amount')

style = ttk.Style()
style.configure('Treeview',font=('', 12))
style.configure('Treeview.Heading',font=('', 14,'bold'))


i=0
for r in dao.get_acc():
    r = (r[0], r[1], "¥{:,d}".format(r[2]))
    tree.insert('','end',tags=i,values=r)
    if 1&i:
        tree.tag_configure(i,background='#CCFFFF')
    i+=1

tree.pack()
root.mainloop()


