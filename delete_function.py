
def display():
    conn = sqlite3.connect(("addressBook.db"))
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)
    all_records = ""
    for record in records:
        all_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[-1]) + "\n"

    query_label = Label(root, text=
    all_records)
    query_label.grid(row=6, column=1, columnspan=3)


def delete():
    # Establishing Connection with database
    conn = sqlite3.connect(("addressBook.db"))

    # Creating Cursor..
    c = conn.cursor()
    # Executing Sql Query.....DELETE from TABLE_NAME WHERE oid = +
    c.execute("DELETE from addresses WHERE oid = " + deletefield.get())
    showinfo(title='Information Box', message="Deleted Successful")
    conn.commit()
    conn.close()