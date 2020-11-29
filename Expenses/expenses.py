import tkinter as tk
import tkinter.ttk as ttk
from DAO import dao

dao = dao.DAO()

def input_gui():
    def display_button():
        root.destroy()
        display_gui()
    
    def exit_button():
        root.destroy()
    
    def entry_button(item_name):
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

    frame = tk.LabelFrame(root, bd=2, relief='ridge', text='menu')
    frame.pack(fill='x')

    button1 = tk.Button(frame, text='input')
    button1.pack(side='left')
    button2 = tk.Button(frame, text='display',command=display_button)
    button2.pack(side='left')
    button3 = tk.Button(frame, text='exit',command=exit_button)
    button3.pack(side='right')

    label1 = tk.Label(root, text='【Input】', font=('', 16), height=2)
    label1.pack(fill='x')

    frame1 = tk.Frame(root, pady=10)
    frame1.pack()
    label2 = tk.Label(frame1, text='Date', font=('', 12))
    label2.pack(side='left')
    entry1 = tk.Entry(frame1, font=('', 12), justify='center', width=15)
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

    button4 = tk.Button(root, text='Entry', font=('', 16),
                        width=10, bg='gray', command=lambda: entry_button(combo.get()))
    button4.pack()

    root.mainloop()

def display_gui():
    def input_button():
        root.destroy()
        input_gui()
        
    def exit_button():
        root.destroy()

    def display_button(start_date, end_date):
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

    button1 = tk.Button(frame, text='input',command=input_button)
    button1.pack(side='left')
    button2 = tk.Button(frame, text='display')
    button2.pack(side='left')
    button3 = tk.Button(frame, text='exit',command=exit_button)
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

    button4 = tk.Button(root, text='Display', font=('', 16), width=10,
                        bg="gray", command=lambda: display_button(entry1.get(), entry2.get()))
    button4.pack()
    tree = ttk.Treeview(root)

    tree['column'] = (1, 2, 3)
    tree['show'] = 'headings'

    tree.column(1, width=75)
    tree.column(2, width=75)
    tree.column(3, width=100)

    tree.heading(1, text='Date')
    tree.heading(2, text='Detail')
    tree.heading(3, text='Amount')

    style = ttk.Style()
    style.configure('Treeview', font=('', 12))
    style.configure('Treeview.Heading', font=('', 14, 'bold'))


    i = 0
    for r in dao.get_acc():
        r = (r[0], r[1], "¥{:,d}".format(r[2]))
        tree.insert('', 'end', tags=i, values=r)
        if 1 & i:
            tree.tag_configure(i, background='#CCFFFF')
        i += 1

    tree.pack()
    root.mainloop()

if __name__ == '__main__':
    input_gui()
