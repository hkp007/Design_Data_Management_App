from tkinter import *
# from PIL import ImageTk,Image
# import PIL.Image as im
# import PIL.ImageTk as imtk
import tkinter as tk
import sqlite3


# Creating root window and configure it
root = tk.Tk()
root.title("Design Data Management")
root.iconbitmap("New_app.ico")
root.geometry("1000x800")
root.config(bg="#1f1f1f")

# Creating Data base
conn = sqlite3.connect("design_data.db")
# Create cursor
cursor_data = conn.cursor()
# # Create table
# cursor_data.execute("""
# CREATE TABLE design (
#     design_name TEXT PRIMARY KEY,
#     gala INTEGER DEFAULT 0,
#     small_lace INTEGER DEFAULT 0,
#     big_lace INTEGER DEFAULT 0,
#     all_over INTEGER DEFAULT 0,
#     sleeves INTEGER DEFAULT 0,
#     top_data INTEGER DEFAULT 0,
#     dupatta INTEGER DEFAULT 0,
#     butti INTEGER DEFAULT 0,
#     butti_lace INTEGER DEFAULT 0,
#     daman_lace INTEGER DEFAULT 0,
#     total INTEGER DEFAULT 0
# )
# """)
# Commite changes
conn.commit()
# Close connection
conn.close()

# Making main menu on root window
main_menu = Menu(root)
root.config(menu=main_menu)


def search_item():
    hide_all_frames()
    search_frame.pack(fill="both",expand=1)
    def ser():
        # Get the design name entered by the user
        search_design_name = d_name.get()

        # Connect to the database
        conn = sqlite3.connect("design_data.db")
        cursor_data = conn.cursor()

        # Execute an SQL SELECT statement to retrieve records that contain the input in design_name
        cursor_data.execute("SELECT * FROM design WHERE design_name LIKE ? ORDER BY design_name ASC",('%' + search_design_name + '%',))
        records = cursor_data.fetchall()

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Display the search results (you can customize this part as needed)
        result_frame = Frame(search_frame)
        result_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=5)

        if records:
            des_label = Label(result_frame,text="Design no.")
            des_label.grid(row=0,column=0, padx=15, pady=5)
            gala_label = Label(result_frame,text="gala")
            gala_label.grid(row=0,column=1, padx=15, pady=5)
            small_lace_label = Label(result_frame,text="small lace")
            small_lace_label.grid(row=0,column=2, padx=15, pady=5)
            big_lace_label = Label(result_frame,text="big lace")
            big_lace_label.grid(row=0,column=3, padx=15, pady=5)
            all_over_label = Label(result_frame,text="all over")
            all_over_label.grid(row=0,column=4, padx=15, pady=5)
            sleeves_label = Label(result_frame,text="sleeve")
            sleeves_label.grid(row=0,column=5, padx=15, pady=5)
            top_label = Label(result_frame,text="top")
            top_label.grid(row=0,column=6, padx=15, pady=5)
            dupatta_label = Label(result_frame,text="dupatta")
            dupatta_label.grid(row=0,column=7, padx=15, pady=5)
            butti_label = Label(result_frame,text="butti")
            butti_label.grid(row=0,column=8, padx=15, pady=5)
            butti_lace_label = Label(result_frame,text="butti lace")
            butti_lace_label.grid(row=0,column=9, padx=15, pady=5)
            daman_lace_label = Label(result_frame,text="daman lace")
            daman_lace_label.grid(row=0,column=10, padx=15, pady=5)
            total_label = Label(result_frame,text="total")
            total_label.grid(row=0,column=11, padx=15, pady=5)
            j=2
            # Display the records if found
            for row in records:
                x=[]
                for i in row:
                    x.append(str(i))
                d_name_label_rec = Label(result_frame, text=x[0])
                d_name_label_rec.grid(row=j,column=0)
                gala_label_rec = Label(result_frame, text=x[1])
                gala_label_rec.grid(row=j,column=1)
                small_lace_label_rec = Label(result_frame, text=x[2])
                small_lace_label_rec.grid(row=j,column=2)
                big_lace_label_rec = Label(result_frame, text=x[3])
                big_lace_label_rec.grid(row=j,column=3)
                all_over_label_rec = Label(result_frame, text=x[4])
                all_over_label_rec.grid(row=j,column=4)
                sleeves_label_rec = Label(result_frame, text=x[5])
                sleeves_label_rec.grid(row=j,column=5)
                top_data_label_rec = Label(result_frame, text=x[6])
                top_data_label_rec.grid(row=j,column=6)
                dupatta_label_rec = Label(result_frame, text=x[7])
                dupatta_label_rec.grid(row=j,column=7)
                butti_label_rec = Label(result_frame, text=x[8])
                butti_label_rec.grid(row=j,column=8)
                butti_lace_label_rec = Label(result_frame, text=x[9])
                butti_lace_label_rec.grid(row=j,column=9)
                daman_lace_label_rec = Label(result_frame, text=x[10])
                daman_lace_label_rec.grid(row=j,column=10)
                total_label_rec = Label(result_frame, text=x[11])
                total_label_rec.grid(row=j,column=11)
                j+=1
        else:
            # Display a message if no records found
            no_results_label = Label(result_frame, text="No matching records found.")
            no_results_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")

    d_name = Entry(search_frame, width=70,bg="white",fg="black")
    d_name.grid(row=1, column=1, padx=15, pady=5)
    d_name_label = Label(search_frame, text="Enter Design name you want to search : ")
    d_name_label.grid(row=1, column=0, padx=15, pady=5)
    search_button = Button(search_frame, text="Show records", command=ser)
    search_button.grid(row=0, column=0,columnspan=2, padx=15, pady=5, ipadx=330)

