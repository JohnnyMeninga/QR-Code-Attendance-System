from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date, datetime
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from tkinter import *
import requests
import numpy as np
import imutils
import os



window = tk.Tk()
window.title('Attendance System V-089')
window.geometry('900x600')


year         = tk.StringVar()
department   = tk.StringVar()
room         = tk.StringVar()
period       = tk.StringVar()


"""
year         = '4'
department   = 'MCS'
room         = 'MCS101'
period       = '1'

"""


title = tk.Label(window,text="Attendance System V-001",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Year",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=year,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4', '5')
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Department",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=department,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("CSE","ECE","EEE","IT","MECH","ECM","BSCS","DBS")
combo_search.place(x=250,y=200)

ttk.Label(window, text = "Room",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=250)
combo_search=ttk.Combobox(window,textvariable=room,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('A','B','C','D','MCS101')
combo_search.place(x=250,y=250)

ttk.Label(window, text = "Period",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=300)
combo_search=ttk.Combobox(window,textvariable=period,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4','5','6','7')
combo_search.place(x=250,y=300)



# ----------------------------------------- Functions checkk --------------------------------
def checkk():
    if(year.get() and department.get() and period.get() and room.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")


exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)


Manag_Frame = Frame(window, bg="lavender")
Manag_Frame.place(x=480, y=80, width=450, height=530)

canvas = Canvas(Manag_Frame, width=300, height=300, background="lavender")
canvas.pack()
img = PhotoImage(file="Bg.png")
canvas.create_image(50, 50, anchor=NW, image=img)

window.mainloop()




cap = cv2.VideoCapture(0)
idList = []
today = date.today()
tn=datetime.now()
d = today.strftime("%b-%d-%Y")

dept = department.get()
#dept = department # temp value. code line will be removed
Ptime = tn.strftime("%H:%M:%S")
yr=year.get()
#yr=year # temp value. code line will be removed



#"""
subdir = 'data/attRecord/'
fileName = dept+' '+yr+'-'+d+'.txt'


if not os.path.exists(subdir):
    os.makdirs(subdir)

filePath = os.path.join(subdir, fileName)
#filePath=os.path.join(subdir, dept+' '+yr+'-'+d+'.txt')

if not os.path.exists(filePath):
    fob=open(filePath,'w+')

    fob.write("Reg No." + '\t')
    fob.write("Class & Sec" + '\t')
    fob.write("Year" + '\t')
    fob.write("Period" + '\t')
    fob.write("In Time" + '\n')

else:
    with open(filePath, 'r+') as file:
        idList=file.read()

#"""


#fob=open(dept+' '+yr+'-'+d+'.txt','w+')


def enterData(z):
    if z in idList:
        pass
    else:
        it = datetime.now()
        idList.append(z)
        z = ''.join(str(z))
        #str_z =  z.decode('gbk')
        intime = it.strftime("%H:%M:%S")
        #fob.write(str_z + '\t' + dept + '-' + room + '\t' + yr + '\t' + period + '\t' + intime + '\n')
        fob.write(z + '\t' + department.get() + ' - ' + room.get() + '\t' + year.get() + '\t' + period.get() + '\t' + intime + '\n')
    return idList


print('Reading...')


"""

def checkData(data):
    # data=str(data)
    if data in idList:
        print('Already Present')
    else:
        print('\n' + str(len(idList) + 1) + '\n' + 'present...')
        enterData(data)

"""

def checkData(data):
    data_str = data.decode('utf-8')
    if data_str in idList:
        print('Already Present')
    else:
        print('\n' + str(len(idList) + 1) + '\n' + 'present...')
        enterData(data_str)


"""

while True:
    _, frame = cap.read()         
    decodedObjects = pyzbar.decode(frame)
    
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)&0xFF == ord('g'):
        cv2.destroyAllWindows()
        break


"""

url = "http://192.168.43.1:8080/shot.jpg"


while True:
    img_resp=requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img=cv2.imdecode(img_arr,-1)
    img = imutils.resize(img, width=1000, height=1800)
    decodedObjects = pyzbar.decode(img)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow("Android_cam", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break


"""

subdir = 'ECEMar-12-2024.txt'
fob = open(subdir)
print(fob.read())


dept + ' ' + yr + '-' + d + '.txt'

"""



if not os.path.exists(filePath):
    print("filePathNotFound!"+'\n'+'Please create a new file!')
else:
    print('pass')

    fob=open(filePath, 'r+')
    print(fob.read())



fob.close()