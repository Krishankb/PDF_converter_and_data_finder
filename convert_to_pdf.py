from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from docx2pdf import convert
import script3
import creating_excel

def openfile():
  file = askopenfilename(filetypes=[('Word Files', '*.docx'),('Word Files', '*.doc')])
  convert(file,r'C:\Users\krish\OneDrive\Desktop\applications\CSV reading\Converted\doc2pdfconverted.pdf')   
  showinfo("Done", "File successfully converted ")

def mobile_command():
  list1.delete(0,END)
  row = script3.mobile_selector()
  list1.insert(END,row)
  list1.insert(END,"Sucessfully inserted into the  Excel database")
  creating_excel.excel_database()
 

def email_command():
  list1.delete(0,END)
  row = script3.email_selector()
  list1.insert(END,row)
  list1.insert(END,"Sucessfully inserted into the Excel database")
  creating_excel.excel_database()

window = Tk()
window.title("Pdf Converter App")
window.geometry('350x265')

label=Label(window,text="Choose a file!")
label.grid(row=0,column=1,padx=5,pady=5)

b1 = Button(window,text = "Convert",width=13,activebackground='green',background='red',command=openfile)
b1.grid(row = 1,column  = 1,padx=5,pady=5)

b2 = Button(window,text = "Store Mobile No:",width=18,activebackground='green',command=mobile_command)
b2.grid(row = 4,column  = 3,padx=5,pady=5)

b3 = Button(window,text = "Store Email No:",width=18,activebackground='green',command=email_command)
b3.grid(row = 5,column  = 3,padx=5,pady=5)

list1= Listbox(window,height= 9,width = 30)
list1.grid(row = 2,column= 0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row= 2, column=2,rowspan=6,sticky='ns')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2=Scrollbar(window)
sb2.grid(row=8,column=1,sticky='ns')

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

window.mainloop()