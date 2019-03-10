'''
Text Sorting Gui. Using WX instead of TK
'''
try:
    import wx
except:
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, "WX is a required dependancy! Please install it!", "Error! PEBKAC!", 1)

class TextSortFrame(wx.Frame):
    '''
    a class frame that will display the unsorted text and allow you to sort it
    '''
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(TextSortFrame, self).__init__(*args, **kw)
        # create a panel in the frame
        pnl = wx.Panel(self)
        # create a menu bar
        self.makeMenuBar()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Everything is fine")

    def makeMenuBar():
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        fileMenu = wx.Menu()
        openFile = fileMenu.Append(-1,"&Open\tCtrl-O","Open a File")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")