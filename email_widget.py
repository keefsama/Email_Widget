# Below is code used to create an Email widget which will be used on Kubuntu 14.04
__author__ = 'kferguson'
from Tkinter import *
import poplib
import parser
import sys

username = ''
password = ''

# This portion is for Creation of the Widget we are going to use.
def show_entry_fields():
    global username
    global password
    username = e1.get()
    password = e2.get()
    get_email(username, password)


# This section is for connecting to gmail for import of all new emails.
def get_email(user, passw):
    user = str(user + "@gmail.com")
    passw = str(passw)
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    print pop_conn.getwelcome()
    pop_conn.user(user)
    pop_conn.pass_(passw)
    #Get messages from server:
    print pop_conn.stat()
    print pop_conn.list()
    if pop_conn.stat()[1] > 0:
        print("You have new mail.")
        msgNum = len(pop_conn.list()[1])
        print("You have %d messages in your inbox" % msgNum)
        for msgList in range(msgNum):
            for totMsg in pop_conn.retr(msgList + 1)[1]:
                if totMsg.startswith('Subject'):
                    print('\t' + totMsg)
                    print("\n")
                    break
        pop_conn.quit()
        sys.exit()
    else:
        print("No new mail.\n")
        pop_conn.quit()

#Remember to always define a function before calling it.
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