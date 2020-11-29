from datetime import datetime
import os
import wx


def click_save_button(event):
    date_now = datetime.now()
    year = date_now.strftime('%Y')
    file_date = date_now.strftime('%m-%d')
    if(not os.path.exists(year)):
        os.mkdir(os.path.join(os.path.dirname(__file__), year))
    save_file = open(os.path.join(year,file_date+'.txt'), 'w') 
    save_file.write(text.GetValue()) 
    save_file.close()


if __name__ == '__main__':
    window = wx.App() 
    frame = wx.Frame(None, -1, 'diary', size=(500, 250))

    panel = wx.Panel(frame, -1) 
    save_button = wx.Button(panel, -1, pos=(10, 10), label='Save')

    text = wx.TextCtrl(panel, -1, pos=(10, 50), size=(465, 150),
                       style=wx.TE_MULTILINE)  
    save_button.Bind(wx.EVT_BUTTON, click_save_button)
    window.MainLoop()

#追加項目
# Saveボタンを押したらテキストboxの文字が消える
#　Saveできたら"It's saved"と表示
