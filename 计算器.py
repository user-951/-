from tkinter import *
from math import *
q=''
m=0
t=0
def func(r):
    d['state']='normal'
    d.delete(0,END) 
    global q
    q=q+r
    d.insert(0,q)
    d['state']='disabled'
def equal():
    d['state']='normal'
    d.delete(0,END)
    global q
    exec('q=str('+q+')',globals())
    d.insert(0,q)
    d['state']='disabled'
def clearall():
    d['state']='normal'
    d.delete(0,END)
    global q
    q=''
    d.insert(0,q)
    d['state']='disabled'
def clearentry():
    d['state']='normal'
    d.delete(0,END)
    global q
    q=q[:-1]
    d.insert(0,q)
    d['state']='disabled'
def memory(r):
    d['state']='normal'
    global q,m
    if r=='+'and q!='': exec('m=m+'+q,globals())
    elif r=='-'and q!='': exec('m=m-'+q,globals())
    elif r=='r':
        if q!='':
            y=0
            for x in range(10):
                if q[-1]==str(x):y=1
            if q[-1]=='.':y=1
            if y==0:d.insert(END,m)
        else:
            q=str(m)
            d.insert(END,m)
    elif r=='c': m=0
    d['state']='disabled'

def science():
    global t,f14_1,f14_2,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,n11,n12
    if t==0:
        a.title('scientific calculator')
        a.geometry('830x350')
        a.minsize(830,350)
        a.maxsize(1500,350)
        f14_2=Button(a,text='SC',command=science,font=5,width=5,height=12,background='purple')
        f15=Button(a,text='sin',command=lambda :func('sin('),font=5,width=5,height=2,background='blue')
        f16=Button(a,text='cos',command=lambda :func('cos('),font=5,width=5,height=2,background='blue')
        f17=Button(a,text='tan',command=lambda :func('tan('),font=5,width=5,height=2,background='blue')
        f18=Button(a,text='sqrt',command=lambda :func('sqrt('),font=5,width=5,height=2,background='purple')
        f19=Button(a,text='log',command=lambda :func('log('),font=5,width=5,height=2,background='purple')
        f20=Button(a,text='log10',command=lambda :func('log10('),font=5,width=5,height=2,background='purple')
        f21=Button(a,text='x2',command=lambda :func('**2'),font=5,width=5,height=2,background='blue')
        f22=Button(a,text='pow',command=lambda :func('**'),font=5,width=5,height=2,background='blue')
        f23=Button(a,text='%',command=lambda :func('%'),font=5,width=5,height=2,background='blue')
        f24=Button(a,text='fac',command=lambda :func('factorial('),font=5,width=5,height=2,background='purple')
        f25=Button(a,text='exp',command=lambda :func('exp('),font=5,width=5,height=2,background='purple')
        f26=Button(a,text='rad',command=lambda :func('radians('),font=5,width=5,height=2,background='purple')
        n11=Button(a,text='e',command=lambda :func(str(e)),font=5,width=5,height=2,background='white')
        n12=Button(a,text='pi',command=lambda :func(str(pi)),font=5,width=5,height=2,background='white')

        f14_1.destroy()
        f14_2.grid(row=1,rowspan=5,column=6,sticky=E)
        f15.grid(row=1,column=7,sticky=E)
        f16.grid(row=1,column=8,sticky=E)
        f17.grid(row=1,column=9,sticky=E)
        f18.grid(row=1,column=10,sticky=E)
        f19.grid(row=1,column=11,sticky=E)
        f20.grid(row=1,column=12,sticky=E)
        f21.grid(row=2,column=7,sticky=E)
        f22.grid(row=2,column=8,sticky=E)
        f23.grid(row=2,column=9,sticky=E)
        f24.grid(row=2,column=10,sticky=E)
        f25.grid(row=2,column=11,sticky=E)
        f26.grid(row=2,column=12,sticky=E)
        n11.grid(row=3,column=7,sticky=E)
        n12.grid(row=3,column=8,sticky=E)
        t=1
    else:
        a.title('standard calculator')
        a.geometry('450x350')
        a.minsize(450,350)
        a.maxsize(1500,350)
        f14_1=Button(a,text='SC',command=science,font=5,width=5,height=12,background='purple')
        f14_2.destroy()
        f14_1.grid(row=1,rowspan=5,column=6,sticky=E)
        f15.destroy()
        f16.destroy()
        f17.destroy()
        f18.destroy()
        f19.destroy()
        f20.destroy()
        f21.destroy()
        f22.destroy()
        f23.destroy()
        f24.destroy()
        f25.destroy()
        f26.destroy()
        n11.destroy()
        n12.destroy()
        t=0
    

