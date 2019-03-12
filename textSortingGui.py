'''
Text Sorting Gui. Using WX instead of TK
'''
try:
    import wx
    import os
except:
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, "WX is a required dependency! Please install it!", "Error! PEBKAC!", 1)
#---------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "Python source (*.py)|*.py|"     \
           "Compiled Python (*.pyc)|*.pyc|" \
           "SPAM files (*.spam)|*.spam|"    \
           "Egg file (*.egg)|*.egg|"        \
           "All files (*.*)|*.*"

#---------------------------------------------------------------------------

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

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        fileMenu = wx.Menu()
        openFile = fileMenu.Append(wx.ID_OPEN)
        
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&About")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen, openFile)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        
    def OnOpen(self,event):
        self.SetStatusText("CWD: %s\n" % os.getcwd())

        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()

            self.SetStatusText('You selected %d files:' % len(paths))

            for path in paths:
                self.SetStatusText('           %s\n' % path)

        # Compare this with the debug above; did we change working dirs?
        self.SetStatusText("CWD: %s\n" % os.getcwd())

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def OnExit(self, event):
        '''Closes the frame'''
        self.Close(True)
        
    def OnAbout(self, event):
        '''Shows the about page.'''
        wx.MessageBox("Using my Text Sorting code and applying that to a GUI. Practice for saving text files, opening text files and sorting functions.",
                    "About TextSortGui", wx.OK | wx.ICON_INFORMATION) #maybe have this pull from readme.md?

        



if __name__ == "__main__":
    app = wx.App()
    frm = TextSortFrame(None, title='Text Sorting: The Gui', size=(400, 300))
    frm.Show()
    app.MainLoop()
