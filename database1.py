from tkinter import *
from tkinter import messagebox
import sqlite3
window=Tk()
window.title("Address book")
window.iconbitmap('c:/Users/dp.ico')
window.resizable(0,0)
'''
conn=sqlite3.connect("Address_book.db")
c=conn.cursor()

c.execute("""CREATE TABLE addresses(
        name text,
        address text,
        city text,
        state text,
        phone_no integer)""")

conn.commit()
conn.close()
'''

def submit():

    # create or open a data_base
    conn = sqlite3.connect("address_book.db")
    # to do everything or like a servant
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:name,:address,:city,:state,:phone_no)",
    {
        'name' : name.get(),
        'address' : address.get(),
        'city' : city.get(),
        'state' : state.get(),
        'phone_no' : phone_no.get()
    } )
    # to commit changes to our data_base
    conn.commit()

    # to close our database
    conn.close()
    if name.get()=="" or address.get()=="" or city.get()=="" or state.get()=="" or phone_no.get()=="" :
    	messagebox.showerror("Error","Not Valid")
    #clear input boxes
    name.delete(0,END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    phone_no.delete(0, END)

def query():
    # create or open a data_base
    conn = sqlite3.connect("address_book.db")
    # to do everything or like a servant
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print_record=''
    for record in records:
        print_record +=str(record[0])+ " "+str(record[5])+"\n"
 
    query_label=Label(window,text=print_record)
    query_label.grid(row=13,column=0,columnspan=2)
    # to commit changes to our data_base
    conn.commit()

    # to close our database
    conn.close()

#function to delete a record
def delete():
	if delete_record.get() == '':
		messagebox.showerror("Error", "Not a valid Id")
	conn=sqlite3.connect("Address_book.db")
	c=conn.cursor()
	c.execute("DELETE FROM addresses WHERE oid="+delete_record.get())
	conn.commit()
	conn.close()

#function to insert
def edit():
	if delete_record.get() == '':
		messagebox.showerror("Error", "Not a valid Id")
		
	conn=sqlite3.connect("Address_book.db")
	c=conn.cursor()
	c.execute("SELECT * FROM addresses WHERE oid="+delete_record.get())
	records=c.fetchall()

	
	#button
	save_bt=Button(window,text="Save changes",command=update)
	save_bt.grid(row=12,column=0,columnspan=2,pady=5,ipadx=90)

	for record in records:
		name.insert(0,record[0])
		address.insert(0,record[1])
		city.insert(0,record[2])
		state.insert(0,record[3])
		phone_no.insert(0,record[4])
	
#function to update record

def update():
	conn= sqlite3.connect("address_book.db")
	c=conn.cursor()
	record_id=delete_record.get()
	c.execute("""UPDATE addresses SET
				 name= :name,
				 address= :address,
				 city= :city,
				 state=:state,
				 phone_no=:phone_no
				 WHERE oid=:oid""",
				 {
					'name':name.get(),
					'address':address.get(),
					'city':city.get(),
					'state':state.get(),
					'phone_no':phone_no.get(),
					'oid':record_id
				})
	conn.commit()
	conn.close()
	name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	phone_no.delete(0,END)
#input_boxes
name=Entry(window,width=30)
name.grid(row=0,column=1,pady=(10,0))
address=Entry(window,width=30)
address.grid(row=1,column=1)
city=Entry(window,width=30)
city.grid(row=2,column=1)
state=Entry(window,width=30)
state.grid(row=3,column=1)
phone_no=Entry(window,width=30)
phone_no.grid(row=4,column=1)
delete_record=Entry(window,width=30)
delete_record.grid(row=9,column=1)


#label for input boxes
name_label=Label(window,text="Name:")
name_label.grid(row=0,column=0)
address_label=Label(window,text="Address:")
address_label.grid(row=1,column=0)
city_label=Label(window,text="City:")
city_label.grid(row=2,column=0)
state_label=Label(window,text="State:")
state_label.grid(row=3,column=0)
phone_no_label=Label(window,text="Phone number:")
phone_no_label.grid(row=4,column=0)
delete_label=Label(window,text="Select ID:")
delete_label.grid(row=9,column=0)

#button
submit_bt=Button(window,text="Add record to database",command=submit)
submit_bt.grid(row=6,column=0,columnspan=2,padx=5,pady=10,ipadx=60)
show_bt=Button(window,text="Show records",command=query)
show_bt.grid(row=7,column=0,columnspan=2,ipadx=86)
delete_bt=Button(window,text="Delete record",command=delete)
delete_bt.grid(row=10,column=0,columnspan=2,pady=5,ipadx=86)
edit_bt=Button(window,text="Edit record",command=edit)
edit_bt.grid(row=11,column=0,columnspan=2,pady=5,ipadx=91)


window.mainloop()