from tkinter import *
window=Tk()

window.title("Simple Interest Calculator")
window.geometry("380x400")
window.configure(bg='grey')

app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

def calculateInterest():
    principle_amount = float(prin.get())
    interest_rate = float(inter.get())
    time = float(years.get())
    si = (principle_amount*interest_rate*time)/100
    si = round(si, 2)
    result_label.destroy()
    output_msg = Label(result_frame, text=" Your Simple Interest is "+ str(si), fg="black", bg="lightcyan", font=("Calibri", 12), width=45)
    output_msg.place(x=20, y=40)    
    output_msg.pack()


p_label=Label(window, text="Principle amount", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
p_label.place(x=20, y=140)

prin=Entry(window, text="", bd=2, width=22)
prin.place(x=150, y=142)

inte_label=Label(window, text="Interest Rate(in %)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
inte_label.place(x=20, y=180)

inter=Entry(window, text="", bd=2, width=22)
inter.place(x=150, y=182)

year_label=Label(window, text="Years", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
year_label.place(x=20, y=220)

years=Entry(window, text="", bd=2, width=22)
years.place(x=150, y=222)

calculateButton = Button(window, text="Calculate", fg ="black", bg = "lightcyan", bd=1, command=calculateInterest)
calculateButton.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()