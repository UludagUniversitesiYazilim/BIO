import tkinter as tk
import random
import GetData
import time
from tkinter import filedialog
import threading
import itertools

def callback(path):
    d = GetData.get_datas(path)
    d, d_backup = itertools.tee(d)
    v = 0
    for i in d_backup:
        for j in i:
            v = v+1
    counter = 0
    main.b.configure(text="\nPlease wait... ("+str(counter)+"/"+str(v)+")\n",fg = "red")
    for i in d: # Her adimda 5 adet Reponse iceren bir liste doner


        for j in i: # listenin icindeki tum nesneler baslatilir.
            j.start()
            print("isim {}. site: {}".format(j.name, j.site))
        
        
        
        
        while len(i) > 0:
            
            for j in i:
                if j.state == True: # Dizideki her elemani durumu true mu diye kontrol ediyorum
                    main.dic[j.name] = j.response
                    if not j.name in main.lbc.list:    
                        main.lbc.list.append(j.name)
                        main.lbc.listBox.insert("end",j.name)
                    print(j.name+ ":")
                    print(j.response+'\n\n')
                    counter = counter + 1
                    main.b.configure(text="\nPlease wait... ("+str(counter)+"/"+str(v)+")\n")
                    i.remove(j) # Isi biten ciksin kasiyo
                    
            time.sleep(0.2) # Bilgisayar cevaplari beklerken cok yorulmasin
    main.b.configure(text="\nDone!\n",fg = "blue")
	
def callback2(path):
    d = GetData.get_datas(path)
    v = 1
    counter = 0
    name = main.lbc.value
    main.b.configure(text="\nPlease wait... ("+str(counter)+"/"+str(v)+")\n",fg = "red")
    for i in d: # Her adimda 5 adet Reponse iceren bir liste doner
        for j in i: # listenin icindeki tum nesneler baslatilir.
            if(j.name == name):
                j.start()
                print("isim {}. site: {}".format(j.name, j.site))
                while True:
                    if j.state == True:
                        main.dic[j.name] = j.response
                        print(j.name+ ":")
                        print(j.response+'\n\n')
                        main.b.configure(text="\nDone!\n",fg = "blue")
                        return
                    time.sleep(0.2)

class ListBoxChoice(object):
    def __init__(self, master=None):
        self.master = master
        self.value = None
        self.modalPane = self.master
        self.list = []
        self.modalPane.grab_set()

        self.modalPane.bind("<Return>", self._choose)


        listFrame = tk.Frame(self.modalPane)
        listFrame.pack(side="left", padx=5, pady=5)
        
        scrollBar = tk.Scrollbar(listFrame)
        scrollBar.pack(side="right", fill="y")
        self.listBox = tk.Listbox(listFrame, selectmode="single")
        self.listBox.pack(side="left", fill="y")
        scrollBar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scrollBar.set)
        self.list.sort()
        for item in self.list:
            self.listBox.insert("end", item)

        buttonFrame = tk.Frame(self.modalPane)
        buttonFrame.pack(side="left")

        chooseButton = tk.Button(buttonFrame, text="Choose", command=self._choose)
        chooseButton.pack()

    def _choose(self, event=None):
        try:
            firstIndex = self.listBox.curselection()[0]
            self.value = self.list[int(firstIndex)]
            self.master.result(self.value)
            print(self.value)
        except IndexError:
            self.value = None

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        

        self.b = tk.Label(self, text='\nPlease choose file from \'File\' menu.\n', fg = "red")
        self.b.pack(side="top")
        
        self.dic = {}
        
        self.lbc = ListBoxChoice(self)

        scrollBar = tk.Scrollbar(self)
        scrollBar.pack(side="right", fill="y", padx=(0,5), pady=5)
        self.T = tk.Text(self, height=4, width=3000, wrap=tk.WORD)
        self.T.pack(side="left", fill="y", padx=(5,0), pady=5)
        scrollBar.config(command=self.T.yview)
        self.T.config(yscrollcommand=scrollBar.set)
        quote = """Select a name from left list to see the result."""
        self.T.insert("end", quote)
    def result(self, value):
        quote = self.dic[value]
        self.T.delete('1.0', "end")
        self.T.insert("end", quote)
            
if __name__ == "__main__":
    root = tk.Tk()
    root.title("BIO")
    def cf():
            global filepath
            filepath = filedialog.askopenfilename(initialdir = "../",title = "Choose file")
            t = threading.Thread(target=callback, args=(filepath,))
            t.start()
    def gr():
            global filepath
            t = threading.Thread(target=callback, args=(filepath,))
            t.start()

    def gsr():
        global filepath
        t = threading.Thread(target=callback2, args=(filepath,))
        t.start()

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Choose File", command=cf)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Get Results Again", command=gr)
    editmenu.add_command(label="Get Selected Result Again", command=gsr)
    menubar.add_cascade(label="Options", menu=editmenu)
    root.config(menu=menubar)

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x400")
    root.mainloop()
