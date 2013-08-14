# -*- coding: utf-8 -*-
"""
/***************************************************************************
 bBoxDialog
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
"""

from PyQt4 import QtCore, QtGui

from ui_bbox import Ui_bBox
# create the dialog for zoom to point


class bBoxDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_bBox()
        self.ui.setupUi(self)
#	self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
#	self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.close)
	self.ui.buttonBox.accepted.connect(self.accept)
	self.ui.buttonBox.rejected.connect(self.closeDialog)
    def accept(self):
	print 'kaas'

    def closeDialog(self):
	self.done(0)

#def on_buttonBox_accepted(self):


#class bBoxDialog(QtGui.QDialog, Ui_bBox):
#    def __init__(self, parent, fl):
#	QtGui.QDialog.__init__(self, parent, fl)
#	self.setupUi(self)