a=Tk()
a.title('standard calculator')
a.geometry('450x350')
a.minsize(450,350)
a.maxsize(1500,350)
d=Entry(a,state='disabled',width=68,font=('Helvetica','30','bold'))
d.grid(row=0,columnspan=100,sticky=E)
f1=Button(a,text='+',command=lambda :func('+'),font=5,width=5,height=2,background='gold')
f2=Button(a,text='-',command=lambda :func('-'),font=5,width=5,height=2,background='gold')
f3=Button(a,text='*',command=lambda :func('*'),font=5,width=5,height=2,background='gold')
f4=Button(a,text='/',command=lambda :func('/'),font=5,width=5,height=2,background='gold')
f5=Button(a,text='=',command=equal,font=5,width=5,height=2,background='green')
f6=Button(a,text='AC',command=clearall,font=5,width=5,height=2,background='yellow')
f7=Button(a,text='(',command=lambda :func('('),font=5,width=5,height=2,background='silver')
f8=Button(a,text=')',command=lambda :func(')'),font=5,width=5,height=2,background='silver')
f9=Button(a,text='CE',command=clearentry,font=5,width=5,height=2,background='yellow')
f10=Button(a,text='M+',command=lambda :memory('+'),font=5,width=5,height=2,background='blue')
f11=Button(a,text='M-',command=lambda :memory('-'),font=5,width=5,height=2,background='blue')
f12=Button(a,text='MR',command=lambda :memory('r'),font=5,width=5,height=2,background='blue')
f13=Button(a,text='MC',command=lambda :memory('c'),font=5,width=5,height=2,background='blue')
f14_1=Button(a,text='SC',command=science,font=5,width=5,height=12,background='purple')
n0=Button(a,text='0',command=lambda :func('0'),font=5,width=5,height=2,background='white')
n1=Button(a,text='1',command=lambda :func('1'),font=5,width=5,height=2,background='white')
n2=Button(a,text='2',command=lambda :func('2'),font=5,width=5,height=2,background='white')
n3=Button(a,text='3',command=lambda :func('3'),font=5,width=5,height=2,background='white')
n4=Button(a,text='4',command=lambda :func('4'),font=5,width=5,height=2,background='white')
n5=Button(a,text='5',command=lambda :func('5'),font=5,width=5,height=2,background='white')
n6=Button(a,text='6',command=lambda :func('6'),font=5,width=5,height=2,background='white')
n7=Button(a,text='7',command=lambda :func('7'),font=5,width=5,height=2,background='white')
n8=Button(a,text='8',command=lambda :func('8'),font=5,width=5,height=2,background='white')
n9=Button(a,text='9',command=lambda :func('9'),font=5,width=5,height=2,background='white')
n10=Button(a,text='.',command=lambda :func('.'),font=5,width=5,height=2,background='white')
f1.grid(row=1,column=1,sticky=E)
f2.grid(row=1,column=2,sticky=E)
f3.grid(row=1,column=3,sticky=E)
f4.grid(row=1,column=4,sticky=E)
f5.grid(row=1,column=5,sticky=E)
f6.grid(row=3,column=5,sticky=E)
f7.grid(row=2,column=4,sticky=E)
f8.grid(row=2,column=5,sticky=E)
f9.grid(row=3,column=4,sticky=E)
f10.grid(row=4,column=4,sticky=E)
f11.grid(row=4,column=5,sticky=E)
f12.grid(row=5,column=4,sticky=E)
f13.grid(row=5,column=5,sticky=E)
f14_1.grid(row=1,rowspan=5,column=6,sticky=E)
n0.grid(row=5,column=1,sticky=E)
n1.grid(row=2,column=1,sticky=E)
n2.grid(row=2,column=2,sticky=E)
n3.grid(row=2,column=3,sticky=E)
n4.grid(row=3,column=1,sticky=E)
n5.grid(row=3,column=2,sticky=E)
n6.grid(row=3,column=3,sticky=E)
n7.grid(row=4,column=1,sticky=E)
n8.grid(row=4,column=2,sticky=E)
n9.grid(row=4,column=3,sticky=E)
n10.grid(row=5,column=2,sticky=E)
a.mainloop()