def show_data():
    hide_all_frames()
    show_data_frame.pack(fill="both",expand=1)
    def qury():
        # Connect to the database
        conn = sqlite3.connect("design_data.db")
        cursor_data = conn.cursor()
        # Query the database
        cursor_data.execute("SELECT *,oid FROM design ORDER BY design_name ASC")
        records = cursor_data.fetchall()
        # print(records)
        if records:
            des_label = Label(show_data_frame,text="Design no.")
            des_label.grid(row=1,column=0, padx=15, pady=5)
            gala_label = Label(show_data_frame,text="gala")
            gala_label.grid(row=1,column=1, padx=15, pady=5)
            small_lace_label = Label(show_data_frame,text="small lace")
            small_lace_label.grid(row=1,column=2, padx=15, pady=5)
            big_lace_label = Label(show_data_frame,text="big lace")
            big_lace_label.grid(row=1,column=3, padx=15, pady=5)
            all_over_label = Label(show_data_frame,text="all over")
            all_over_label.grid(row=1,column=4, padx=15, pady=5)
            sleeves_label = Label(show_data_frame,text="sleeve")
            sleeves_label.grid(row=1,column=5, padx=15, pady=5)
            top_label = Label(show_data_frame,text="top")
            top_label.grid(row=1,column=6, padx=15, pady=5)
            dupatta_label = Label(show_data_frame,text="dupatta")
            dupatta_label.grid(row=1,column=7, padx=15, pady=5)
            butti_label = Label(show_data_frame,text="butti")
            butti_label.grid(row=1,column=8, padx=15, pady=5)
            butti_lace_label = Label(show_data_frame,text="butti lace")
            butti_lace_label.grid(row=1,column=9, padx=15, pady=5)
            daman_lace_label = Label(show_data_frame,text="daman lace")
            daman_lace_label.grid(row=1,column=10, padx=15, pady=5)
            total_label = Label(show_data_frame,text="total")
            total_label.grid(row=1,column=11, padx=15, pady=5)
            j=2
            for row in records:
                x=[]
                for i in row:
                    x.append(str(i))
                d_name_label_rec = Label(show_data_frame, text=x[0])
                d_name_label_rec.grid(row=j,column=0)
                gala_label_rec = Label(show_data_frame, text=x[1])
                gala_label_rec.grid(row=j,column=1)
                small_lace_label_rec = Label(show_data_frame, text=x[2])
                small_lace_label_rec.grid(row=j,column=2)
                big_lace_label_rec = Label(show_data_frame, text=x[3])
                big_lace_label_rec.grid(row=j,column=3)
                all_over_label_rec = Label(show_data_frame, text=x[4])
                all_over_label_rec.grid(row=j,column=4)
                sleeves_label_rec = Label(show_data_frame, text=x[5])
                sleeves_label_rec.grid(row=j,column=5)
                top_data_label_rec = Label(show_data_frame, text=x[6])
                top_data_label_rec.grid(row=j,column=6)
                dupatta_label_rec = Label(show_data_frame, text=x[7])
                dupatta_label_rec.grid(row=j,column=7)
                butti_label_rec = Label(show_data_frame, text=x[8])
                butti_label_rec.grid(row=j,column=8)
                butti_lace_label_rec = Label(show_data_frame, text=x[9])
                butti_lace_label_rec.grid(row=j,column=9)
                daman_lace_label_rec = Label(show_data_frame, text=x[10])
                daman_lace_label_rec.grid(row=j,column=10)
                total_label_rec = Label(show_data_frame, text=x[11])
                total_label_rec.grid(row=j,column=11)
                j+=1
        else:
            # Display a message if no records found
            no_results_label = Label(show_data_frame, text="No matching records found.")
            no_results_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    query_button = Button(show_data_frame, text="Show records", command=qury)
    query_button.grid(row=0, column=0,columnspan=12, padx=15, pady=5, ipadx=330)

