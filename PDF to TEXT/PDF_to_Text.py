import PyPDF2
from tkinter import *
# import filedialog module
from tkinter import filedialog

root=Tk()
root.title('PDF to Text @_python.py_')
root.geometry("400x380")
root.config(bg="#FFE873")

Label(root, text = 'PDF to Text', fg="RED", bg="#FFE873", font="Verdana 30 bold").pack()
Label(root, text = '@_python.py_', fg="#4B8BBE", bg="#FFE873", font="Verdana 30 bold").pack()



def pdf_to_text():
    # Browse Files
    filename=filedialog.askopenfilename(initialdir="/", title="Select a File",
                                        filetypes=(("Text files", "*.pdf*"), ("all files", "*.*")))
    # Change label contents
    label_file_explorer.configure(text="File : "+filename)

    # Change Pdf to text
    pdf_obj=open(filename, "rb")
    pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
    #assign page no. at getPage(0)
    pageObj=pdf_reader.getPage(0)
    pageText= pageObj.extractText()

    T=Text(root, height=4, width=45)
    T.pack(pady=5)
    # Insert The Text.
    T.insert(INSERT, pageText)

label_file_explorer = Label(root, text="File: ", width=50, height=4, fg="blue")
label_file_explorer.pack(anchor='center', pady=5)
Button(root, text="Convert", width=9, command=pdf_to_text).pack(anchor='center', pady=5)
Button(root, text="Exit", width=9, command=exit).pack(anchor='center', pady=5)

root.mainloop()

