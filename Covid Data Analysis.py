#COVID DATA ANALYSIS
  
from tkinter import *  
import wikipedia  
import tkinter  
from covid import Covid  
covid=Covid()  
window=tkinter.Tk()  
window.title('TrackCOVID')  
window.geometry('800x800')  
window.configure(bg='turquoise')  
t=Text(window, height=1 ,width=30,bg='turquoise', bd=0, fg='DarkOliveGreen', font=('Cooper Black',72))  
name='TRACK COVID'  
t.insert(END, name)  
t.pack(side='top', anchor='ne')  
frame=tkinter.Frame(window).pack()  
def about():  
    top0=Toplevel(bg='orange')  
    top0.title("ABOUT COVID-19 DISEASE")  
    cov=wikipedia.summary('Coronavirus Disease 2019')  
    text0=Text(top0, height=28, width=100,font=('Kristen ITC', 12))  
    texth=Text(top0, height=1, width=22,bg='orange',bd='0',font=('Lucida Handwriting', 20))  
    texth.insert(END, 'Coronavirus Disease 2019')  
    texth.pack()  
    text0.insert(END, cov)  
    text0.pack(side='top', anchor='n')  
      
b1=tkinter.Button(frame, text='ABOUT', fg='red', bg='yellow', activebackground='Blue', height=5, width=30, font=('ms sans serif',16), command=about).pack(side='top', anchor='n')  
  
  
def track():  
    top1=Toplevel(bg='green' )  
    top1.title("INFORMATION BY COUNTRY")  
    text1=Text(top1, height=30,width=70,font='Cambria')  
    countries = covid.list_countries()  
    text1.insert(END, countries)  
    text1.pack(side='top', anchor='n')  
    cc=tkinter.Label(top1, text='Enter Country ID').pack(side='top', anchor='n')  
    e=tkinter.Entry(top1, bd=5, font='Cambria', relief='ridge')  
    e.pack(side='top', anchor='n')  
    def display():  
        file=open('Results.txt', 'a')  
        top2=Toplevel(bg='dark green')  
        top2.title('RESULTS')  
        x=e.get()  
        l=tkinter.Label(top2, text=x).pack(side='top', anchor='n')  
        txt=Text(top2, fg='dark slate gray', height=15,width=50)  
        data=covid.get_status_by_country_id(x)  
        file.write(str(data))  
        file.close()  
        txt.insert(END, data)  
        txt.pack()  
          
          
          
    b=tkinter.Button(top1, text='GO', command=display).pack()  
     
      
b2=tkinter.Button(frame, text='TRACK', fg='green' , bg='yellow', activebackground='Blue', height=5, width=30, font=('ms sans serif',16), command=track).pack(side='top', anchor='n')  
  
  
def donate():  
    top3=Toplevel(bg='hotpink')  
    top3.title('DONATIONS AND RELIEF FUNDS')  
    head=Text(top3, bg='hotpink',fg='forestgreen', height=1, width=80, bd=0, font=('times new roman', 40))  
    txt1=Text(top3, bg='hotpink', fg='Navy', height=1, width=80, bd=0, font=('times new roman', 20))  
    txt2=Text(top3, bg='hotpink', fg='Navy', height=1, width=80, bd=0, font=('times new roman', 20))  
    txt3=Text(top3, bg='hotpink', fg='Navy', height=1, width=80, bd=0, font=('times new roman', 20))  
    txt4=Text(top3, bg='hotpink', fg='Navy', height=1, width=80, bd=0, font=('times new roman', 20))  
    txt5=Text(top3, bg='hotpink', fg='Navy', height=1, width=80, bd=0, font=('times new roman', 20))  
    fund1='WHO - https://covid19responsefund.org/en/ '  
    fund2='PM CARE FUNDS - https://www.pmcares.gov.in/en/#'  
    fund3='HELPAGE INDIA - https://www.helpageindia.org/covid-19/'  
    fund4='INDIAN RED CROSS SOCIETY - https://indianredcross.org/ircs/donatenow'  
    fund5='GLOBAL GIVING - https://www.globalgiving.org/projects/coronavirus-relief-fund/'  
    head.insert(END, 'You can make a donation on these websites -')  
    txt1.insert(END, fund1)  
    txt2.insert(END, fund2)  
    txt3.insert(END, fund3)  
    txt4.insert(END, fund4)  
    txt5.insert(END, fund5)  
    head.pack()  
    txt1.pack()  
    txt2.pack()  
    txt3.pack()  
    txt4.pack()  
    txt5.pack()  
      
b3=tkinter.Button(frame,text='DONATIONS AND RELIEF FUNDS',fg='Deep pink',bg='yellow',activebackground='Blue' ,height=5,width=30, font=('ms sans serif',16), command=donate)  
b3.pack(side='top', anchor='n')  
  
def feedback():  
    top4=Toplevel(bg='Chartreuse' )  
    top4.title("FEEDBACK")  
    text4=Text(top4, height=1,width=100,font=('Cooper Black',40))  
    b1=tkinter.Label(top4, text='Name').pack(side='top', anchor='nw')  
    e1=tkinter.Entry(top4, bd=5, font='Cambria', width=20)  
    e1.pack(side='top', anchor='n')  
    b2=tkinter.Label(top4, text='Feedback').pack(side='top', anchor='nw')  
    e2=tkinter.Entry(top4, bd=5, font='Cambria', width=50)  
    e2.pack(side='top', anchor='n')  
    def save():  
        file=open('feedback.txt', 'a')  
        m=e1.get()  
        file.write(m)  
        n=e2.get()  
        file.write(n)  
        file.close()  
    btn=tkinter.Button(top4, text='SAVE', command=save).pack()  
      
b4=tkinter.Button(frame, text='FEEDBACK', fg='blue', height=5, width=30,bg='yellow', activebackground='Blue', font=('ms sans serif',16), command=feedback)  
b4.pack(side='top', anchor='n')    
window.mainloop()  

