from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno


class AddressBook:
    def __init__(self):
        self.allContacts = []
        self.parent = Tk()
        self.parent.title("Final Project")
        self.parentFrame = LabelFrame(self.parent, text="Address Book", padx=75, pady=10)
        self.parentFrame.pack(padx=10, pady=10, fill="both", expand=True)

        self.parentLabel = Label(self.parentFrame, text="What would you like to do?")
        self.parentLabel.pack()

        self.addContact = Button(self.parentFrame, text="Add Contact", width=20, command=self.add_contacts)
        self.addContact.pack(pady=5)

        self.editContactButton = Button(self.parentFrame, text="Edit Contact", width=20, command=self.edit_contacts)
        self.editContactButton.pack(pady=5)

        self.deleteContactButton = Button(self.parentFrame, text="Delete Contact", width=20,
                                          command=self.delete_contact)
        self.deleteContactButton.pack(pady=5)

        self.viewContactsButton = Button(self.parentFrame, text="View Contacts", width=20, command=self.view_contacts)
        self.viewContactsButton.pack(pady=5)

        self.searchAddressBookButton = Button(self.parentFrame, text="Search Address Book", width=20,
                                              command=self.search_address_book)
        self.searchAddressBookButton.pack(pady=5)

        self.exitButton = Button(self.parentFrame, text="Exit", width=20, command=self.exit_phone_book)
        self.exitButton.pack(pady=5)

        self.load_contacts_from_file()


    def load_contacts_from_file(self):
        try:
            with open("Final Project Data Base.txt", "r") as dataFileRead:
                lines = dataFileRead.readlines()

            for line in lines:
                asList = line.split(", ")
                self.allContacts.append([asList[1], asList[2], asList[3], asList[4].replace("\n", "")])

        except FileNotFoundError:
            messagebox.showwarning("Notice", "No data file found.")

    def save_contacts_to_file(self):
        with open("Final Project Data Base.txt", "w") as dataFileWrite:
            for count, contact in enumerate(self.allContacts, 1):
                dataFileWrite.writelines(f"{count}, {contact[0]}, {contact[1]}, {contact[2]}, {str(contact[3])}\n")


    def add_contacts(self):
        child = Toplevel()
        childFrame = LabelFrame(child, text="Add Contacts")
        childFrame.pack(padx=10, pady=10, fill="both", expand=True)
        childFrame.grab_set()

        firstNameLabel = Label(childFrame, text="First Name:")
        firstNameLabel.grid(row=0, column=0)
        firstNameEntry = Entry(childFrame, width=30)
        firstNameEntry.grid(row=0, column=1, padx=5, pady=5)

        lastNameLabel = Label(childFrame, text="Last Name:")
        lastNameLabel.grid(row=1, column=0)
        lastNameEntry = Entry(childFrame, width=30)
        lastNameEntry.grid(row=1, column=1, padx=5, pady=5)

        addressLabel = Label(childFrame, text="Address:")
        addressLabel.grid(row=2, column=0)
        addressEntry = Entry(childFrame, width=30)
        addressEntry.grid(row=2, column=1, padx=5, pady=5)

        contactNumLabel = Label(childFrame, text="Contact Number:")
        contactNumLabel.grid(row=3, column=0)
        contactNumEntry = Entry(childFrame, width=30)
        contactNumEntry.grid(row=3, column=1, padx=5, pady=5)

        def submit_data():
            def disable_widgets():
                submitButton['state'] = "disabled"
                firstNameEntry["state"] = "disabled"
                lastNameEntry["state"] = "disabled"
                addressEntry["state"] = "disabled"
                contactNumEntry["state"] = "disabled"

            def normal_widgets():
                submitButton['state'] = 'normal'
                firstNameEntry['state'] = 'normal'
                lastNameEntry['state'] = 'normal'
                addressEntry['state'] = 'normal'
                contactNumEntry['state'] = 'normal'

            if firstNameEntry.get().isalpha() and lastNameEntry.get().isalpha() and contactNumEntry.get().isdigit():
                self.allContacts.append([firstNameEntry.get(), lastNameEntry.get(), addressEntry.get(),
                                         contactNumEntry.get()])
                self.save_contacts_to_file()
                disable_widgets()
                messagebox.showinfo(title="Notice", message="A contact has been added.")
                normal_widgets()
                child.destroy()

            else:
                disable_widgets()
                messagebox.showerror(title="Invalid Input", message="Please enter valid contact details.")
                normal_widgets()
                raise TypeError


        submitButton = Button(childFrame, text="Submit", width=25, command=submit_data)
        submitButton.grid(row=4, column=1)

        child.mainloop()

    def edit_contacts(self):
        child = Toplevel()
        childFrame = LabelFrame(child, text="Edit Contacts")
        childFrame.pack(padx=10, pady=10, fill="both", expand=True)
        child.grab_set()

        numToEditLabel = Label(childFrame, text="Entry Number:")
        numToEditLabel.grid(row=0, column=0)
        numToEditEntry = Entry(childFrame, width=30)
        numToEditEntry.grid(row=0, column=1, padx=5, pady=5)

        def disable_widgets():
            checkButton['state'] = 'disabled'
            numToEditEntry['state'] = 'disabled'

        def normal_widgets():
            checkButton['state'] = 'normal'
            numToEditEntry['state'] = 'normal'

        def get_info():
            if numToEditEntry.get().isdigit():
                if int(numToEditEntry.get()) == 0:
                    disable_widgets()
                    messagebox.showerror(title="Invalid Input", message="Please enter valid entry number.")
                    normal_widgets()

                elif int(numToEditEntry.get()) > 100 or int(numToEditEntry.get()) > len(self.allContacts):
                    disable_widgets()
                    messagebox.showerror(title="Invalid Input", message="Out of range.")
                    normal_widgets()
                    raise IndexError

                elif numToEditEntry.get().isdigit():
                    separator = ttk.Separator(childFrame, orient='horizontal')
                    separator.grid(row=2, columnspan=1 and 2, sticky="ew", pady=10)

                    disable_widgets()

                    firstNameLabel = Label(childFrame, text="First Name:")
                    firstNameLabel.grid(row=3, column=0)
                    firstNameEntry = Entry(childFrame, width=30)
                    firstNameEntry.grid(row=3, column=1, padx=5, pady=5)

                    lasNameLabel = Label(childFrame, text="Last Name:")
                    lasNameLabel.grid(row=4, column=0)
                    lastNameEntry = Entry(childFrame, width=30)
                    lastNameEntry.grid(row=4, column=1, padx=5, pady=5)

                    addressLabel = Label(childFrame, text="Address:")
                    addressLabel.grid(row=5, column=0)
                    addressEntry = Entry(childFrame, width=30)
                    addressEntry.grid(row=5, column=1, padx=5, pady=5)

                    contactNumLabel = Label(childFrame, text="Contact Number:")
                    contactNumLabel.grid(row=6, column=0)
                    contactNumEntry = Entry(childFrame, width=30)
                    contactNumEntry.grid(row=6, column=1, padx=5, pady=5)


                    def set_new_info():
                        if firstNameEntry.get().isalpha() and lastNameEntry.get().isalpha() \
                                and contactNumEntry.get().isdigit():
                            self.allContacts[int(numToEditEntry.get()) - 1][0] = firstNameEntry.get()
                            self.allContacts[int(numToEditEntry.get()) - 1][1] = lastNameEntry.get()
                            self.allContacts[int(numToEditEntry.get()) - 1][2] = addressEntry.get()
                            self.allContacts[int(numToEditEntry.get()) - 1][3] = contactNumEntry.get()

                            with open("Final Project Data Base.txt", "w") as dataFileWrite:
                                for count, items in enumerate(self.allContacts, 1):
                                    dataFileWrite.writelines(
                                        f"{count}, {items[0]}, {items[1]}, {items[2]}, {str(items[3])}\n")

                            submitButton['state'] = "disabled"
                            firstNameEntry["state"] = "disabled"
                            lastNameEntry["state"] = "disabled"
                            addressEntry["state"] = "disabled"
                            contactNumEntry["state"] = "disabled"
                            messagebox.showinfo(title="Notice", message="A contact has been edited.")
                            child.destroy()

                        else:
                            submitButton['state'] = "disabled"
                            firstNameEntry["state"] = "disabled"
                            lastNameEntry["state"] = "disabled"
                            addressEntry["state"] = "disabled"
                            contactNumEntry["state"] = "disabled"
                            messagebox.showerror(title="Invalid Input", message="Please enter valid contact details")
                            submitButton['state'] = 'normal'
                            firstNameEntry['state'] = 'normal'
                            lastNameEntry['state'] = 'normal'
                            addressEntry['state'] = 'normal'
                            contactNumEntry['state'] = 'normal'
                            raise TypeError

                    submitButton = Button(childFrame, text="Submit", width=25, command=set_new_info)
                    submitButton.grid(row=7, column=1)

            else:
                disable_widgets()
                messagebox.showerror(title="Invalid Input", message="Please enter valid entry number.")
                normal_widgets()
                raise TypeError

        checkButton = Button(childFrame, text="Check", width=25, command=get_info)
        checkButton.grid(row=1, column=1)

        child.mainloop()

    def delete_contact(self):
        child = Toplevel()
        childFrame = LabelFrame(child, text="Delete Contact")
        childFrame.pack(padx=10, pady=10, fill="both", expand=True)
        childFrame.grab_set()

        numToDelLabel = Label(childFrame, text="Entry Number:")
        numToDelLabel.grid(row=0, column=0)
        numToDelEntry = Entry(childFrame, width=30)
        numToDelEntry.grid(row=0, column=1, padx=5, pady=5)

        def delete():
            if numToDelEntry.get().isdigit():
                if int(numToDelEntry.get()) == 0:
                    submitButton['state'] = 'disabled'
                    numToDelEntry['state'] = 'disabled'
                    messagebox.showerror(title="Invalid Input", message="Please enter valid entry number.")
                    submitButton['state'] = 'normal'
                    numToDelEntry['state'] = 'normal'

                elif int(numToDelEntry.get()) > 100 or int(numToDelEntry.get()) > len(self.allContacts):
                    submitButton['state'] = 'disabled'
                    numToDelEntry['state'] = 'disabled'
                    messagebox.showerror(title="Invalid Input", message="Out of range.")
                    submitButton['state'] = 'normal'
                    numToDelEntry['state'] = 'normal'
                    raise IndexError

                else:
                    for entry in enumerate(self.allContacts, 1):
                        if int(numToDelEntry.get()) in entry:
                            self.allContacts.pop(int(numToDelEntry.get()) - 1)

                    with open("Final Project Data Base.txt", "w") as dataFileWrite:
                        for count, items in enumerate(self.allContacts, 1):
                            dataFileWrite.writelines(f"{count}, {items[0]}, {items[1]}, {items[2]}, {str(items[3])}\n")

                    submitButton['state'] = 'disabled'
                    numToDelEntry['state'] = 'disabled'
                    messagebox.showinfo(title="Notice", message="A contact has been deleted.")
                    child.destroy()

            else:
                submitButton['state'] = 'disabled'
                numToDelEntry['state'] = 'disabled'
                messagebox.showerror(title="Invalid Input", message="Please enter valid entry number.")
                submitButton['state'] = 'normal'
                numToDelEntry['state'] = 'normal'
                raise TypeError

        submitButton = Button(childFrame, text="Submit", width=25, command=delete)
        submitButton.grid(row=4, column=1)

    def view_contacts(self):
        child = Toplevel()
        childFrame = LabelFrame(child, text="View Contacts")
        childFrame.pack(padx=10, pady=10, fill="both", expand=True)
        childFrame.grab_set()

        tableData = ttk.Treeview(childFrame)
        tableData['show'] = 'headings'
        tableTheme = ttk.Style()
        tableTheme.theme_use("clam")

        tableData['columns'] = ("Entry Number", "First Name", "Last Name", "Address", "Contact Number")
        tableData.column("Entry Number", width=100, minwidth=100, anchor=CENTER)
        tableData.column("First Name", width=200, minwidth=200, anchor=CENTER)
        tableData.column("Last Name", width=200, minwidth=200, anchor=CENTER)
        tableData.column("Address", width=300, minwidth=300, anchor=CENTER)
        tableData.column("Contact Number", width=125, minwidth=125, anchor=CENTER)

        tableData.heading("Entry Number", text="Entry Number", anchor=CENTER)
        tableData.heading("First Name", text="First Name", anchor=CENTER)
        tableData.heading("Last Name", text="Last Name", anchor=CENTER)
        tableData.heading("Address", text="Address", anchor=CENTER)
        tableData.heading("Contact Number", text="Contact Number", anchor=CENTER)

        for count, items in enumerate(self.allContacts, 1):
            tableData.insert('', count, text="", values=(count, items[0], items[1], items[2], items[3]))
        tableData.pack()

    def search_address_book(self):
        child = Toplevel()
        childFrame = LabelFrame(child, text="Search Address Book")
        childFrame.pack(padx=10, pady=10, fill="both", expand=True)
        childFrame.grab_set()

        childFrameLabel = Label(childFrame, text="Would you like to search the address book by:", padx=20, pady=10)
        childFrameLabel.pack()

        radioVar = IntVar()

        radioFirst = Radiobutton(childFrame, text='First Name', value=1, variable=radioVar)
        radioSecond = Radiobutton(childFrame, text='Last Name', value=2, variable=radioVar)
        radioThird = Radiobutton(childFrame, text='Address', value=3, variable=radioVar)
        radioFourth = Radiobutton(childFrame, text='Contact Number', value=4, variable=radioVar)

        radioFirst.pack(anchor=W, side=TOP, padx=3, pady=3)
        radioSecond.pack(anchor=W, side=TOP, padx=3, pady=3)
        radioThird.pack(anchor=W, side=TOP, padx=3, pady=3)
        radioFourth.pack(anchor=W, side=TOP, padx=3, pady=3)

        matchedEntry = []

        def disable_button():
            submitButton["state"] = "disabled"
            radioFirst["state"] = "disabled"
            radioSecond["state"] = "disabled"
            radioThird["state"] = "disabled"
            radioFourth["state"] = "disabled"

        def normal_button():
            submitButton["state"] = "normal"
            radioFirst["state"] = "normal"
            radioSecond["state"] = "normal"
            radioThird["state"] = "normal"
            radioFourth["state"] = "normal"

        def prepare_interface():
            disable_button()
            separator = ttk.Separator(childFrame, orient='horizontal')
            separator.pack(pady=5, fill="x")

            firstNameLabel = Label(childFrame, text="First Name:")
            firstNameLabel.pack(anchor=W, side=TOP, padx=3, pady=3)

        def submitted():

            if radioVar.get() == 1:
                prepare_interface()

                firstNameEntry = Entry(childFrame, width=40)
                firstNameEntry.pack(anchor=W, side=TOP, padx=3, pady=3, fill="x")

                def show_matched_contact():
                    for entries in self.allContacts:
                        if entries[0] == firstNameEntry.get():
                            index = self.allContacts.index(entries) + 1
                            matchedEntry.append([index, entries])

                    show_data()

                submitButton2 = Button(childFrame, text="Submit", width=25, command=show_matched_contact)
                submitButton2.pack(fill="x", padx=3, pady=3)

            elif radioVar.get() == 2:
                prepare_interface()

                firstNameEntry = Entry(childFrame, width=40)
                firstNameEntry.pack(anchor=W, side=TOP, padx=3, pady=3, fill="x")

                def show_matched_contact():
                    for entries in self.allContacts:
                        if entries[1] == firstNameEntry.get():
                            index = self.allContacts.index(entries) + 1
                            matchedEntry.append([index, entries])

                    show_data()

                submitButton2 = Button(childFrame, text="Submit", width=25, command=show_matched_contact)
                submitButton2.pack(fill="x", padx=3, pady=3)

            elif radioVar.get() == 3:
                prepare_interface()

                firstNameEntry = Entry(childFrame, width=40)
                firstNameEntry.pack(anchor=W, side=TOP, padx=3, pady=3, fill="x")

                def show_matched_contact():
                    for entries in self.allContacts:
                        if entries[2] == firstNameEntry.get():
                            index = self.allContacts.index(entries) + 1
                            matchedEntry.append([index, entries])

                    show_data()

                submitButton2 = Button(childFrame, text="Submit", width=25, command=show_matched_contact)
                submitButton2.pack(fill="x", padx=3, pady=3)

            elif radioVar.get() == 4:
                prepare_interface()

                firstNameEntry = Entry(childFrame, width=40)
                firstNameEntry.pack(anchor=W, side=TOP, padx=3, pady=3, fill="x")

                def show_matched_contact():
                    for entries in self.allContacts:
                        if entries[3] == firstNameEntry.get():
                            index = self.allContacts.index(entries) + 1
                            matchedEntry.append([index, entries])

                    show_data()

                submitButton2 = Button(childFrame, text="Submit", width=25, command=show_matched_contact)
                submitButton2.pack(fill="x", padx=3, pady=3)

            else:
                disable_button()
                messagebox.showerror(title="Error", message="Please select a category.")
                normal_button()

            def show_data():
                if len(matchedEntry) > 0:
                    child3 = Toplevel()
                    childFrame3 = LabelFrame(child3, text="Search Address Book")
                    childFrame3.pack(padx=10, pady=10, fill="both", expand=True)
                    childFrame3.grab_set()

                    tableData = ttk.Treeview(childFrame3)
                    tableData['show'] = 'headings'
                    tableTheme = ttk.Style()
                    tableTheme.theme_use("clam")

                    tableData['columns'] = ("Entry Number", "First Name", "Last Name", "Address", "Contact Number")
                    tableData.column("Entry Number", width=100, minwidth=100, anchor=CENTER)
                    tableData.column("First Name", width=200, minwidth=200, anchor=CENTER)
                    tableData.column("Last Name", width=200, minwidth=200, anchor=CENTER)
                    tableData.column("Address", width=300, minwidth=300, anchor=CENTER)
                    tableData.column("Contact Number", width=125, minwidth=125, anchor=CENTER)

                    tableData.heading("Entry Number", text="Entry Number", anchor=CENTER)
                    tableData.heading("First Name", text="First Name", anchor=CENTER)
                    tableData.heading("Last Name", text="Last Name", anchor=CENTER)
                    tableData.heading("Address", text="Address", anchor=CENTER)
                    tableData.heading("Contact Number", text="Contact Number", anchor=CENTER)

                    for items in matchedEntry:
                        tableData.insert('', items[0], text="",
                                         values=(items[0], items[1][0], items[1][1], items[1][2], items[1][3]))
                    tableData.pack()
                    matchedEntry.clear()

                else:
                    submitButton2["state"] = "disabled"
                    firstNameEntry["state"] = "disabled"
                    messagebox.showerror(title="Error", message="Entry does not exist.")
                    submitButton2["state"] = "normal"
                    firstNameEntry["state"] = "normal"
                    raise IndexError

        submitButton = Button(childFrame, text="Submit", width=40, command=submitted)
        submitButton.pack(side=TOP, padx=3, pady=3, fill="x")

    def exit_phone_book(self):
        userAnswer = askyesno("Exit", "Are you sure?")
        if userAnswer:
            self.parent.destroy()

    def run(self):
        self.parent.mainloop()


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()
