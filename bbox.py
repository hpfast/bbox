# -*- coding: utf-8 -*-
"""
/***************************************************************************
 bBox
                                 A QGIS plugin
 plugin for Quantum GIS which reports current bounding box and zooms to user-entered bounding box
                              -------------------
        begin                : 2013-07-26
        copyright            : (C) 2013 by Hans Fast -- Webmapper
        email                : hans@webmapper.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 
Purpose
-------

Facilitates control of map extent by making it easier to input a bounding box and read the current bounding box.
 
Usage
-----
 
You can enter the border extents into seperate fields, or enter all four coordinates as a single comma-separated text string. Both input methods update together. The diagram may be handy for interactively adjusting the bounding box, while the text field may be handy for copying and pasting from/to other applications.

You can update the values from the map window's current extent, and you can zoom the map to the current extent.

Note that because the proportions of the QGIS window may be different than the bounding box, it will not always match exactly. Future versions may allow a rectangle to be drawn on the map canvas showing the actual extent specified.
 
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from bboxdialog import bBoxDialog
import os.path


class bBox:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'bbox_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = bBoxDialog()

	#create connections to do things based on button input of dialog
	self.dlg.ui.buttonBox.rejected.connect(self.closeDialog) #connect self.closeDialog to signal buttonBox.rejected (when Close button is pressed in buttonBox)
	self.dlg.ui.updateMap.clicked.connect(self.updateMap) #connect self.updateMap to signal pushButton.clicked (when Update Map button is pressed in buttonBox)
#	self.dlg.ui.updateDialog.clicked.connect(self.updateDialog) #we don't need this button because now the dialog updates at each map extent change: connect self.updateDialog to signal pushButton.clicked (when Update from Map button is pressed in buttonBox)

	#connect the Map Canvas extentsChanged signal to our getExtent method
	self.iface.mapCanvas().extentsChanged.connect(self.updateDialog)

    # method which updates the map extent from the values entered into the dialog box input string
    def updateMap(self):
	print 'kaas'
        inputString = self.dlg.ui.inputString.text()
	print inputString
	rect = QgsRectangle()
	rect.setXMinimum(0)
	rect.setXMaximum(40000)
	rect.setYMinimum(300000)
	rect.setYMaximum(600000)
	self.iface.mapCanvas().setExtent(rect)
	self.iface.mapCanvas().refresh()
    #method which sets the contents of the input string in the dialog box
    def updateDialog(self):
	self.dlg.ui.inputString.setText(self.getExtent().toString()) #set the text of inputString to the result of getExtent()
	
    def getExtent(self):
#	print dir(self.iface.mapCanvas().extent())
#	print self
	extent = self.iface.mapCanvas().extent()
	return extent

    def closeDialog(self):
	self.dlg.done(0)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/bbox/icon.png"),
            u"bbox plugin", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&bbox", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&bbox", self.action)
        self.iface.removeToolBarIcon(self.action)
    def popup_string(self, inputString):
        #pop up an alert with the entered string
        QMessageBox.information(self.iface.mainWindow(),"About",inputString)
        
    # run method that performs all the real work
    def run(self):
       # infoString = u"This is a test"
       # QMessageBox.information(self.iface.mainWindow(),"About",infoString)
	self.updateDialog() #fill the dialog input with current extent of map
        self.dlg.show()
