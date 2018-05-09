import tkinter as tk
from GetData import *
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   entries = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Gene:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Transcript:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Position / snippet refers to:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)
       
       l = tk.Label(self, text="Enter a few bases around your alteration:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter position:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter new base:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter position of last wild type base before alteration:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter position of first wild type base after alteration:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter positions of  inserted bases:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)
class Page2(Page):
   entries = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Protein or SNP identifier:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Protein sequence in FASTA format:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Position:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Substitution(AA1):").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Substitution(AA2):").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

class Page3(Page):
   entries = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Protein sequence:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)

       l = tk.Label(self, text="Enter the substitutions of interest:").pack(side="top", fill="both", expand=True)
       e = tk.Entry(self)
       e.pack(side="top", fill="both", expand=True, padx=20)
       self.entries.append(e)
       
class Page4(Page):
   labels = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Result:").pack(side="top", fill="both", expand=True)
       s = tk.Label(self, text="Result")
       s.pack(side="top", fill="both", expand=True)
       self.labels.append(s)
class Page5(Page):
   labels = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Result:").pack(side="top", fill="both", expand=True)
       s = tk.Label(self, text="Result")
       s.pack(side="top", fill="both", expand=True)
       self.labels.append(s)
class Page6(Page):
   labels = []
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       l = tk.Label(self, text="Result:").pack(side="top", fill="both", expand=True)
       s = tk.Label(self, text="Result")
       s.pack(side="top", fill="both", expand=True)
       self.labels.append(s)
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.p1 = Page1(self)
        self.p2 = Page2(self)
        self.p3 = Page3(self)

        self.p4 = Page4(self)
        self.p5 = Page5(self)
        self.p6 = Page6(self)
        
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.b1 = tk.Button(buttonframe, text="MutationTaster", command=self.p1.lift)
        self.b2 = tk.Button(buttonframe, text="PolyPhen2", command=self.p2.lift)
        self.b3 = tk.Button(buttonframe, text="SIFT", command=self.p3.lift)

        self.b1.pack(side="left", expand=True, fill="x")
        self.b2.pack(side="left", expand=True, fill="x")
        self.b3.pack(side="left", expand=True, fill="x")

        bottomframe = tk.Frame(self).pack(side="top", fill="x", expand=False)
        self.b4 = tk.Button(bottomframe, text="OK", command=self.results)
        self.b4.pack(side="bottom", pady=10)

        self.p1.show()
        
    def results(self):
        arr = []
        arr.append("mt")
        for i in Page1.entries:
            arr.append(i.get())
            
        d = get_data(arr)
        Page4.labels[0].configure(text=d)
        
        arr = []
        arr.append("pp")
        for i in Page2.entries:
            arr.append(i.get())
        arr.append("")
        d = get_data(arr)
        Page5.labels[0].configure(text=d)
        """
        arr = []
        arr.append("st")
        for i in Page3.entries:
            arr.append(i.get())
        
        d = get_data(arr)
        Page6.labels[0].configure(text=d)
        """
        self.b4.configure(text="New Query", command=self.queries)
        self.p4.show()
        self.b1.configure(command=self.p4.lift)
        self.b2.configure(command=self.p5.lift)
        self.b3.configure(command=self.p6.lift)

    def queries(self):
        self.b4.configure(text="OK", command=self.results)
        self.p1.show()
        self.b1.configure(command=self.p1.lift)
        self.b2.configure(command=self.p2.lift)
        self.b3.configure(command=self.p3.lift)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x800")
    root.mainloop()
