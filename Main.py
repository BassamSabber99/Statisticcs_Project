from os import stat_result
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib as plt
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats





def Chart():
    toplevel = Toplevel(My_Window)
    width_of_Window = 1000
    height_of_Window = 500
    screen_Width = My_Window.winfo_screenwidth()
    screen_height = My_Window.winfo_screenheight()
    x_coordinate = (screen_Width / 2) - (width_of_Window / 2)
    y_coordinate = (screen_height / 2) - (height_of_Window / 2)
    toplevel.title("Charts two_Diminsions")
    toplevel.resizable(width=False, height=False)
    toplevel.configure(bg="#DDD")
    toplevel.geometry("%dx%d+%d+%d" % (width_of_Window, height_of_Window, x_coordinate, y_coordinate))
    style = ttk.Style()
    style.configure("TButton", font="Serif 15")
    style.configure("TEntry", font=('Arial', 10))
    labeldimx = Label(toplevel, text="X", bg="#DDD", font="Atoma  20")
    labeldimx.place(x=90, y=20)
    entryx = ttk.Entry(toplevel, width=130)
    entryx.place(x=120, y=30)
    labeldimy = Label(toplevel, text="Y", bg="#DDD", font="Atoma  20")
    labeldimy.place(x=90, y=50)
    entryy = ttk.Entry(toplevel, width=130)
    entryy.place(x=120, y=60)
    boxplot = ttk.Button(toplevel, text="BoxPlot")
    def BoxPlot():
        x = entryx.get()
        y = entryy.get()
        if entryx.get() == "" or entryy.get() == "":
            messagebox.showinfo("Error","Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        plt.boxplot(m,n)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("BoxPlot")

        plt.show()
    boxplot.configure(command=BoxPlot)
    histogram = ttk.Button(toplevel, text="Histogram")
    barchart = ttk.Button(toplevel, text="BarChart")
    scatterplot = ttk.Button(toplevel,text="ScatterPlot")
    def ScatterPlot():
        x = entryx.get()
        y = entryy.get()
        if entryx.get() == "" or entryy.get() == "":
            messagebox.showinfo("Error", "Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        plt.scatter(m, n, s=10, marker='*')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("ScatterPlot")

        plt.show()
    scatterplot.configure(command=ScatterPlot)
    histogram.place(x=250, y=150)
    def histogramm():
        x = entryx.get()
        y = entryy.get()
        if entryx.get() == "" or entryy.get() == "":
            messagebox.showinfo("Error", "Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        plt.hist(n,m,histtype='bar',rwidth=0.5)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Histogram")

        plt.show()
    histogram.config(command = histogramm)


    barchart.place(x=700, y=150)
    boxplot.place(x=550, y=150)
    def barchar():
        x = entryx.get()
        y = entryy.get()
        if entryx.get() == "" or entryy.get() == "":
            messagebox.showinfo("Error", "Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        plt.bar(n, m)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("BarChart")

        plt.show()
    barchart.config(command=barchar)
    scatterplot.place(x=400,y=150)
    style.configure("TEntry", font=('Arial', 10))
    labeldim = Label(toplevel, text="X", bg="#DDD", font="Atoma  20")
    labeldim.place(x=90, y=290)
    entryx1 = ttk.Entry(toplevel, width=130)
    entryx1.place(x=120, y=300)
    piechart = ttk.Button(toplevel, text="PieChart")

    def piechar():
        x = entryx1.get()
        if entryx1.get() == "":
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        plt.pie(n)
        plt.title("Pie Chart")
        plt.show()
    piechart.config(command = piechar)
    piechart.place(x=500, y=350)
    back = ttk.Button(toplevel, text="Back", command=toplevel.destroy)
    back.place(x=50, y=450)


def Calculations():
    toplevel = Toplevel(My_Window)
    width_of_Window = 1000
    height_of_Window = 500
    screen_Width = My_Window.winfo_screenwidth()
    screen_height = My_Window.winfo_screenheight()
    x_coordinate = (screen_Width / 2) - (width_of_Window / 2)
    y_coordinate = (screen_height / 2) - (height_of_Window / 2)
    toplevel.title("Calculations")
    toplevel.resizable(width=False, height=False)
    toplevel.configure(bg="#DDD")
    toplevel.geometry("%dx%d+%d+%d" % (width_of_Window, height_of_Window, x_coordinate, y_coordinate))
    style = ttk.Style()
    style.configure("TButton", font="Serif 15")
    mean = ttk.Button(toplevel, text="Mean")
    mean.place(x=50,y=50);
    mode = ttk.Button(toplevel,text="Mode")
    mode.place(x=50,y=150)
    median= ttk.Button(toplevel,text="Median")
    median.place(x=50,y=250)
    samplevariance = ttk.Button(toplevel,text="Sample Variance")
    samplevariance.place(x=200,y=50)
    standarddeviation = ttk.Button(toplevel,text="Standard Deviation")
    standarddeviation.place(x=200,y=150)
    iqr = ttk.Button(toplevel,text="IQR")
    iqr.place(x=200,y=250)
    zscore = ttk.Button(toplevel,text="Z-Score")
    zscore.place(x=150,y=300)
    numbers=ttk.Entry(toplevel, width=50)
    numbers.place(x=100,y=350)
    xl=Label(toplevel,text="Numbers", bg="#DDD", font="Atoma  12")
    xl.place(x=30,y=350)
    def Mean():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result",statistics.mean(n))
    mean.config(command=Mean)

    def Median():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result",statistics.median(n))
    median.config(command = Median)

    def Mode():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result",statistics.mode(n))
    mode.config(command=Mode)

    def Varaince():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result",statistics.variance(n))
    samplevariance.config(command=Varaince)

    def StandardDeviation():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result", statistics.stdev(n))
    standarddeviation.config(command = StandardDeviation)

    def median(a, l, r):
        if r % 2 != 0:
            r = r + 1
        n = r - l + 1
        n = (n + 1) // 2 - 1
        return n + l

    def iqrr(a,n):
        a.sort()
        # Index of median of entire data
        mid_index = median(a, 0, n)
        # Median of first half
        Q1 = a[median(a, 0, mid_index)]
        # Median of second half
        Q3 = a[median(a, mid_index + 1, n)]
        # IQR calculation
        return (Q3 - Q1)

    def IQR():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        messagebox.showinfo("Result",iqrr(n,n.__len__()))
    iqr.config(command=IQR)

    def Zscore():
        x = numbers.get()
        if numbers.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        y = x.split(',')
        n = []
        i = 0
        while i < y.__len__():
            n.append(int(y[i]))
            i = i + 1
        ax = stats.zscore(n)
        j=0
        a=""
        while j < n.__len__():
            a += str(ax[j])+'\n'
            j = j + 1
        messagebox.showinfo("Result",a)
    zscore.config(command = Zscore)


    correlation = ttk.Button(toplevel,text= "Correlation")
    correlation.place(x=600,y=150)
    samplelinearregression = ttk.Button(toplevel,text="Sample Linear Regression")
    samplelinearregression.place(x=750,y=150)
    data1 = ttk.Entry(toplevel, width=50)
    data1.place(x=690, y=300)
    xl = Label(toplevel, text="Data1", bg="#DDD", font="Atoma  12")
    xl.place(x=630, y=300)
    data2 = ttk.Entry(toplevel, width=50)
    data2.place(x=690, y=350)
    x2 = Label(toplevel, text="Data2", bg="#DDD", font="Atoma  12")
    x2.place(x=630, y=350)

    def calculate_Sum(list=[]):
        c = 0
        for items in range(list.__len__()):
            c = c + list[items]
        return c

    def calculate_mult(list=[],list2=[]):
        c = 0
        for items in range(list.__len__()):
            c = c + list[items]*list2[items]
        return c

    def calculatesqaure(list=[]):
        c = 0
        for items in range(list.__len__()):
            c = c + (list[items]*list[items])
        return c

    def Correlation():
        x = data1.get()
        y = data2.get()
        if data1.get() == "" or data2.get() == "" :
            messagebox.showinfo("Error", "Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        z = n.__len__()*(calculate_mult(n,m))-(calculate_Sum(m)*calculate_Sum(n))
        r = math.sqrt((n.__len__()*calculatesqaure(n)-math.pow(calculate_Sum(n),2))*(m.__len__()*calculatesqaure(m)-math.pow(calculate_Sum(m),2)))
        messagebox.showinfo("Result",z/r)
    correlation.config(command=Correlation)

    def estimate_coef(x, y):
        #    x = np.array([1, 2, 3, 4])
        #   y = np.array([1, 2, 3, 4])

        # number of observations/points
        n = np.size(x)

        # mean of x and y vector
        m_x, m_y = np.mean(x), np.mean(y)

        # calculating cross-deviation and deviation about x
        SS_xy = np.sum(y * x) - n * m_y * m_x
        SS_xx = np.sum(x * x) - n * m_x * m_x
        # calculating regression coefficients
        b_1 = SS_xy / SS_xx
        b_0 = m_y - b_1 * m_x
        return (b_0, b_1)

    def RegressionLinear():
        x = data1.get()
        y = data2.get()
        if data1.get() == "" or data2.get() == "":
            messagebox.showinfo("Error", "Empty Field")
            return
        z = x.split(',')
        c = y.split(',')
        m = []
        n = []
        i = 0
        while i < z.__len__():
            n.append(int(z[i]))
            i = i + 1
        i = 0
        while i < c.__len__():
            m.append(int(c[i]))
            i = i + 1
        a = np.asarray(n)
        b = np.asarray(m)
        messagebox.showinfo("Result",estimate_coef(a,b))

    samplelinearregression.config(command = RegressionLinear)
    back = ttk.Button(toplevel, text="Back", command=toplevel.destroy)
    back.place(x=50, y=450)


My_Window = Tk()
width_of_Window = 1000
height_of_Window = 500

screen_Width = My_Window.winfo_screenwidth()
screen_height = My_Window.winfo_screenheight()

x_coordinate = (screen_Width / 2) - (width_of_Window / 2)
y_coordinate = (screen_height / 2) - (height_of_Window / 2)

My_Window.title("Statistical Analysis")

My_Window.resizable(width=False, height=False)
My_Window.configure(bg="#DDD")
My_Window.geometry("%dx%d+%d+%d" % (width_of_Window, height_of_Window, x_coordinate, y_coordinate))

style = ttk.Style()
style.configure("TButton", font="Serif 15")

label = Label(My_Window, text="Statistical Analysis", bg="black", fg="green", font="Broadway 30 bold", width=1000)
label.pack()


Charts = ttk.Button(text="Charts", command = Chart)

Charts.place(x=700, y=235)

Calculations = ttk.Button(text="Calculation",  command = Calculations)

Calculations.place(x=200, y=230)

My_Window.mainloop()