from tkinter import END, HIDDEN, Tk,Canvas,Frame,Label,Entry,Button,W,E,Listbox
import psycopg2


connData = {
    'db':input('Database name: '),
    'usr':input('User: '),
    'pwd':input('Password: '),
    'host':input('Host: '),
    'port':input('Port:')
}

# instancia de tk para crear una ventana
root = Tk()
root.title("Students")

# funcion para guardar 
def save_new_student(connData,name,age,address):
    conn = connect_to_db_(connData)
    cursor = conn.cursor()
    query = '''INSERT INTO students(name,age,address) VALUES (%s,%s,%s)'''
    cursor.execute(query, (name,age,address))
    print("Data saved")
    conn.commit()
    conn.close()
    # refrescar
    display_students_(connData)

def connect_to_db_(connData):
    conn = psycopg2.connect(
        dbname = connData['db'],
        user = connData['usr'], 
        password = connData['pwd'],
        host = connData['host'],
        port = connData['port']
        )
    return conn

def display_students_(connData):
    conn = connect_to_db_(connData)
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)

    # retorna una lista de todos los datos de la db
    row = cursor.fetchall()

    # lost tengo que recorrer en un listbox para irlos mostrando
    listbox = Listbox(frame, width = 20, height = 5)
    listbox.grid(row = 10, columnspan = 4, sticky = W + E)

    for x in row:
        listbox.insert(END,x)

    conn.commit()
    conn.close()



# instancia de Canvas
canvas = Canvas(root, height = 380, width = 400)
canvas.pack()

# para colocar espaciado y posicionar los elementos a partir de una grilla
frame = Frame()
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8) 

# etiquetas y botones
label = Label(frame, text = 'Add a student')
label.grid(row = 0, column = 1)

# crear inputs

# name
label = Label(frame, text = 'Name')
label.grid(row = 1, column = 0)

entry_name = Entry(frame)
entry_name.grid(row = 1, column = 1)

# age
label = Label(frame, text = 'Age')
label.grid(row = 2, column = 0)

entry_age = Entry(frame)
entry_age.grid(row = 2, column = 1)

# address
label = Label(frame, text = 'Address')
label.grid(row = 3, column = 0)

entry_address = Entry(frame)
entry_address.grid(row = 3, column = 1)

# boton
button = Button(frame, text = 'Add', command = lambda: save_new_student(connData,entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row = 4, column = 1, sticky = W + E)

# buscar
label = Label(frame, text = 'Search')
label.grid(row = 5, column = 1)

label = Label(frame, text = 'Search by ID')
label.grid(row = 6, column = 0)

id_search = Entry(frame)
id_search.grid(row = 6, column = 1)


display_students_(connData)

root.mainloop() 