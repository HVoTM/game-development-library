import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg') # specify the backend that we wish to use with matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import urllib, requests, time
import json

import pandas as pd

from matplotlib import style

LARGE_FONT = ("Verdana", 12)
style.use('ggplot')

# defining aa figure and subplot
f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

def Animate(i): # DEPRECATED -- ---
    """
    Graph live Bitcoin prices from the BTC-e API
    f will be drawn as we click onto pagethree button GUI
    """
    """
    pullData = open('sampletext.txt', 'r').read()
    dataArray = pullData.split('\n')
    X, Y  = [], []

    for line in dataArray:
        if len(line) > 1: # len of 
            x, y = line.split(',')
            X.append(int(x))
            Y.append(int(y))
    a.clear()
    a.plot(X, Y)
    """
    # Pulling the data from the BTC-e public API 
    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.readall().decode("utf-8")
    # Using the json module to actually process the data
    data = json.loads(data)
    
    # making sure
    if "btc_usd" not in data:
        raise KeyError("Key btc_usd not found in the response")
    
    data = pd.DataFrame(data["btc_usd"])

    # Dividing data into "bid" and "task"
    # FYI: In case you do not know, a "bid" is an offer to buy and an "ask" is an offer to sell. 
    # In this case, these are offers that actually were accepted, as opposed to "depth," which is all current "offers."
    buys = data[(data['type']=="bid")]
    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]") # convert the data into datetime64 format, making it more of a time-series data
    buyDates = (buys["datestamp"]).tolist()

    sells = data[(data['type']=="ask")]
    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    sellDates = (sells["datestamp"]).tolist()

    a.clear()
    a.plot_date(buyDates, buys["price"])
    a.plot_date(sellDates, sells["price"])

def FetchBitcoinPrice():
    dataLink = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(dataLink)

    try:
        if response.status_code == 200:
            data = response.json()
            return float(data['bpi']['USD']['rate'].replace(',', ''))
        else:
            print("Failed to fetch data.")
            return None
        
    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None
    
timestamps = []
prices = []

def VisualizeBTCprice(i):
    # Initialize lists to store time and price data
    global timestamps, prices
    price = FetchBitcoinPrice()

    if price is not None:
        timestamps.append(time.strftime("%H:%M:%S"))  # Current time
        prices.append(price)
        
        # Limit the number of points displayed
        if len(timestamps) > 20:  # Keep only the last 20 data points
            timestamps = timestamps[-20:]
            prices = prices[-20:]

        a.clear()  # Clear the plot
        a.plot(timestamps, prices, label='BTC/USD Price', color='blue')
        a.set_title('Live Bitcoin Price')
        a.set_xlabel('Time')
        a.set_ylabel('Price (USD)')
        a.legend(loc='upper left')
        a.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability
        f.tight_layout()
    
class SeaofBTCapp(tk.Tk): # inheritance on tkinter's Tk
    """
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Note: typing 'args' and 'kwargs' is not necessary, you can name them differently
        # args: non-keyworded arguments
        # kwargs* keyword arguments, or usually called dictionaries

        # --- SOME OVERHEAD CONFIGS ---
        tk.Tk.iconbitmap(self,default='clienticon.ico') # change the icon
        tk.Tk.wm_title(self, "Sea of BTC Client") # change the window title

        # --- DEFINING THE MAIN CONTAINTER OF THIS APPLICATION ---
        # defined the container, which will be filled with frames to be accessed later on
        container = tk.Frame(self)
        """
        Grid allows you to create a sort of grid, which is used for orienting where things go in your application. (grid gives more control, IMO)
        Pack allows some control, but mostly feels to me like you're just stuffing things into a pillow case, just trying your best to pick a side, but it doesn't always work as intended.
        """
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1) # config settings that 
        container.grid_columnconfigure(0, weight=1)

        # We are going to pack self.frames with a bunch of possible frames, with the top frame being the current frame
        self.frames = {}

        for F in (StartPage, BTC_Page): # populate the tuple with tthe posisble pages to our application
            frame = F(container, self) # a class defining a page in the application

            self.frames[F] = frame # save the frame to the corresponding key of the dictionary
             # using grid to place the widget at coordinate (0, 0) (row, col)
            # sticky: corresponds to north, south, east, west
            # example: "ew" : stretch from left to right
            # "e": to the right
            # "nsew": fill the entire space allotted
            frame.grid(row=0, column=0, sticky="nsew")
       
        self.show_frame(StartPage) # basically here we are initializing the object which will display the start page which we define as another class
        # As we build the backend, we can add more and more pages by creating another class just like StartPage
        # Within our __init__ method, we're calling StartPage to show first, but later we can call upon show_frame to raise any other frame/window that we please

    def show_frame(self, cont):
        # cont: for controller, or the class definition 
        frame = self.frames[cont]
        frame.tkraise()

def qf(quickPrint):
    print(quickPrint)

class StartPage(tk.Frame):
    """Definition of the Main Starting page"""
    # init 
    def __init__(self, parent, controller): 
        # parameters:
        # - parent: the container
        # - controller: the app's class object itself, which includes some other functions to evoke in this page?
        tk.Frame.__init__(self,parent)
        # referencing the for F in (...) in the application's __init__()
        # NOTE
        # tk.Frame will __init__ itself ('self) and the container defined in the app's __init__() as 'parent'
        # I believe that is the right interpretation
        label = ttk.Label(self, text="ALPHA Bitcoin trading application. Use at your own risk, this is basically organized gambling online", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        """
        # TODO: we discard for now, but basically you get the idea of creating a new page for the Tk's container 
        # generate a button from tkinter
        button = ttk.Button(self, text="Click here to check for passing the variable in the command line", command= lambda:qf("Check me out, I'm passing vars!"))
        button.pack()

        # navigation to the pages (PageOne, PageTwo, etc)
        button_1 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)) # packaging the function into a lambda funtion
        button_1.pack()

        button_2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button_2.pack()

        button_3 = ttk.Button(self, text="Visit Page 3 - Visualization", command=lambda: controller.show_frame(PageThree))
        button_3.pack() 
        """

        button1 = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(BTC_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()
class PageOne(tk.Frame):
    """
    Definition of the first page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    """
    Definition of the second page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()

class BTC_Page(tk.Frame):
    """Definition of the third page to display matplotlib functions"""
    """
    def __init__(self, master = None, cnf = ..., *, background = ..., bd = 0, bg = ..., border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = ..., highlightcolor = ..., highlightthickness = 0, name = ..., padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph Visualization", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home', command=lambda:controller.show_frame(StartPage)) # navigation back to the Main StartPage
        button1.pack()

        # --- MAIN VISUALIZATION CODE BLOCK ---
        # define a figure
        # example for static data visualization
        # f = Figure(figsize=(5,5), dpi=100)
        # a = f.add_subplot(111)
        # # example data to show that we can refer from the API
        # # a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        # # anothe example - Sinewave visualization
        # t = np.arange(0.0,3.0,0.01)
        # s = np.sin(2*math.pi*t)
        # a.plot(t,s)
        # add the canvas, where to draw the graph onto
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # add the toolbar, which is the traditional matplotlib tool bar
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.ani = animation.FuncAnimation(f, VisualizeBTCprice, interval=1000)

# instantiate the object of this application - SeaofBTCapp
app = SeaofBTCapp()
# run mainloop(), a functionality of tkinter
app.mainloop()