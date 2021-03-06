#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0 on Fri May  1 18:25:57 2020 from "/home/a0/Projects/xrr/xrr_wx2.wxg"
#

import wx
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class XRR_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: XRR_Frame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1283, 768))
        
        # Menu Bar
        self.Xframe_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Quit", "")
        self.Bind(wx.EVT_MENU, self.OnMenu_Close, id=item.GetId())
        self.Xframe_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Start", "")
        self.Bind(wx.EVT_MENU, self.OnButton_B_Fit_Start, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Stop", "")
        self.Bind(wx.EVT_MENU, self.OnButton_B_Fit_Stop, id=item.GetId())
        self.Xframe_menubar.Append(wxglade_tmp_menu, "Fit")
        self.SetMenuBar(self.Xframe_menubar)
        # Menu Bar end
        self.B_Data_Load = wx.Button(self, wx.ID_ANY, "Load Data")
        self.T_Data_FName = wx.TextCtrl(self, wx.ID_ANY, "")
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.Panel1_Data = wx.Panel(self.notebook_1_pane_1, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL)
        self.notebook_1_Profile = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.Panel2_Profile = wx.Panel(self.notebook_1_Profile, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL)
        self.B_Layer_Load = wx.Button(self, wx.ID_ANY, "Layers Load")
        self.B_Layer_Save = wx.Button(self, wx.ID_ANY, "Save")
        self.B_Layer_Insert = wx.Button(self, wx.ID_ANY, "insert")
        self.B_Layer_Delete = wx.Button(self, wx.ID_ANY, "delete")
        self.B_Layer_Update = wx.Button(self, wx.ID_ANY, "update")
        self.grid_1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.B_Fit_Start = wx.Button(self, wx.ID_ANY, "Fit Start")
        self.B_Fit_Stop = wx.Button(self, wx.ID_ANY, "Fit Stop")
        self.B_Fit_N = wx.Button(self, wx.ID_ANY, "0", style=wx.BU_RIGHT)
        self.RB_Fit_Layer = wx.RadioButton(self, wx.ID_ANY, "Layer")
        self.RB_Fit_Profile = wx.RadioButton(self, wx.ID_ANY, "Profile")
        self.Chk_L_ab = wx.CheckBox(self, wx.ID_ANY, "a0b0")
        self.Chk_L_dd = wx.CheckBox(self, wx.ID_ANY, "d")
        self.Chk_L_rh = wx.CheckBox(self, wx.ID_ANY, "rho")
        self.Chk_L_sg = wx.CheckBox(self, wx.ID_ANY, "sg")
        self.Chk_P_ab = wx.CheckBox(self, wx.ID_ANY, "a0b0")
        self.Chk_P_rh = wx.CheckBox(self, wx.ID_ANY, "rho")
        self.Chk_P_ac = wx.CheckBox(self, wx.ID_ANY, "atom")
        self.Chk_P_atom = wx.ComboBox(self, wx.ID_ANY, choices=["W", "Si", "O"], style=wx.CB_SIMPLE)
        self.notebook_2 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_2_pane_1 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.T_Logger = wx.TextCtrl(self.notebook_2_pane_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH)
        self.notebook_2_Error = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.Panel3_Error = wx.Panel(self.notebook_2_Error, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.BORDER_SUNKEN)
        self.notebook_2_Settings = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.RB_Fit_LM = wx.RadioButton(self.notebook_2_Settings, wx.ID_ANY, "L-M")
        self.RB_Fit_DE = wx.RadioButton(self.notebook_2_Settings, wx.ID_ANY, "D-E")
        self.V_Fit_Update = wx.SpinCtrl(self.notebook_2_Settings, wx.ID_ANY, "100", min=10, max=100)
        self.V_Profile_Step = wx.SpinCtrlDouble(self.notebook_2_Settings, wx.ID_ANY, "2.0", min=0.5, max=9.0)
        self.notebook_2_Help = wx.Panel(self.notebook_2, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Data_Load, self.B_Data_Load)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Layer_Load, self.B_Layer_Load)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Layer_Save, self.B_Layer_Save)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Layer_Insert, self.B_Layer_Insert)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Layer_Delete, self.B_Layer_Delete)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Layer_Update, self.B_Layer_Update)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Fit_Start, self.B_Fit_Start)
        self.Bind(wx.EVT_BUTTON, self.OnButton_B_Fit_Stop, self.B_Fit_Stop)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.OnValue_V_Fit_Update, self.V_Fit_Update)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: XRR_Frame.__set_properties
        self.SetTitle("frame")
        self.Panel1_Data.SetMinSize((600, 333))
        self.Panel2_Profile.SetMinSize((600, 333))
        self.B_Layer_Load.SetMinSize((130, 34))
        self.B_Layer_Load.SetBackgroundColour(wx.Colour(181, 175, 255))
        self.B_Layer_Save.SetBackgroundColour(wx.Colour(113, 255, 90))
        self.B_Layer_Update.SetBackgroundColour(wx.Colour(255, 249, 116))
        self.grid_1.CreateGrid(10, 7)
        self.grid_1.EnableDragRowSize(0)
        self.grid_1.EnableDragGridSize(0)
        self.grid_1.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid_1.SetColLabelValue(0, "Name")
        self.grid_1.SetColSize(0, 90)
        self.grid_1.SetColLabelValue(1, "Composition")
        self.grid_1.SetColSize(1, 150)
        self.grid_1.SetColLabelValue(2, "d [A]")
        self.grid_1.SetColSize(2, 75)
        self.grid_1.SetColLabelValue(3, "sg [A]")
        self.grid_1.SetColSize(3, 75)
        self.grid_1.SetColLabelValue(4, "[g/cm^3]")
        self.grid_1.SetColSize(4, 75)
        self.grid_1.SetColLabelValue(5, "[g/mol]")
        self.grid_1.SetColSize(5, 75)
        self.grid_1.SetColLabelValue(6, "[A^3]")
        self.grid_1.SetColSize(6, 75)
        self.B_Fit_Start.SetMinSize((130, 34))
        self.B_Fit_Start.SetBackgroundColour(wx.Colour(255, 110, 100))
        self.B_Fit_Stop.SetMinSize((130, 34))
        self.B_Fit_Stop.SetBackgroundColour(wx.Colour(255, 110, 100))
        self.B_Fit_N.SetMinSize((80, 34))
        self.B_Fit_N.Enable(False)
        self.Chk_L_ab.SetToolTip(wx.ToolTip("fit scale and background parameters"))
        self.Chk_L_ab.Enable(False)
        self.Chk_L_ab.SetValue(1)
        self.Chk_L_dd.SetToolTip(wx.ToolTip("fit layer thickness d [A]"))
        self.Chk_L_dd.SetValue(1)
        self.Chk_L_rh.SetToolTip(wx.ToolTip("fit layer density [g/cm^3]"))
        self.Chk_L_rh.SetValue(1)
        self.Chk_L_sg.SetToolTip(wx.ToolTip("fit roughness parameter sigma [A]"))
        self.Chk_L_sg.SetValue(1)
        self.Chk_P_ab.SetToolTip(wx.ToolTip("fit scale and background parameters"))
        self.Chk_P_ab.Enable(False)
        self.Chk_P_ab.SetValue(1)
        self.Chk_P_rh.SetToolTip(wx.ToolTip("fit density profile"))
        self.Chk_P_rh.Enable(False)
        self.Chk_P_rh.SetValue(1)
        self.Chk_P_ac.SetToolTip(wx.ToolTip("fit profile of atomic concentration for atom ..."))
        self.Chk_P_ac.Enable(False)
        self.Chk_P_atom.SetMinSize((80, 34))
        self.Chk_P_atom.SetSelection(0)
        self.T_Logger.SetMinSize((652, 170))
        self.Panel3_Error.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.RB_Fit_LM.SetToolTip(wx.ToolTip("LM = Levenberg-Marquand"))
        self.RB_Fit_DE.SetToolTip(wx.ToolTip("DE = Differential Evolution"))
        self.V_Fit_Update.SetMinSize((130, 34))
        self.V_Profile_Step.SetMinSize((130, 34))
        self.V_Profile_Step.SetToolTip(wx.ToolTip("profile step"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: XRR_Frame.__do_layout
        sizer_V0 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_R = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_R1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_L = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_L1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_L1.Add(self.B_Data_Load, 0, wx.ALL, 1)
        sizer_L1.Add(self.T_Data_FName, 1, wx.ALL | wx.EXPAND, 3)
        sizer_L.Add(sizer_L1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.Panel1_Data, 1, wx.ALL | wx.EXPAND, 1)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        sizer_15.Add(self.Panel2_Profile, 1, wx.ALL | wx.EXPAND, 1)
        self.notebook_1_Profile.SetSizer(sizer_15)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Reflectivity")
        self.notebook_1.AddPage(self.notebook_1_Profile, "Profile")
        sizer_L.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_V0.Add(sizer_L, 1, wx.EXPAND, 0)
        sizer_R1.Add(self.B_Layer_Load, 0, wx.ALL, 3)
        sizer_R1.Add(self.B_Layer_Save, 0, wx.ALL, 3)
        sizer_R1.Add(self.B_Layer_Insert, 0, wx.ALL, 3)
        sizer_R1.Add(self.B_Layer_Delete, 0, wx.ALL, 3)
        sizer_R1.Add(self.B_Layer_Update, 0, wx.ALL, 3)
        sizer_R.Add(sizer_R1, 0, wx.EXPAND, 0)
        sizer_R.Add(self.grid_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.B_Fit_Start, 0, wx.ALL, 3)
        sizer_4.Add(self.B_Fit_Stop, 0, wx.ALL, 3)
        sizer_7.Add(sizer_4, 0, 0, 0)
        sizer_7.Add(self.B_Fit_N, 0, wx.ALL, 3)
        sizer_10.Add(self.RB_Fit_Layer, 0, wx.ALL, 3)
        sizer_10.Add(self.RB_Fit_Profile, 0, wx.ALL, 3)
        sizer_7.Add(sizer_10, 1, wx.EXPAND, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Layer")
        sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_1.Add(self.Chk_L_ab, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_1.Add(self.Chk_L_dd, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_1.Add(self.Chk_L_rh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_1.Add(self.Chk_L_sg, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_8.Add(sizer_1, 1, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Profile")
        sizer_2.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_2.Add(self.Chk_P_ab, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_2.Add(self.Chk_P_rh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_2.Add(self.Chk_P_ac, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_2.Add(self.Chk_P_atom, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_8.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_R.Add(sizer_7, 0, wx.EXPAND, 0)
        sizer_11.Add(self.T_Logger, 1, wx.ALL | wx.EXPAND, 3)
        self.notebook_2_pane_1.SetSizer(sizer_11)
        sizer_12.Add(self.Panel3_Error, 1, wx.ALL | wx.EXPAND, 2)
        self.notebook_2_Error.SetSizer(sizer_12)
        sizer_9.Add(self.RB_Fit_LM, 0, wx.ALL, 3)
        sizer_9.Add(self.RB_Fit_DE, 0, wx.ALL, 3)
        sizer_14.Add(sizer_9, 0, wx.EXPAND, 0)
        label_3 = wx.StaticText(self.notebook_2_Settings, wx.ID_ANY, "update every")
        label_3.SetMinSize((110, 17))
        sizer_5.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 3)
        sizer_5.Add(self.V_Fit_Update, 0, wx.ALL, 3)
        sizer_14.Add(sizer_5, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.notebook_2_Settings, wx.ID_ANY, "profile step [A]")
        label_2.SetMinSize((110, 17))
        sizer_6.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 3)
        sizer_6.Add(self.V_Profile_Step, 0, wx.ALL, 3)
        sizer_14.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)
        self.notebook_2_Settings.SetSizer(sizer_13)
        self.notebook_2.AddPage(self.notebook_2_pane_1, "Logger")
        self.notebook_2.AddPage(self.notebook_2_Error, "Error")
        self.notebook_2.AddPage(self.notebook_2_Settings, "Settings")
        self.notebook_2.AddPage(self.notebook_2_Help, "Help")
        sizer_R.Add(self.notebook_2, 1, wx.EXPAND, 0)
        sizer_V0.Add(sizer_R, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_V0)
        self.Layout()
        # end wxGlade

    def OnMenu_Close(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnMenu_Close' not implemented!")
        event.Skip()

    def OnButton_B_Fit_Start(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Fit_Start' not implemented!")
        event.Skip()

    def OnButton_B_Fit_Stop(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Fit_Stop' not implemented!")
        event.Skip()

    def OnButton_B_Data_Load(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Data_Load' not implemented!")
        event.Skip()

    def OnButton_B_Layer_Load(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Layer_Load' not implemented!")
        event.Skip()

    def OnButton_B_Layer_Save(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Layer_Save' not implemented!")
        event.Skip()

    def OnButton_B_Layer_Insert(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Layer_Insert' not implemented!")
        event.Skip()

    def OnButton_B_Layer_Delete(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Layer_Delete' not implemented!")
        event.Skip()

    def OnButton_B_Layer_Update(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnButton_B_Layer_Update' not implemented!")
        event.Skip()

    def OnValue_V_Fit_Update(self, event):  # wxGlade: XRR_Frame.<event_handler>
        print("Event handler 'OnValue_V_Fit_Update' not implemented!")
        event.Skip()

# end of class XRR_Frame

class XRR_App(wx.App):
    def OnInit(self):
        self.Xframe = XRR_Frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Xframe)
        self.Xframe.Show()
        return True

# end of class XRR_App

if __name__ == "__main__":
    app = XRR_App(0)
    app.MainLoop()
