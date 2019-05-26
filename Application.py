from Front import *
import Backend as core

app = None

def view_command():
    rows = core.view()
    app.listCEP.delete(0, END)
    for r in rows:
        app.listCEP.insert(END, r)

def search_command():
    app.listCEP.delete(0, END)
    rows = core.search(app.txt1.get(), app.txt2.get(), app.txt3.get(), app.txt4.get())
    for r in rows:
        app.listCEP.insert(END, r)

def insert_command():
    core.insert(app.txt1.get(), app.txt2.get(), app.txt3.get(), app.txt4.get())
    view_command()

def update_command():
    core.update(selected[0],app.txt1.get(),app.txt2.get(),app.txt3.get(), app.txt4.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listCEP.curselection()[0]
    selected = app.listCEP.get(index)
    app.ent1.delete(0, END)
    app.ent1.insert(END, selected[1])
    app.ent2.delete(0, END)
    app.ent2.insert(END, selected[2])
    app.ent3.delete(0, END)
    app.ent3.insert(END, selected[3])
    app.ent4.delete(0, END)
    app.ent4.insert(END, selected[4])
    return selected


if __name__ == "__main__":
    app = Front()
    app.listCEP.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
app.run()
