'''

This example uses the getHistoricalData function to extract and plot a time series in Python.

DL = darren lefcoe

DL uses PAGE (for python) to make a nice GUI with Tkinter.
The builder is here: https://sourceforge.net/projects/page/

The can directly copy and paste the code.

Other GUI framework options are: PyQt, kivy, BeeWare, pyGame

'''



#import sys
import tkinter as tk
import tradingeconomics as te


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt




def loginProcess():
    keyGiven = ''
    keyGuest = 'guest:guest'
    
    
    # used guest key for testing if no Given key (empty string)
    if keyGiven == '':
        keyGiven = keyGuest
    
    #without a client key only a small sample of data will be given.
    try:
        te.login(keyGiven)
        print('login succesful')
    except:
        print('login failed')





def StartGUI():
    
    ''' function to run the GUI  '''
    mainPage = tk.Tk()
    
    
    def destroyMainPage():
        ''' nested function to close the app '''
        mainPage.destroy()
        print('The app is closed.')
        
    def getDataPressed(countryToUse, IndicToUse):
        print('get data was pressed')
        getHistoricData(countryToUse, IndicToUse)
        labelOutput = tk.Label(mainPage, width = 25, text = 'data for ' + entry1.get() + ' ' + entry2.get())
        labelOutput.grid(row=r, column=0)
    

    
    # counter for the rows
    r = 0
    
    # the title of the GUI
    mainPage.title('Historic Chart GUI')
    
    mainPage.grid_rowconfigure(0, minsize = 50)

    
    label0 = tk.Label(mainPage, width = 25, text = 'Enter the required parameters:')
    label0.grid(row=r,column=0)
    r += 1
    
    
    label1 = tk.Label(mainPage, width = 25, text = 'Country')
    label1.grid(row=r,column=0)
    
    entry1 = tk.Entry(mainPage)
    entry1.insert(0, 'United states')
    entry1.grid(row=r, column=1)
    r += 1
    
    

    label2 = tk.Label(mainPage, width = 25, text = 'indicator')
    label2.grid(row=r,column=0)
    
    entry2 = tk.Entry(mainPage)
    entry2.insert(0, 'Exports')
    entry2.grid(row=r, column=1)
    r += 1

        
    #command = lambda: getHistoricData(entry1.get(), entry2.get())
    
    
    # a button to get historical data
    button = tk.Button(mainPage, text = 'get data', width = 25, command = lambda:getDataPressed(entry1.get(), entry2.get()))
    button.grid(row=r,column=0, padx=10)
    
    
    
    # a simple close button
    button2 = tk.Button(mainPage, text = 'stop', width = 25, command = destroyMainPage)
    button2.grid(row=r,column=1, padx=10, pady=20)
    
    r += 1
    
    label3 = tk.Label(mainPage, width = 25, text = '--- Trading Economics ---')
    label3.grid(row=r, column=1)
    
    labelOutput = tk.Label(mainPage, width = 25, text = 'data for ' + entry1.get() + ' ' + entry2.get())
    labelOutput.grid(row=r, column=0)
    
    
    mainPage.mainloop()
    


def getHistoricData(countryToUse, indicToUse):
    ''' function to get data given country and indicator  '''
    
    
    # code to login
    loginProcess()

    print('getting data...')
    
    
    # code here for getting data
    mydata = te.getHistoricalData(country = countryToUse, indicator = indicToUse)
    
    #plot a simple chart in the cmd line
    plt.title(countryToUse + " - " + indicToUse)
    plt.grid(True)
    plt.ylabel("Indicator - " + indicToUse)
    plt.xlabel("Historical dates")
    
    plt.plot(mydata)
    plt.show()
    
    # plot chart to a new GUI page
    graphPage = tk.Tk()

    graphPage.title('A chart of ' + countryToUse + ' ' + indicToUse)
    
    w = tk.Label(graphPage, text="- - - Graph Page - - -", font=("Helvetica", 16))
    w.pack()
    
    w = tk.Label(graphPage, text="A chart of " + countryToUse + " - " + indicToUse)
    w.pack()
        
    
    f = Figure(figsize=(7,7), dpi=60)

    a = f.add_subplot(111)

    a.plot(mydata)
    a.set_xlabel('Historical dates')
    a.set_ylabel(indicToUse)
    a.grid(True)
    a.set_title(countryToUse + " - " + indicToUse)
    
    canvas = FigureCanvasTkAgg(f, graphPage)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas,graphPage)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    
    
    print('data complete')





# routines to run

StartGUI()






    
    
    