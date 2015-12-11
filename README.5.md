part of rmjd_base module

==========================================
software base - linux / fedora 23
==========================================

instalar python (3.5) [default del package mgr - dnf]
	# desinstalar otras versiones de python
	dnf remove python3



	# requiere openssl
	sudo dnf install openssl-devel 
	sudo dnf install openssl
	sudo dnf install libffi-devel
	sudo dnf install gmp-devel
	sudo dnf install redhat-rpm-config

	# # python (por defecto/gestor de paquetes: no funcionan algunas librerias)
	# sudo dnf install python3
	# s udo dnf install python3-pip
	# sudo dnf install python3-devel
	#


	# descargarlo e instalarlo en /.work/Python35 o
	cd /.tools
	wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
	cp /.tools/Python-3.5.1.* /.work/
	cd /.work
	tar -xvf Python-3.5.1.tar.xz
	rm Python-3.5.1.tar.xz
	mv Python-3.5.1 Python-3.5.1-src
	cd Python-3.5.1-src
	./configure --prefix=/.work/Python35
	sudo make
	sudo make install
	#
	## editar entorno
	sudo vi /etc/profile 
	#
	## adicionar
	export PYTHONPATH=/.work/Python35
	export PYTHON_HOME=/.work/Python35
	export PATH=/.work/Python-3.5/bin::$PATH
	#
	## ejecutar script
	source /etc/profile
	# ejecutar el siguiente comando; si no se puede, eliminar los link simbolicos existentes con unlink

	sudo ln -s /.work/Python35/bin/python3.5 /usr/bin/python
	sudo ln -s /.work/Python35/bin/pip3 /usr/bin/pip


instalar/actualizar pip
	sudo pip install --upgrade pip
	# python instala un pip en el sistema; 
	# si hay multiples se debe crear un link simbolico para que use esta version

instalar pycrypto (http://www.pycrypto.org/)
	sudo pip install pycrypto

	# wget https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.1.tar.gz
	# tar -xvf pycrypto-2.6.1.tar.gz
	# cd pycrypto-2.6.1
	# ./configure
	# sudo python ./setup.py build
	# sudo python ./setup.py install



instalar/actualizar virtualenv
	sudo pip install --upgrade virtualenv
crear virtualenv
	mkdir -p /.work/virtualenv
	cd /.work/virtualenv
	virtualenv dj19
activar virtualenv
	chmod +x  /.work/virtualenv/dj19/bin/activate
	. /.work/virtualenv/dj19/bin/activate
instalar django
	pip install django

==========================================
software base - windows
==========================================
instalar python (3.5) C:\.work\Python35
instalar pycrypto
	ver referencia : http://codeyarns.com/2012/04/28/python-version-not-found-in-registry-error/

	exportar de HKEY_LOCAL_MACHINE\SOFTWARE\Python (python_install_35.reg)
	editar el archivo y reemplazar HKEY_LOCAL_MACHINE por HKEY_CURRENT_USER

	ejecutar una consola como admin y dando
	regedit python_install_35.reg
	adicionar las entradas
	luego ver con regedit y cambiar HKEY_CURRENT_USER\SOFTWARE\Python\PythonCore\3.5 por 3.3
	ejecutar de nuevo el instalador 

instalar virtualenv
	pip install virtualenv
crear virtualenv
	cd c:\.work\virtualenv\
	virtualenv dj19
instalar django
	c:\.work\virtualenv\dj19\Scripts\activate
	pip install django

==========================================
oauth-2 + openidconnect-1.0 python/django
==========================================

scaffold del proyecto (solo la primera vez)

	cd C:\.apps\e.dj\rmjd_base
	django-admin startproject _app
	cd _app
	python manage.py startapp m_auth
	cd ..
	mv _app rmjd
	cd rmjd
	python manage.py runserver

descargar dependencias
 	cd /.apps/rmjd_base
 	# descargar conector - base
 	git clone https://github.com/rohe/pyoidc.git
 	cd pyoidc
 	python setup.py install

 	# descargar conector - librerias de apoyo
 	cd /.apps/rmjd_base
	git clone https://github.com/ahurtado-dj/pyjwkest.git 
	cd pyjwkest
	python setup.py install

 	# descargar src del proyecto y dependencias
 	
 	pip install -r requirements.txt


subir proyecto
	python manage.py migrate
	python manage.py runserver



======================================
REFERENCIAS
======================================

- implemnetacion cliente python: https://github.com/rohe/pyoidc
- impleemtnacin client django: https://pypi.python.org/pypi/django-oidc-provider
- ejemplo oauth2openidconnect: https://oauthssodemo.appspot.com/step/2

======================================
ANEXO 1: INSTALAR PYCRYPTO WINDOWS
======================================

