import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import datetime

root = tk.Tk()
root.title("Calorie Tracker")
root.geometry("300x350")

now=datetime.datetime.now()
date=now.strftime("%d-%m-%y")
tk.Label(root,text=date,fg="#333333",relief="groove").pack()

tk.Label(root,text="Food Name:").pack()
name_entry=tk.Entry(root)
name_entry.pack()

tk.Label(root,text="Calorie:").pack()
calorie_entry=tk.Entry(root)
calorie_entry.pack()

class Calorie:
    def save(self):
        self.date=date
        self.name=name_entry.get()
        self.calorie=calorie_entry.get()
        luffy=pd.DataFrame([[self.date,self.name,self.calorie]],columns=("DATE","FOOD","CALORIES"))
        luffy.to_csv("history.csv",mode="a",index=False,header=False)
    def graph(self):
        df=pd.read_csv("history.csv")
        df["CALORIES"]=pd.to_numeric(df["CALORIES"],errors="coerce")
        group=df.groupby("DATE")["CALORIES"].sum()
        plt.bar(group.index,group.values,color="#1C3B41")
        plt.xlabel("DATE")
        plt.ylabel("TOTAL CALORIES")
        plt.title("calories")
        plt.show()
        
l1=Calorie()

tk.Button(root,text="SAVE",command=l1.save,background="#2d3436",fg="#dfe6e9").pack(pady=5)
tk.Button(root,text="ANALYZE",command=l1.graph,bg="#30306E",fg="white").pack(pady=5)

tk.mainloop()