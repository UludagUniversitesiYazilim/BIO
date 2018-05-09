import GetData
import time
from tkinter import *

import threading
def callback():
    for i in GetData.get_datas("../input/input"): # Her adimda 5 adet Reponse iceren bir liste doner


        for j in i: # listenin icindeki tum nesneler baslatilir.
            j.start()
            print("isim {}. site: {}".format(j.name, j.site))
        
        
        
        
        while len(i) > 0:
            
            for j in i:
                if j.state == True: # Dizideki her elemani durumu true mu diye kontrol ediyorum
                    a.configure(text=a.cget("text")+j.name+'\n'+j.response+"\n\n"+'-'*7+'\n')
                    print(j.name+ ":")
                    print(j.response+'\n\n')
                    i.remove(j) # Isi biten ciksin kasiyo
                    
            time.sleep(0.2) # Bilgisayar cevaplari beklerken cok yorulmasin
        b.configure(text="\nDone!\n",fg = "blue")


root = Tk()
b = Label(root, text='\nPlease wait...\n', fg = "red")
b.pack()
a = Label(root, text='')
a.pack()
t = threading.Thread(target=callback)
t.start()
root.mainloop()
