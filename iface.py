from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x120')


def make_a_raw(i):
    lblx = Label(window, text="x*")
    lblx.grid(column=0, row=i)
    x = Entry(window,width=5)
    x.grid(column=1, row=i)
    lbly = Label(window, text="y*")
    lbly.grid(column=2, row=i)
    y = Entry(window,width=5)
    y.grid(column=3, row=i)
    lblz = Label(window, text="z*")
    lblz.grid(column=4, row=i)
    z = Entry(window, width=5)
    z.grid(column=5, row=i)
    lblf = Label(window, text="=")
    lblf.grid(column=6, row=i)
    f = Entry(window, width=5)
    f.grid(column=7, row=i)
    return x, y, z, f

xs = []
for i in range(3):
    xs.append(make_a_raw(i))


si_btn = Button(window, text="simple iteration")
si_btn.grid(column=3, row=4)

from iteration import SimpleIterationRoots


def si(window):
    global xs
    a = []
    b = []
    for raw in xs:
        t = []
        for x in raw:
            t.append(float(x.get()))
        b.append([t.pop()])
        a.append(t)

    from iteration import SimpleIterationRoots
    from print_res import print_tbl
    import numpy as np

    print_tbl(SimpleIterationRoots(np.array(a), np.array(b), 0.001))

def sr(window):
    global xs
    a = []
    b = []
    for raw in xs:
        t = []
        for x in raw:
            t.append(float(x.get()))
        b.append([t.pop()])
        a.append(t)

    from zeidel import zeidel
    from print_res import print_tbl
    import numpy as np

    print_tbl(zeidel(np.array(a), np.array(b), 0.001))

si_btn.bind("<Button-1>", si)

gs_btn = Button(window, text="gauss-seidel")
gs_btn.grid(column=3, row=5)

gs_btn.bind("<Button-1>", sr)

window.mainloop()