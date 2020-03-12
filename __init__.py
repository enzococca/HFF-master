# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
                             -------------------
        begin                : 2007-12-01
        copyright            : (C) 2008 by Luca Mandolesi
        email                : mandoluca at gmail.com
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

import os
import re
import traceback
import subprocess
import sys
from qgis.core import QgsMessageLog, Qgis, QgsSettings

from .modules.utility.hff_OS_utility import Hff_OS_Utility
from .modules.utility.hff_folder_installation import hff_Folder_installation

sys.path.append(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'resources')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'gui', 'ui')))

hff_home = os.path.expanduser("~") + os.sep + 'HFF'
fi = hff_Folder_installation()
if not os.path.exists(hff_home):
    fi.install_dir()
else:
    os.environ['HFF_HOME'] = hff_home

confing_path = os.path.join(os.sep, hff_home, 'HFF_DB_folder', 'config.cfg')
if not os.path.isfile(confing_path):
    fi.installConfigFile(os.path.dirname(confing_path))

missing_libraries = []

try:
    import pkg_resources
    pkg_resources.require("pip")
    import pip
    
except Exception as e:
    missing_libraries.append(str(e))


try:
    import sqlalchemy
except Exception as e:
    missing_libraries.append(str(e))

try:
    import reportlab
except Exception as e:
    missing_libraries.append(str(e))

try:
    import matplotlib
except Exception as e:
    missing_libraries.append(str(e))

try:
    import sqlalchemy_utils
except Exception as e:
    missing_libraries.append(str(e))

try:
    import pandas
except Exception as e:
    missing_libraries.append(str(e))
    
try:
    import psycopg2
except Exception as e:
    missing_libraries.append(str(e))

try:
    import elasticsearch
except Exception as e:
    missing_libraries.append(str(e))    

try:
    import pysftp
except Exception as e:
    missing_libraries.append(str(e))        
    
try:
    import xlsxwriter
except Exception as e:
    missing_libraries.append(str(e))        
    
    
install_libraries = []
for l in missing_libraries:
    p = re.findall(r"'(.*?)'", l)
    install_libraries.append(p[0])

if install_libraries:
    from qgis.PyQt.QtWidgets import QMessageBox

    res = QMessageBox.warning(None, 'HFF-survey', "If you see this message it means some of the required packages are missing from your machine:\n{}\n\n"
                                                  "Do you want install the missing packages? Remember you need start QGIS like Admin".format(
        ',\n'.join(missing_libraries)), QMessageBox.Ok | QMessageBox.Cancel)
    if res == QMessageBox.Ok:
        import subprocess

        try:
            cmd = 'python3'
            subprocess.call([cmd,'{}'.format(os.path.join(os.path.dirname(__file__), 'scripts', 'modules_installer.py')),
                             ','.join(install_libraries)], shell=True if Hff_OS_Utility.isWindows() else False)
        except Exception as e:
            if Hff_OS_Utility.isMac():
                python_version = sys.version[:3]
                library_path = '/Library/Frameworks/Python.framework/Versions/{}/bin'.format(python_version)
                cmd = '{}/python3'.format(library_path)
                subprocess.call(
                    [cmd, '{}'.format(os.path.join(os.path.dirname(__file__), 'scripts', 'modules_installer.py')),
                     ','.join(install_libraries)])
            else:
                error = traceback.format_exc()
                QgsMessageLog.logMessage(error, tag="HFF-survey", level=Qgis.Critical)
    else:
        pass


                   
def classFactory(iface):
    from .hffPlugin import PyArchInitPlugin
    return PyArchInitPlugin(iface)
