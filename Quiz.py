#QUIZ

from tkinter import * 
from tkinter import ttk 
 
def main(): 
 
    notebook.add(frame1, text="Q1.") 
    notebook.add(frame2, text="Q2.") 
    notebook.add(frame3, text="Q3.") 
    notebook.add(frame4, text="Q4.") 
    notebook.add(frame5, text="Q5.") 
 
 
    Label(frame1, text="Which Indian state reported first case of Covid19?",bg="blue",fg="white").grid(row=2, column=3) 
    Button(frame1, text="MAHARASHTRA", command=incorrect1,bg="brown",fg="white").grid(row=3, column=1) 
    Button(frame1, text="KERALA", command=correct1,bg="brown",fg="white").grid(row=3, column=2) 
    Button(frame1, text="KARNATAKA", command=incorrect1,bg="brown",fg="white").grid(row=3, column=3) 
    Button(frame1, text="DELHI", command=incorrect1,bg="brown",fg="white").grid(row=3, column=4) 
     
    Label(frame2, text="How long does novel coronavirus survive outside the body?",bg="green",fg='white').grid(row=2, column=2) 
    Button(frame2, text="A WEEK IN AIR OR ON SURFACES", command=incorrect2,bg="orange",fg="white").grid(row=3, column=1) 
    Button(frame2, text="SEVERAL HOURS TO DAYS", command=correct2,bg="orange",fg="white").grid(row=3, column=2) 
    Button(frame2, text="UPTO TWO AND A HALF WEEKS", command=incorrect2,bg="orange",fg="white").grid(row=3, column=3) 
 
    Label(frame3, text="Do antibiotics work against coronavirus?",bg="red",fg="white").grid(row=2, column=4) 
    Button(frame3, text="NO", command=correct3,bg="violet",fg="white").grid(row=3, column=5) 
    Button(frame3, text="YES", command=incorrect3,bg="violet",fg="white").grid(row=3, column=3) 
 
    Label(frame4, text="How much distance should one maintain from others to prevent the spread of covid19 disease?",bg="light blue",fg="blue").grid(row=2, column=2) 
    Button(frame4, text="5 feet", command=incorrect4,bg="purple",fg="white").grid(row=3, column=1) 
    Button(frame4, text="3 feet", command=correct4,bg="purple",fg="white").grid(row=3, column=2) 
    Button(frame4, text="1 feet", command=incorrect4,bg="purple",fg="white").grid(row=3, column=3) 
    Button(frame4, text="2feet", command=incorrect4,bg="purple",fg="white").grid(row=3, column=4) 
 
    Label(frame5, text="What is a fomite?",bg="brown",fg="white").grid(row=2, column=2) 
    Button(frame5, text="A HOSPITAL GRADE DISINFECTANT", command=incorrect5,bg="dark blue",fg="white").grid(row=3, column=1) 
    Button(frame5, text="DISEASE CARRIER", command=incorrect5,bg="dark blue",fg="white").grid(row=3, column=2) 
    Button(frame5, text="CONTAMINATED OBJECT OR SURFACE", command=correct5,bg="dark blue",fg="white").grid(row=3, column=3) 
    Button(frame5, text="IMMUNITY BOOSTING SUPPLEMENT", command=incorrect5,bg="dark blue",fg="white").grid(row=3, column=4) 
 
     
 
    notebook.pack() 
 
    Label(root, text="Total:").pack() 
    Label(root, textvariable=total).pack() 
 
def correct1(): 
    Label(frame1, text="Correct  :)").grid(row=1, column=3) 
    counter() 
 
def incorrect1(): 
    Label(frame1, text="Incorrect   :o").grid(row=1, column=3) 
 
def correct2(): 
    Label(frame2, text="Correct   :)").grid(row=1, column=2) 
    counter() 
 
def incorrect2(): 
    Label(frame2, text="Incorrect   :o").grid(row=1, column=2) 
 
def correct3(): 
    Label(frame3, text="Correct   :)").grid(row=1, column=4) 
    counter() 
 
def incorrect3(): 
    Label(frame3, text="Incorrect   :o").grid(row=1, column=4) 
 
def correct4(): 
    Label(frame4, text="Correct  :)").grid(row=1, column=2) 
    counter() 
 
def incorrect4(): 
    Label(frame4, text="Incorrect   :o").grid(row=1, column=2) 
 
def correct5(): 
    Label(frame5, text="Correct   :)").grid(row=1, column=2) 
    counter() 
 
def incorrect5(): 
    Label(frame5, text="Incorrect   :o").grid(row=1, column=2) 
 
 
 
def counter(): 
    total.set(total.get() + 1) 
 
root = Tk() 
 
total = IntVar()  # defaults to 0 
 
notebook = ttk.Notebook(root) 
 
frame1 = ttk.Frame(notebook) 
frame2 = ttk.Frame(notebook) 
frame3 = ttk.Frame(notebook) 
frame4 = ttk.Frame(notebook) 
frame5 = ttk.Frame(notebook) 
 
main() 
 
root.mainloop() 
