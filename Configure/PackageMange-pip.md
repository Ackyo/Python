Install Packages User Guide:

1. Update all the packages that installed by pip:

pip install -U distribute

pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U


2. Install lxml:

MAC OSX下pip安装lxml发生 某个.h not found问题解决办法
http://blog.marchtea.com/archives/91

在pip中如何设置一些编译变量.正确的语法是在pip之前先设置好变量,再pip install.

sudo C_INCLUDE_PATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/libxml2:/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/libxml2/libxml:/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include pip install lxml

同样的,如果需要设置libpath,也在pip之前加入C_LIB_PATH再使用pip.

进Python编辑器，import lxml测试下，看是否报错



pip introduction:

pip 是一个安装和管理 Python 包的工具，python安装包的工具有easy_install, setuptools, pip，distribute。

使用这些工具都能下载并安装django, 而pip是easy_install的替代品。在CPython解释器，pypy解释器，可以很好地工作

安装pip:
安装和升级之前，先下载get-pip.py

然后使用下面的命令：

python get-pip.py

不过注意一下，linux或osX下，需要权限，使用下面的命令，输入密码后即可。

sudo python get-pip.py 

windows下需要管理员权限启动终端。

如果你还没有安装了setuptools，get-pip.py 会帮你安装。

如果你已经安装了setuptools，运行下面的命令进行升级。

pip install -U setuptools

windows下，注意将pip路劲加到系统的path中

升级pip

Linux or OS X系统，运行下面的命令:

pip install -U pip

windows系统运行下面的命令：

python -m pip install -U pip

安装包
使用下面的命令来安装包

pip install SomePackage# latest versionpip install SomePackage==1.0.4 # specific versionpip install 'SomePackage>=1.0.4' # minimum version

要看更多地例子，可以看这里pip install

例如我要安装Django，用下面的一条命令即可，方便快捷。

pip install Django==1.7

http://www.ttlsa.com/python/how-to-install-and-use-pip-ttlsa/





