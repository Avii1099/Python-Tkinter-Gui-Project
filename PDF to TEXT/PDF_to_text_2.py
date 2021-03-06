import PyPDF2
from tkinter import *

from tkinter import filedialog

# making label and window

root = Tk()
root.geometry("400x350")
root.title("PDF to Text")
root.config(bg="#FFE873")

Label(root, text="PDF to Text", bg="#FFE873", fg = "RED", font="Verdana 30 bold").pack()
Label(root, text="@_python.py_", bg="#FFE873", fg = "RED", font="Verdana 30 bold").pack()

# define function
def PDF_to_Text():

    #browse file
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files ", "*.pdf*"), ("all files", "*.*")))

    # link show in window label
    label_pdf_file.configure(text="File : "+filename)

    #change pdf to text code

    pdf_obj = open(filename, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)

    # assign page number
    pageObj = pdf_reader.getPage(0)
    pageText = pageObj.extractText()

    # making Text label
    T = Text(root, height=4, width=45)
    T.pack(pady=5)

    #Insert the text in label
    T.insert(INSERT, pageText)

# design button and label for pf file link
label_pdf_file = Label(root, text="File : ", width=50, height=4, fg="blue")
label_pdf_file.pack(anchor="center", pady=5)

#desgine convert button

Button(root, text="Convert", width=9, command=PDF_to_Text).pack(anchor="center", pady=5)
Button(root, text="exit", width=9, command=exit).pack(anchor="center", pady=5)



root.mainloop()





