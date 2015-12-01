Mac Install PyQt

1、Install Qt：
http://www.qt.io/download-open-source/

Check the checkbox of clang_64

2、Install sip：
https://riverbankcomputing.com/software/sip/download

Unzip the file, then open Terminal, use the following Command：

python2 configure.py

make

sudo make install

3、Install PyQt：
https://riverbankcomputing.com/software/pyqt/intro

Unzip the file, then open Terminal, use the following Command:

python2 configure.py -q /Users/Ack/Qt/5.5/clang_64/bin/qmake --disable=QtPositioning

make

make install

detail of the command: 
Python2 or Python3 or others of which the version that installed on the target machine，
specify the path of qmke that installed on the machine） 
"--disable=QtPositioning"：http://stackoverflow.com/questions/33446131/pyqt5-error-during-python3-configure-py-fatal-error-qgeolocation-h-file-no/33460342#33460342

4、Verify whether installed successfully

in python Idle, input the following command, if no errors, then installed successfully

from PyQt5 import QtCore, QtGui  

