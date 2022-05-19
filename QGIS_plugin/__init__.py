# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GMQ710Analyser
                                 A QGIS plugin
 GMQ710Analyser
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-07
        copyright            : (C) 2020 by Yves Voirin
        email                : yves.voirin@usherbrooke.ca
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GMQ710Analyser class from file GMQ710Analyser.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .GMQ710Analyser import GMQ710Analyser
    return GMQ710Analyser(iface)
