from DAO import dao
import tkinter as tk
import tkinter.ttk as ttk

from googletrans import Translator

dao = dao.DAO()
translator = Translator()
def translate_gui():
    def exit_button():
        root.destroy()
    def saved_button():
        root.destroy()
        saved_gui()

    def translate_en2ja():
        en_word = str(entry1.get("1.0", "end"))
        translated_word = translator.translate(en_word, dest="ja")
        print(en_word)
        print(translated_word.text)
        dao.save_word(en_word, translated_word.text)
    root = tk.Tk()
    root.title('Translation')
    root.geometry('400x400')

    frame = tk.LabelFrame(root, bd=2, relief='ridge', text='menu')
    frame.pack(fill='x')

    button1 = tk.Button(frame, text='translation')
    button1.pack(side='left')
    button2 = tk.Button(frame, text='saved',command=saved_button)
    button2.pack(side='left')
    button3 = tk.Button(frame, text='exit',command=exit_button)
    button3.pack(side='right')

    label1 = tk.Label(root, text='【Translation】', font=('', 16), height=2)
    label1.pack(fill='x')

    frame1 = tk.Frame(root, pady=10)
    frame1.pack()
    label2 = tk.Label(frame1, text='Input Word:', font=('', 12))
    label2.pack(side='left')
    entry1 = tk.Text(frame1, font=('', 12), width=90, height=6, bg='#dcecec')
    entry1.pack(side='right')

    frame2 = tk.Frame(root, pady=10)
    frame2.pack()
    label3 = tk.Label(frame2, text='Translated Word:', font=('', 12))
    label3.pack(side='left')
    entry2 = tk.Text(frame2, font=('', 12), width=100, height=6, bg='#fce0e9')
    entry2.pack(side='right')

    button4 = tk.Button(root, text='translate', font=('', 16), width=10, bg='#1b5af9',command=translate_en2ja)
    button4.pack(side='right')

    root.mainloop()


def saved_gui():
    def exit_button():
        root.destroy()

    def translate_button():
        root.destroy()
        translate_gui()
        
    root = tk.Tk()
    root.title('Translation')
    root.geometry('400x400')

    frame = tk.LabelFrame(root, bd=2, relief='ridge', text='menu')
    frame.pack(fill='x')

    button1 = tk.Button(frame, text='translation',command=translate_button)
    button1.pack(side='left')
    button2 = tk.Button(frame, text='saved')
    button2.pack(side='left')
    button3 = tk.Button(frame, text='exit', command=exit_button)
    button3.pack(side='right')

    label1 = tk.Label(root, text='【Saved word】', font=('', 16), height=2)
    label1.pack(fill='x')
    
    tree = ttk.Treeview(root)


    tree['column'] = (1, 2)
    tree['show'] = 'headings'

    tree.column(1, width=150)
    tree.column(2, width=150)

    tree.heading(1, text='English word')
    tree.heading(2, text='Japanese word')

    style = ttk.Style()
    style.configure('Treeview', font=('', 12))
    style.configure('Treeview.Heading', font=('', 14, 'bold'))


    i = 0
    for r in dao.get_data():
        tree.insert('', 'end', tags=i, values=r)
        if 1 & i:
            tree.tag_configure(i, background='#CCFFFF')
        i += 1

    tree.pack()
    root.mainloop()
    
if __name__ == '__main__':
    translate_gui()
