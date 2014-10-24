# Below is code used to create an Email widget which will be used on Kubuntu 14.04
__author__ = 'kferguson'
from Tkinter import *
import poplib
from email import parser

# This portion is for Creation of the Widget we are going to use.
def show_entry_fields():
	print('Please Enter Username: %s\nPlease Enter Password: %s' % (e1.get(), e2.get()))

master = Tk()
Label(master, text='Please Enter Username:').grid(row=0)
Label(master, text='Please Enter Password:').grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop()

#This section is for connecting to gmail for import of all new emails.

def get_email():
	print(message)
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('username')
pop_conn.pass_('password')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print message['subject']
pop_conn.quit()
