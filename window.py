from tkinter import *
from tkinter import messagebox
import numpy as np
from tkinter.scrolledtext import ScrolledText
from task import *
from symbol_func import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

alpha1 = "alpha_k = 1/(k+1)\n------------------------\nне гарантирует монотонности"
alpha2 = "alpha = 1\nwhile J(u_(k+1))>=J(u_k):\n    alpha/=2\n------------------------\nгарантирует монотонность"
alpha3 = "0<=alpha_k<=1\nf_k(alpha_k) = min(0,1)f_k(a)\nf_k(a)=J(u_k+a(u1_k-u_k))\n------------------------\nметод минизации\nфункции одной переменной"


root = Tk()
root.title("Fuck")
root.geometry("600x600")

status = 0#0 - примеры 1- ввод своей функции
alpha_type = IntVar()
alpha_type.set(1)
alpha_text = StringVar()
alpha_text.set(alpha1)
u0 = StringVar()
u0.set("0;0.0")
func_text = StringVar()
func_text.set("x**2+x*y+y**2")
is_steps_frames = IntVar()
is_steps_frames.set(1)
steps_frames = StringVar()
steps_frames.set(10000)
is_accuracy_frames = IntVar()
is_accuracy_frames.set(1)
accuracy_frames = StringVar()
accuracy_frames.set("0.000001")


class Calculate_and_print_ans:
    def __init__(self):
        self.root = Tk()
        self.root.title("Answer")
        self.root.geometry("800x400")
    def calculate(self, func, frames, fder, u_0,  alpha_num, eps, steps):
        func0 = Func(func, fder)
        alpha = alpha_1
        if alpha_num.get() == 2:
            alpha = alpha_2
        elif alpha_num.get() == 3:
            alpha = alpha_3
        print(alpha_num.get())
        job = Job(func0, frames0, np.array(list(map(float, (u_0.split(";"))))), alpha) 
        job.check_errors()
        print(eps, " ", steps)
        self.answ = calculate_m(job, float(eps), int(steps))
    def __get_step_string(self):
        a = "i|  f  |  u  \n--------------------\n"
        for i in range(0, len(self.answ[2])):
            a+="{}| {} | {} \n".format(i, self.answ[2][i], self.answ[3][i])
        return a

    def draw(self):
        Label(self.root, text="f:     {}".format(self.answ[0]), fg="#000", wraplength=0, font="Arial 11", padx="10", justify=RIGHT, anchor="nw").place(relx=.0, rely=.05, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)
        Label(self.root, text="u:     {}".format(self.answ[1]), fg="#000", wraplength=0, font="Arial 11", padx="10", justify=RIGHT, anchor="nw").place(relx=.0, rely=.1, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)
        Label(self.root, text="steps: {}".format(self.answ[4]), fg="#000", wraplength=0, font="Arial 11", padx="10", justify=RIGHT, anchor="nw").place(relx=.0, rely=.15, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)
        Label(self.root, text="eps:   {}".format(self.answ[5]), fg="#000", wraplength=0, font="Arial 11", padx="10", justify=RIGHT, anchor="nw").place(relx=.0, rely=.2, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)
        st = ScrolledText(self.root)
        st.place(relx=.4, rely=1, anchor="sw", relheight=1, relwidth=.6, bordermode=INSIDE)
        st.insert(INSERT, self.__get_step_string())
        f = Figure(dpi=100)
        a = f.add_subplot(111)
        a.plot(self.answ[2])
        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx=.0, rely=1, anchor="sw", relheight=.4, relwidth=.4, bordermode=INSIDE)
#expand=True
        self.root.mainloop()



def set_alpha_text():
    if alpha_type.get() == 1:
        alpha_text.set(alpha1)
    elif alpha_type.get() == 2:
        alpha_text.set(alpha2)
    else:
        alpha_text.set(alpha3)

def examples_button_press():
    global status
    if status == 0:
        status = 1
        hide_examples()
    else: 
        status = 0
        btn_example0.place(relx=.0, rely=.25, anchor="sw", relheight=.25, relwidth=.6, bordermode=INSIDE)
        btn_example1.place(relx=.0, rely=.5, anchor="sw", relheight=.25, relwidth=.6, bordermode=INSIDE)
def hide_examples():
    btn_example0.place_forget()
    btn_example1.place_forget()
def example_0_press():
    stps = "-1"
    if is_steps_frames.get() == 1:
        stps = steps_frames.get()
    acc = "-1"
    if is_accuracy_frames.get() == 1:
        acc = accuracy_frames.get()
    c1 = Calculate_and_print_ans()
    c1.calculate(f0, frames0 ,f0der, u0.get(), alpha_type, acc, stps)
    c1.draw()
def example_1_press():
    stps = "-1"
    if is_steps_frames.get() == 1:
        stps = steps_frames.get()
    acc = "-1"
    if is_accuracy_frames.get() == 1:
        acc = accuracy_frames.get()
    c1 = Calculate_and_print_ans()
    c1.calculate(f0, frames1 ,f0der, u0.get(), alpha_type, acc, stps)
    c1.draw()

def my_func_button_press():
    global status
    status = 1

