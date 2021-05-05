1. GIT
    # Install: 
        sudo apt update
        sudo apt install git
        git --version
    # Config: 
        git config --global user.name "Your Name"
        git config --global user.email "youremail@yourdomain.com"
    # SSH Keys - Create the public and private RSA keys in your machine: 
        In case .ssh not exist: mkdir ~/.ssh
            cd ~/.ssh
            ssh-keygen -t rsa -b 4096
        Add the public SSH Key into your SSH Agent: 
            sudo ssh-add /home/<your username>/.ssh/id_rsa
        In case get message "Could not open a connection to your authentication agent.": 
            eval `ssh-agent -s`
        Copy content of public key id_rsa.pub and paste it to github
2. Java
    # Prerequisites: 
        The JRE will allow you to run almost all Java software.
        The Java Development Kit (JDK) in addition to the JRE in order to compile and run some specific Java-based software.
    # Installing the Default JRE/JDK
    # first update the package index: 
        sudo apt update
    # install the JRE/JDK from OpenJDK 11: 
        sudo apt install default-jre
        sudo apt install default-jdk
    # verify JRE/JDK: 
        java -version(Check JRE)
        javac -version(Check JDK or Java compiler)
    # Managing Java: 
        sudo update-alternatives --config java
    # Setting the JAVA_HOME Environment Variable
        Copy the path from your preferred installation then execute command
            sudo nano /etc/environment
        Then add this line
            JAVA_HOME="Path of installed JDK"
        Then reload this file to apply the changes
            source /etc/environment
        Finally verify environment variables
            echo $JAVA_HOME
    # Link: https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-18-04
3. ADB
    # Install ADB & Fastboot: 
        sudo apt update
        sudo apt-get install android-tools-adb android-tools-fastboot
    # Verify version: 
        adb version
    # Check connected devices: 
        adb devices
    # Stop and restart server:
        adb kill-server
        adb start-server
    # Link: https://computingforgeeks.com/install-adb-fastboot-on-ubuntu-mint/
4. Python
    # Update and refresh package lists: 
        sudo apt update
    # Install Python: 
        sudo apt install python2.7(For build Android Open Source Project)
        sudo apt install python3.8(For build PyQt5 app)
    # Install Python from source - extract compressed files(tgz files): 
        tar –xf Python-3.8.3.tgz
    # Store installed Python Packages version
        pip freeze > requirements.txt
    # Install Python Packages from file
        pip install -r requirements.txt
    # Link: 
        https://phoenixnap.com/kb/extract-tar-gz-files-linux-command-line
5. PyQt
    # Create a virtual environment in the current directory: 
        Windows: python3 -m venv venv
        Ubuntu: Starting from Python 3.6, the recommended way to create a virtual environment is to use the venv module
            sudo apt update
            sudo apt install python3-venv
    # Activate virtual enviroment: 
        Windows: call venv/scripts/activate.bat
        Mac/Linux: source venv/bin/activate
    # Install pip/pip3: 
        sudo apt update
        Python2: sudo apt install python-pip
        Python3: sudo apt install python3-pip
    # Install PyQt: 
        Within the virtual environment, you can use the command pip instead of pip3 and python instead of python3.
            pip3 install PyQt5==5.9.2
    # Packing and build installer: 
        pip3 install fbs PyQt5==5.9.2 PyInstaller==3.4
        Create project: fbs startproject
        Test app: fbs run
        Create a standalone executable: fbs freeze
    # Link: 
        https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/
        https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
        https://www.learnpyqt.com/tutorials/packaging-pyqt5-apps-fbs/
6. IDE
    # Visual Studio Code: 
        sudo apt install ./<file>.deb
    # Qt Designer: 
        sudo apt install qt5-default
        sudo apt install qttools5-dev-tools
        sudo apt install qttools5-dev
        Open Qt Designer: designer
    # Link: https://wiki.qt.io/Install_Qt_5_on_Ubuntu
7. Django: 
    # Create a virtual environment: 
        python3 -m venv project_name
    # Install Django web framework: 
        pip install django==3.2.1
    # Create Django project: 
        django-admin startproject project_name
    # Create a superuser: 
        - Run this cmd to apply: admin, auth, contenttypes and sessions: python manage.py migrate
        - Next: python manage.py createsuperuser
    # Create apps into Django project: 
        - Create: python manage.py startapp app_name
        - Generate SQL command: python manage.py makemigrations
        - Execute generated SQL command: python manage.py migrate
    # Upgrade Django version: 
        - pip install --upgrade django==specify_version
    # Install Django Rest Framework: 
        - pip install djangorestframework
    # Start django project: 
        - py manage.py runserver
8. Docker: 
    # Create a Dockerfile: 
    # Build Image from Dockerfile: 
        - Image has many image layers(Created by execute RUN command)
        - cmd: docker image build -t <image-name> <context>
    # Run Docker Container: 
        - docker container run -it --name <define name for image> <name of docker image>
    # Docker Client and Docker Daemon: 
    # Docker Registry: 
        - Register Docker Image
    # Check image layers: 
        - docker inspect image <image-name>
    # Remove docker image: 
        - remove by name: docker image rm -f <image-name>
        - remove by id: docker rmi -f <image-id>
    # Remove docker container by id: 
        - docker container rm -f <docker-container-id>
