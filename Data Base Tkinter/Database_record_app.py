from tkinter import *
import sqlite3

root=Tk()
root.title(" DataBase Record ")
root.geometry("400x600")
root.iconbitmap('edit.ico')
'''
# Create a Database or connect to one
conn=sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()

# Create a Table
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer) """)
'''
def update():
    # Create a Database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create cursor
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("""
                UPDATE address SET 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                WHERE oid = :oid""",
              {
                  'first': f_name_edit.get(),
                  'last': l_name_edit.get(),
                  'address': address_edit.get(),
                  'city': city_edit.get(),
                  'state': state_edit.get(),
                  'zipcode': zipcode_edit.get(),

                  'oid': record_id
              })
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create edit() function to update a record
def edit():
    editor=Tk()
    editor.title("Update a Record")
    editor.geometry("400x600")
    root.iconbitmap('edit.ico')
    # Create a Database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create cursor
    c=conn.cursor()
    record_id=delete_box.get()
    # Query the Data base
    c.execute(" SELECT * FROM addresses WHERE oid ="+record_id)
    records=c.fetchall()

    show=''
    for record in records[0:]:
        show+=str(record)+"\t"+"\n"

        # Create Global variable for text boxes name
        global f_name_edit
        global l_name_edit
        global address_edit
        global city_edit
        global state_edit
        global zipcode_edit

        # Create Text Boxes
        f_name_edit=Entry(editor, width=50)
        f_name_edit.grid(row=0, column=1, padx=20, pady=5)
        l_name_edit=Entry(editor, width=50)
        l_name_edit.grid(row=1, column=1, padx=20, pady=5)
        address_edit=Entry(editor, width=50)
        address_edit.grid(row=2, column=1, padx=20, pady=5)
        city_edit=Entry(editor, width=50)
        city_edit.grid(row=3, column=1, padx=20, pady=5)
        state_edit=Entry(editor, width=50)
        state_edit.grid(row=4, column=1, padx=20, pady=5)
        zipcode_edit=Entry(editor, width=50)
        zipcode_edit.grid(row=5, column=1, padx=20, pady=5)

        # Create Text Label
        f_name_label_edit=Label(editor, text="First Name")
        f_name_label_edit.grid(row=0, column=0)
        l_name_label_edit=Label(editor, text="Last Name")
        l_name_label_edit.grid(row=1, column=0)
        address_label_edit=Label(editor, text="Address")
        address_label_edit.grid(row=2, column=0)
        city_label_edit=Label(editor, text="City")
        city_label_edit.grid(row=3, column=0)
        state_label_edit=Label(editor, text="State")
        state_label_edit.grid(row=4, column=0)
        zipcode_label_edit=Label(editor, text="ZipCode")
        zipcode_label_edit.grid(row=5, column=0)

        # Create a Save Button to save edited record
        save_btn=Button(editor, text=" save Record ", command=query)
        save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

        # loop through result
        for record in records:
            f_name_edit.insert(0, record[0])
            l_name_edit.insert(0, record[1])
            address_edit.insert(0, record[2])
            city_edit.insert(0, record[3])
            state_edit.insert(0, record[4])
            zipcode_edit.insert(0, record[5])


# Create data base submit function
def submit():
    # Create a Database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create cursor
    c=conn.cursor()
    # Insert into Table
    c.execute(" INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode) ",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    # clear the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create a function to show record
def query():
    # Create a Database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create cursor
    c=conn.cursor()

    # Query the Data base
    c.execute(" SELECT *,oid FROM addresses ")
    records=c.fetchall()
    show=''
    for record in records[0:]:
        show+=str(record[0:6])+"\t"+str(record[6])+"\n"

    query_label=Label(root, text=show)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create a function to delete record
def delete():
    # Create a Database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create cursor
    c=conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# Create Text Boxes
f_name=Entry(root, width=50)
f_name.grid(row=0, column=1, padx=20, pady=5)
l_name=Entry(root, width=50)
l_name.grid(row=1, column=1, padx=20, pady=5)
address=Entry(root, width=50)
address.grid(row=2, column=1, padx=20, pady=5)
city=Entry(root,width=50)
city.grid(row=3, column=1, padx=20, pady=5)
state=Entry(root, width=50)
state.grid(row=4, column=1, padx=20, pady=5)
zipcode=Entry(root, width=50)
zipcode.grid(row=5, column=1, padx=20, pady=5)
delete_box=Entry(root, width=50)
delete_box.grid(row=9, column=1, padx=20, pady=5)

# Create Text Label
f_name_label=Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label=Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label=Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label=Label(root, text="City")
city_label.grid(row=3, column=0)
state_label=Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label=Label(root, text="ZipCode")
zipcode_label.grid(row=5, column=0)
delete_box_label=Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0)

# Create Submit Button
submit_btn=Button(root, text='Submit', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=120)

# Create Query Button
query_btn=Button(root, text=" Show Records ", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Delete Button
delete_btn=Button(root, text=" Delete Record ", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Update Button
edit_btn=Button(root, text=" Edit Record ", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

'''
# commit changes
conn.commit()
# close connection
conn.close()
'''
root.mainloop()



