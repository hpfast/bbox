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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "bbox"


def description():
    return "plugin for Quantum GIS which reports current bounding box and zooms to user-entered bounding box"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Hans Fast -- Webmapper"

def email():
    return "hans@webmapper.net"

def classFactory(iface):
    # load bBox class from file bBox
    from bbox import bBox
    return bBox(iface)