def add_data():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)
    def save_data():
        # Get the values entered by the user
        design_name = d_name.get()
        gala_data = gala.get()
        if(gala_data == ""):
            gala_data='0'
        small_lace_data = small_lace.get()
        if(small_lace_data == ""):
            small_lace_data='0'
        big_lace_data = big_lace.get()
        if(big_lace_data == ""):
            big_lace_data='0'
        all_over_data = all_over.get()
        if(all_over_data == ""):
            all_over_data='0'
        sleeves_data = sleeves.get()
        if(sleeves_data == ""):
            sleeves_data='0'
        top_data_data = top_data.get()
        if(top_data_data == ""):
            top_data_data='0'
        dupatta_data = dupatta.get()
        if(dupatta_data == ""):
            dupatta_data='0'
        butti_data = butti.get()
        if(butti_data == ""):
            butti_data='0'
        butti_lace_data = butti_lace.get()
        if(butti_lace_data == ""):
            butti_lace_data='0'
        daman_lace_data = daman_lace.get()
        if(daman_lace_data == ""):
            daman_lace_data='0'
        total_data = int(gala_data)+int(small_lace_data)+int(big_lace_data)+int(all_over_data)+int(sleeves_data)+int(top_data_data)+int(dupatta_data)+int(butti_data)+int(butti_lace_data)+int(daman_lace_data)
        # Connect to the database
        conn = sqlite3.connect("design_data.db")
        cursor_data = conn.cursor()
        # Insert the data into the database
        cursor_data.execute("INSERT INTO design (design_name, gala, small_lace, big_lace, all_over, sleeves, top_data, dupatta, butti, butti_lace, daman_lace, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(design_name, gala_data, small_lace_data, big_lace_data, all_over_data, sleeves_data, top_data_data, dupatta_data, butti_data, butti_lace_data, daman_lace_data, total_data))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Clear the input fields after saving
        d_name.delete(0, 'end')
        gala.delete(0, 'end')
        small_lace.delete(0, 'end')
        big_lace.delete(0, 'end')
        all_over.delete(0, 'end')
        sleeves.delete(0, 'end')
        top_data.delete(0, 'end')
        dupatta.delete(0, 'end')
        butti.delete(0, 'end')
        butti_lace.delete(0, 'end')
        daman_lace.delete(0, 'end')

    d_name = Entry(add_frame, width=70,bg="white",fg="black")
    d_name.grid(row=0, column=1, padx=15, pady=5)
    gala = Entry(add_frame, width=70,bg="white",fg="black")
    gala.grid(row=1, column=1, padx=15, pady=5)
    small_lace = Entry(add_frame, width=70,bg="white",fg="black")
    small_lace.grid(row=2, column=1, padx=15, pady=5)
    big_lace = Entry(add_frame, width=70,bg="white",fg="black")
    big_lace.grid(row=3, column=1, padx=15, pady=5)
    all_over = Entry(add_frame, width=70,bg="white",fg="black")
    all_over.grid(row=4, column=1, padx=15, pady=5)
    sleeves = Entry(add_frame, width=70,bg="white",fg="black")
    sleeves.grid(row=5, column=1, padx=15, pady=5)
    top_data = Entry(add_frame, width=70,bg="white",fg="black")
    top_data.grid(row=6, column=1, padx=15, pady=5)
    dupatta = Entry(add_frame, width=70,bg="white",fg="black")
    dupatta.grid(row=7, column=1, padx=15, pady=5)
    butti = Entry(add_frame, width=70,bg="white",fg="black")
    butti.grid(row=8, column=1, padx=15, pady=5)
    butti_lace = Entry(add_frame, width=70,bg="white",fg="black")
    butti_lace.grid(row=9, column=1, padx=15, pady=5)
    daman_lace = Entry(add_frame, width=70,bg="white",fg="black")
    daman_lace.grid(row=10, column=1, padx=15, pady=5)

    d_name_label = Label(add_frame, text="Design name : ")
    d_name_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")
    gala_label = Label(add_frame, text="Gala : ")
    gala_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")
    small_lace_label = Label(add_frame, text="Small lace : ")
    small_lace_label.grid(row=2, column=0, padx=15, pady=5, sticky="w")
    big_lace_label = Label(add_frame, text="Big lace : ")
    big_lace_label.grid(row=3, column=0, padx=15, pady=5, sticky="w")
    all_over_label = Label(add_frame, text="All over : ")
    all_over_label.grid(row=4, column=0, padx=15, pady=5, sticky="w")
    sleeves_label = Label(add_frame, text="Sleeves : ")
    sleeves_label.grid(row=5, column=0, padx=15, pady=5, sticky="w")
    top_data_label = Label(add_frame, text="Top data : ")
    top_data_label.grid(row=6, column=0, padx=15, pady=5, sticky="w")
    dupatta_label = Label(add_frame, text="Dupatta : ")
    dupatta_label.grid(row=7, column=0, padx=15, pady=5, sticky="w")
    butti_label = Label(add_frame, text="Butti : ")
    butti_label.grid(row=8, column=0, padx=15, pady=5, sticky="w")
    butti_lace_label = Label(add_frame, text="Butti lace : ")
    butti_lace_label.grid(row=9, column=0, padx=15, pady=5, sticky="w")
    daman_lace_label = Label(add_frame, text="Daman lace : ")
    daman_lace_label.grid(row=10, column=0, padx=15, pady=5, sticky="w")
    add_button = Button(add_frame, text="Add Data", command=save_data)
    add_button.grid(row=11, column=0, columnspan=2, padx=15, pady=5, ipadx=70)

def update_data():
    hide_all_frames()
    update_frame.pack(fill="both",expand=1)
    def udt():
        # Get the new data entered by the user
        new_design_name = d_name.get()
        # Connect to the database
        conn = sqlite3.connect("design_data.db")
        cursor_data = conn.cursor()
        # Execute an SQL UPDATE statement to update the data for the specified design_name
        a=gala_data.get()
        b=small_lace_data.get()
        c=big_lace_data.get()
        d=all_over_data.get()
        e=sleeves_data.get()
        f=top_data_data.get()
        g=dupatta_data.get()
        h=butti_data.get()
        i=butti_lace_data.get()
        j=daman_lace_data.get()
        if(a == ""): a='0'
        if(b == ""): b='0'
        if(c == ""): c='0'
        if(d == ""): d='0'
        if(e == ""): e='0'
        if(f == ""): f='0'
        if(g == ""): g='0'
        if(h == ""): h='0'
        if(i == ""): i='0'
        if(j == ""): j='0'
        cursor_data.execute("UPDATE design SET "
                            "gala=?, small_lace=?, big_lace=?, all_over=?, sleeves=?, "
                            "top_data=?, dupatta=?, butti=?, butti_lace=?, daman_lace=?, "
                            "total=? "
                            "WHERE design_name=?",
                            (int(a), int(b), int(c),
                             int(d), int(e), int(f),
                             int(g), int(h), int(i),
                             int(j), int(a)+int(b)+int(c)+int(d)+int(e)+int(f)+int(g)+int(h)+int(i)+int(j), new_design_name))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Optionally, clear the input fields after updating
        d_name.delete(0, 'end')
        gala_data.delete(0, 'end')
        small_lace_data.delete(0, 'end')
        big_lace_data.delete(0, 'end')
        all_over_data.delete(0, 'end')
        sleeves_data.delete(0, 'end')
        top_data_data.delete(0, 'end')
        dupatta_data.delete(0, 'end')
        butti_data.delete(0, 'end')
        butti_lace_data.delete(0, 'end')
        daman_lace_data.delete(0, 'end')
    # Create Entry fields for other data you want to update
    d_name = Entry(update_frame, width=70, bg="white", fg="black")
    gala_data = Entry(update_frame, width=70, bg="white", fg="black")
    small_lace_data = Entry(update_frame, width=70, bg="white", fg="black")
    big_lace_data = Entry(update_frame, width=70, bg="white", fg="black")
    all_over_data = Entry(update_frame, width=70, bg="white", fg="black")
    sleeves_data = Entry(update_frame, width=70, bg="white", fg="black")
    top_data_data = Entry(update_frame, width=70, bg="white", fg="black")
    dupatta_data = Entry(update_frame, width=70, bg="white", fg="black")
    butti_data = Entry(update_frame, width=70, bg="white", fg="black")
    butti_lace_data = Entry(update_frame, width=70, bg="white", fg="black")
    daman_lace_data = Entry(update_frame, width=70, bg="white", fg="black")
    # Position the Entry fields
    row_offset = 0
    fields = [
        ("Design name: ", d_name),
        ("Gala: ", gala_data),
        ("Small Lace: ", small_lace_data),
        ("Big Lace: ", big_lace_data),
        ("All Over: ", all_over_data),
        ("Sleeves: ", sleeves_data),
        ("Top Data: ", top_data_data),
        ("Dupatta: ", dupatta_data),
        ("Butti: ", butti_data),
        ("Butti Lace: ", butti_lace_data),
        ("Daman Lace: ", daman_lace_data),
    ]
    for label, entry in fields:
        Label(update_frame, text=label).grid(row=row_offset, column=0, padx=15, pady=5, sticky="w")
        entry.grid(row=row_offset, column=1, padx=15, pady=5)
        row_offset += 1
    update_button = Button(update_frame, text="Update Data",command=udt)
    update_button.grid(row=12,column=0,columnspan=2,padx=10,pady=10)

def delete_data():
    hide_all_frames()
    delete_frame.pack(fill="both",expand=1)
    def dlt():
        # Get the design name entered by the user
        design_name_to_delete = d_name.get()
        # Connect to the database
        conn = sqlite3.connect("design_data.db")
        cursor_data = conn.cursor()
        # Execute an SQL DELETE statement to delete the record with the specified design_name
        cursor_data.execute("DELETE FROM design WHERE design_name = ?", (design_name_to_delete,))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Optionally, clear the input field after deleting
        d_name.delete(0, 'end')
    d_name = Entry(delete_frame, width=70,bg="white",fg="black")
    d_name.grid(row=0, column=1)
    d_name_label = Label(delete_frame, text="Enter Design name you want to delete : ")
    d_name_label.grid(row=0, column=0, padx=15, pady=5)
    dlt_button = Button(delete_frame, text="Delete Data",command=dlt)
    dlt_button.grid(row=1,column=0,columnspan=2,padx=15,pady=5)

# Function for deleting previous frames widgets
def hide_all_frames():
    for widget in search_frame.winfo_children():
        widget.destroy()
    for widget in show_data_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()
    for widget in update_frame.winfo_children():
        widget.destroy()
    for widget in delete_frame.winfo_children():
        widget.destroy()

    search_frame.pack_forget()
    show_data_frame.pack_forget()
    add_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()

# Home menu for search and exit.
home_menu = Menu(main_menu)
main_menu.add_cascade(label="Home",menu=home_menu)
home_menu.add_command(label="Search",command=search_item)
home_menu.add_separator()
home_menu.add_command(label="Show data",command=show_data)
home_menu.add_separator()
home_menu.add_command(label="Exit",command=root.quit)

# Data Management menu for add, update, and delete.
manage_data_menu = Menu(main_menu)
main_menu.add_cascade(label="Manage Data",menu=manage_data_menu)
manage_data_menu.add_command(label="Add",command=add_data)
manage_data_menu.add_separator()
manage_data_menu.add_command(label="Update",command=update_data)
manage_data_menu.add_separator()
manage_data_menu.add_command(label="Delete",command=delete_data)

# Making Frames.
search_frame = Frame(root, width=1000, height=800, bg="#1f1f1f")
show_data_frame = Frame(root, width=1000, height=800, bg="#1f1f1f")
add_frame = Frame(root, width=1000, height=800, bg="#1f1f1f")
update_frame = Frame(root, width=1000, height=800, bg="#1f1f1f")
delete_frame = Frame(root, width=1000, height=800, bg="#1f1f1f")

# Main loop...
root.mainloop()