def calculate():
    stps = "-1"
    if is_steps_frames.get() == 1:
        stps = steps_frames.get()
    acc = "-1"
    if is_accuracy_frames.get() == 1:
        acc = accuracy_frames.get()
    c1 = Calculate_and_print_ans()
    f,d = get_func_and_st_der(func_text.get())
    c1.calculate(f, frames0 ,d, u0.get(), alpha_type, acc, stps)
    c1.draw()


btn0 = Button(text="examples", background="#ccc", foreground="#000", activebackground="#ccc",
             padx="10", pady="4", font="Arial 14", width="20", command=examples_button_press)
btn0.place(relx=.8, rely=.05, anchor="sw", relheight=.05, relwidth=.195, bordermode=INSIDE)
#btn1 = Button(text="own", background="#ccc", foreground="#000", activebackground="#ccc",
#             padx="10", pady="4", font="Arial 14", width="20", command=my_func_button_press)
#btn1.place(relx=.8, rely=.1, anchor="sw", relheight=.05, relwidth=.195, bordermode=INSIDE)
btn2 = Button(text="calculate", background="#ccc", foreground="#000", activebackground="#ccc",
             padx="10", pady="4", font="Arial 14", width="20", command=calculate)
btn2.place(relx=.6, rely=.99, anchor="sw", relheight=.05, relwidth=.395, bordermode=INSIDE)


rb1 = Radiobutton(text="Alpha 1", value=1, variable=alpha_type, padx=10, pady=4, font="Arial 14", command=set_alpha_text)
rb1.place(relx=.6, rely=.05, anchor="sw", relheight=.05, relwidth=.2, bordermode=INSIDE)
Radiobutton(text="Alpha 2", value=2, variable=alpha_type, padx=10, pady=4, font="Arial 14", command=set_alpha_text).place(relx=.6, rely=.1, anchor="sw", relheight=.05, relwidth=.2, bordermode=INSIDE)
Radiobutton(text="Alpha 3", value=3, variable=alpha_type, padx=10, pady=4, font="Arial 14", command=set_alpha_text).place(relx=.6, rely=.15, anchor="sw", relheight=.05, relwidth=.2, bordermode=INSIDE)
Label(textvariable=alpha_text, fg="#000", bg="#bbb", wraplength=0, font="Arial 12", padx="10", pady="4", justify=LEFT, anchor="nw", bd=.05).place(relx=.6, rely=.89, anchor="sw", relheight=.74, relwidth=.395, bordermode=INSIDE)
Label(text="u0:", fg="#000", wraplength=0, font="Arial 12", padx="10", pady="4", justify=RIGHT, anchor="ne").place(relx=.6, rely=.94, anchor="sw", relheight=.05, relwidth=.2, bordermode=INSIDE)
Entry(textvariable=u0).place(relx=.8, rely=.94, anchor="sw", relheight=.05, relwidth=.195, bordermode=INSIDE)

Label(text="f:", fg="#000", wraplength=0, font="Arial 12", padx="10", pady="4", justify=RIGHT, anchor="ne").place(relx=.0, rely=.05, anchor="sw", relheight=.05, relwidth=.1, bordermode=INSIDE)
Entry(textvariable=func_text).place(relx=.1, rely=.05, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)
Label(text="frames:", fg="#000", wraplength=0, font="Arial 12", padx="10", pady="4").place(relx=.0, rely=.1, anchor="sw", relheight=.05, relwidth=.6, bordermode=INSIDE)
ScrolledText().place(relx=.1, rely=.4, anchor="sw", relheight=.3, relwidth=.4, bordermode=INSIDE)

Checkbutton(text="Steps", variable=is_steps_frames, onvalue=1, offvalue=0).place(relx=.0, rely=.95, anchor="sw", relheight=.05, relwidth=.1, bordermode=INSIDE)
Entry(textvariable=steps_frames).place(relx=.1, rely=.95, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)

Checkbutton(text="Accur", variable=is_accuracy_frames, onvalue=1, offvalue=0).place(relx=.0, rely=1, anchor="sw", relheight=.05, relwidth=.1, bordermode=INSIDE)
Entry(textvariable=accuracy_frames).place(relx=.1, rely=1, anchor="sw", relheight=.05, relwidth=.4, bordermode=INSIDE)

btn_example0_text = "f(x,y)=x^2+xy+y^2\n0<=x<=1\n-1<=y<=0"
btn_example0 = Button(text=btn_example0_text, background="#ccc", foreground="#000", activebackground="#ccc",
             padx="10", pady="4", font="Arial 14", width="20", command=example_0_press)
btn_example1_text = "f(x,y)=x^2+xy+y^2\n0x+y<=0\n0x-y<=1\nx+0y<=1\n-x+0y<=0"
btn_example1 = Button(text=btn_example1_text, background="#ccc", foreground="#000", activebackground="#ccc",
             padx="10", pady="4", font="Arial 14", width="20", command=example_1_press)
btn_example0.place(relx=.0, rely=.25, anchor="sw", relheight=.25, relwidth=.6, bordermode=INSIDE)
btn_example1.place(relx=.0, rely=.5, anchor="sw", relheight=.25, relwidth=.6, bordermode=INSIDE)
#btn_example0.place_forget()

#def show_message():
#    messagebox.showinfo("GUI Python", message.get())#

root.mainloop()

