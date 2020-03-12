# -*- coding: utf-8 -*-
"""
/***************************************************************************
Code from QgisCloudPluginDialog
                                 A QGIS plugin
 Publish maps on qgiscloud.com
                             -------------------
        begin                : 2011-04-04
        copyright            : (C) 2011 by Sourcepole
        email                : pka@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import

import os

from qgis.PyQt.QtXml import *
from qgis.PyQt.uic import loadUiType
from qgis.gui import QgsDockWidget
# from .tabs.hff_ANC_mainapp import hff_ANC
# from .tabs.hff_ART_mainapp import hff_ART
# from .tabs.hff_UW_mainapp import hff_UW
# from .tabs.hff_Pottery_mainapp import hff_Pottery

#from .tabs.Gis_Time_controller import hff_Gis_Time_Controller
# from .tabs.Image_viewer import Main
# from .tabs.Images_directory_export import hff_Images_directory_export

# from .tabs.Pdf_export import hff_pdf_export

# from .tabs.Upd import hff_Upd_Values
#from .gui.hffConfigDialog import pyArchInitDialog_Config
#from .gui.hffInfoDialog import pyArchInitDialog_Info

MAIN_DIALOG_CLASS, _ = loadUiType(os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'gui', 'ui', 'hff_plugin.ui')))


class PyarchinitPluginDialog(QgsDockWidget, MAIN_DIALOG_CLASS):
    def __init__(self, iface):
        super(PyarchinitPluginDialog, self).__init__()
        self.setupUi(self)

        self.iface = iface
        

    
    # def runPottery(self):
        # pluginGui = hff_Pottery(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui # save   
        
    # def runUW(self):
        # pluginGui = hff_UW(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui # save       
    

    # def runART(self):
        # pluginGui = hff_ART(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui # save   

    # def runANC(self):
        # pluginGui = hff_ANC(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui # save   
        
    # def runSite(self):
        # pluginGui = hff_Site(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui  # save

    

    # def runGisTimeController(self):
        # pluginGui = hff_Gis_Time_Controller(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui  # save

    # def runUpd(self):
        # pluginGui = hff_Upd_Values(self.iface)
        # pluginGui.show()
        # self.pluginGui = pluginGui  # save

    def runConf(self):
        pluginConfGui = pyArchInitDialog_Config()
        pluginConfGui.show()
        self.pluginGui = pluginConfGui  # save

    def runInfo(self):
        pluginInfoGui = pyArchInitDialog_Info()
        pluginInfoGui.show()
        self.pluginGui = pluginInfoGui  # save

    # def runImageViewer(self):
        # pluginImageView = Main()
        # pluginImageView.show()
        # self.pluginGui = pluginImageView  # save

    # def runImages_directory_export(self):
        # pluginImage_directory_export = hff_Images_directory_export()
        # pluginImage_directory_export.show()
        # self.pluginGui = pluginImage_directory_export  # save

    

    # def runPDFadministrator(self):
        # pluginPDFadmin = hff_pdf_export(self.iface)
        # pluginPDFadmin.show()
        # self.pluginGui = pluginPDFadmin  # save
