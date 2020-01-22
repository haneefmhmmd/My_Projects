from tkinter import *
import sqlite3
from tkinter import messagebox
window=Tk()
window.title("Room Booker")
window.iconbitmap('c:/Users/hotel.ico')
window.resizable(False,False)
window.configure(bg='grey')
conn=sqlite3.connect("hotel_db.db")
c=conn.cursor()
'''
c.execute("""CREATE TABLE reservation_info(
			name text,
			phone_no INTEGER,
			email text,
			bt_state INTEGER 
			)""")
conn.commit()
conn.close()
'''
def room_checker(number):
	conn=sqlite3.connect("hotel_db.db")
	c=conn.cursor()
	c.execute("SELECT * FROM reservation_info WHERE oid="+number)
	records=c.fetchall()
	for record in records:
		if record[3]==1:
			return True
		else:
			return False

def bt_click(number):

	global window_1,name,phone_no,email,bt_state
	bt_state=0
	window_1=Tk()
	window_1.title("Booking Form")

	

	#form labels
	name=Label(window_1,text="Name :")
	name.grid(row=1,column=0,padx=5)
	phone_no=Label(window_1,text="Phone number :")
	phone_no.grid(row=2,column=0,padx=5)
	email=Label(window_1,text="E-mail id :")
	email.grid(row=3,column=0,padx=5)

	#form input boxes
	name=Entry(window_1,width=30)
	name.grid(row=1,column=1,padx=(0,5))
	phone_no=Entry(window_1,width=30)
	phone_no.grid(row=2,column=1,padx=(0,5))
	email=Entry(window_1,width=30)
	email.grid(row=3,column=1,padx=(0,5))

	#form button
	book_bt=Button(window_1,text="Book",command=book)
	book_bt.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
	window_1.mainloop()

def book():
	#storing data
	conn=sqlite3.connect("hotel_db.db")
	c=conn.cursor()
	c.execute("INSERT INTO reservation_info VALUES(:name,:phone_no,:email,:bt_state)",
		{ 
			 'name':name.get(),
			 'phone_no':phone_no.get(),
			 'email':email.get(),
			 'bt_state':'1'
		})
	conn.commit()
	conn.close()
	if room_checker("1"):
		room_no_1.config(text="Filled",state=DISABLED)
	if room_checker("2"):
		room_no_2.config(text="Filled",state=DISABLED)
	if room_checker("3"):
		room_no_3.config(text="Filled",state=DISABLED)
	if room_checker("4"):
		room_no_4.config(text="Filled",state=DISABLED)
	if room_checker("5"):
		room_no_5.config(text="Filled",state=DISABLED)
	if room_checker("6"):
		room_no_6.config(text="Filled",state=DISABLED)
	if room_checker("7"):
		room_no_7.config(text="Filled",state=DISABLED)
	if room_checker("8"):
		room_no_8.config(text="Filled",state=DISABLED)

	#button creation
	room_no_1.grid(row=1,column=0,pady=5,ipadx=40)
	room_no_2.grid(row=1,column=1,pady=5,ipadx=40)
	room_no_3.grid(row=1,column=2,pady=5,ipadx=40)
	room_no_4.grid(row=1,column=3,pady=5,ipadx=40)
	room_no_5.grid(row=2,column=0,pady=5,ipadx=40)
	room_no_6.grid(row=2,column=1,pady=5,ipadx=40)
	room_no_7.grid(row=2,column=2,pady=5,ipadx=40)
	room_no_8.grid(row=2,column=3,pady=5,ipadx=40)
	show_bt=Button(window,text="Show records",command=query)
	show_bt.grid(row=7,column=0,columnspan=4,pady=10,ipadx=100)

	messagebox.showinfo("Booking Info","Booking Successful")
	window_1.destroy()

def query():
    # create or open a data_base
    conn = sqlite3.connect("hotel_db.db")
    # to do everything or like a servant
    c = conn.cursor()
    c.execute("SELECT *,oid FROM reservation_info")
    records=c.fetchall()
    print_record=''
    for record in records:
        print_record +=str(record)+"\n"
 
    query_label=Label(window,text=print_record)
    query_label.grid(row=13,column=0,columnspan=2)
    # to commit changes to our data_base
    conn.commit()

    # to close our database
    conn.close()


#labels
hotel_name=Label(window,text="Welcome to Luxury Hotel",font=("Comic Sans MS",30,"bold"))
hotel_name.grid(row=0,column=0,columnspan=4,padx=20,pady=30)
#initialization

#buttons declaration
room_no_1=Button(window,text="1",command=lambda:bt_click("1"))
room_no_2=Button(window,text="2",command=lambda:bt_click("2"))
room_no_3=Button(window,text="3",command=lambda:bt_click("3"))
room_no_4=Button(window,text="4",command=lambda:bt_click("4"))
room_no_5=Button(window,text="5",command=lambda:bt_click("5"))
room_no_6=Button(window,text="6",command=lambda:bt_click("6"))
room_no_7=Button(window,text="7",command=lambda:bt_click("7"))
room_no_8=Button(window,text="8",command=lambda:bt_click("8"))


#button initializaion
if room_checker("1"):
	room_no_1.config(text="Filled",state=DISABLED)
if room_checker("2"):
	room_no_2.config(text="Filled",state=DISABLED)
if room_checker("3"):
	room_no_3.config(text="Filled",state=DISABLED)
if room_checker("4"):
	room_no_4.config(text="Filled",state=DISABLED)
if room_checker("5"):
	room_no_5.config(text="Filled",state=DISABLED)
if room_checker("6"):
	room_no_6.config(text="Filled",state=DISABLED)
if room_checker("7"):
	room_no_7.config(text="Filled",state=DISABLED)
if room_checker("8"):
	room_no_8.config(text="Filled",state=DISABLED)

#button creation
room_no_1.grid(row=1,column=0,pady=5,ipadx=40)
room_no_2.grid(row=1,column=1,pady=5,ipadx=40)
room_no_3.grid(row=1,column=2,pady=5,ipadx=40)
room_no_4.grid(row=1,column=3,pady=5,ipadx=40)
room_no_5.grid(row=2,column=0,pady=5,ipadx=40)
room_no_6.grid(row=2,column=1,pady=5,ipadx=40)
room_no_7.grid(row=2,column=2,pady=5,ipadx=40)
room_no_8.grid(row=2,column=3,pady=5,ipadx=40)
show_bt=Button(window,text="Show records",command=query)
show_bt.grid(row=7,column=0,columnspan=4,pady=10,ipadx=100)

'''#DELETE COMMAND
conn=sqlite3.connect("hotel_db.db")
c=conn.cursor()
c.execute("DELETE FROM reservation_info")
conn.commit()
conn.close()'''
window.mainloop()