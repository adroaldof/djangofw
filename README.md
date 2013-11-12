#Django Framework

This is a practical example to show how to work with Django Framework.

The present tutorial assumes that you are familiar with command line tools and Git, some modules are used here just run this project, with no intention to show what it does and how it works.


##Enviroment Setup
---
###Mac OS X 10.7 or latter

1. Check if you have `Easy Install` on your machine

        easy_install --version

2. If you get an answer that looks like line bellow you can go to step #4

        setuptools 0.9.8

3. If you didn't get above answer you need to install `Setup Tools`

        curl -O "http://python-distribute.org/distribute_setup.py"
        sudo python distribute_setup.py
        sudo rm distribute_setup.py

4. Now you are ready to install `PIP`

        sudo easy_install pip

5. [Install Git for Mac OS X](https://help.github.com/articles/set-up-git#platform-mac "GitHub for Mac")

6. Check if you have a `Homebrew` on your machine

        brew --version

7. If you get an answer that looks like line bellow you can go to step #9

        0.9.5

8. Install `Homebrew` [Homebrew](http://mxcl.github.com/homebrew/) install

9. Once you've got `Homebrew` you can install `gettext`:

        brew update
        brew install gettext
        brew link gettext


---
###Ubuntu 12.04 or newer
1. Become root user

        sudo su

2. Update package list

        apt-get update

3. Install needed packages

        apt-get install build-essential python2.7-dev gettext

4. Install Python pip

        sudo apt-get install python-pip

5. Install git

        apt-get install git

6. Leave root

        exit


---

---
###Virtual Env and Fetching GitHub Repo

1. Install `Virtual Env` and `Virtual Env Wrapper`

        sudo pip install virtualenv virtualenvwrapper

2. Add the follow lines to the end of your `.bash_profile` or `.profile` file

        # set where virutal environments will live
        export WORKON_HOME=$HOME/.virtualenvs
        # ensure all new environments are isolated from the site-packages directory
        export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
        # use the same directory for virtualenvs as virtualenvwrapper
        export PIP_VIRTUALENV_BASE=$WORKON_HOME
        # makes pip detect an active virtualenv and install to it
        export PIP_RESPECT_VIRTUALENV=true
        if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then
            source /usr/local/bin/virtualenvwrapper.sh
        else
            echo "WARNING: Can't find virtualenvwrapper.sh"
        fi

3. Create a virtual enviroment project

        # You can give the same project name or any name you want
        # This command will create and activate a new virtualenv
        # You can note a `(djangofw)` in front of your command line header
        # (djangofw)user@machine$
        mkvirtualenv djangofw

        # To activate another time
        workon djangofw

        # To deactivate when you end working
        deactivate

4. Chose a place to checkout your local repo and access it

        # Sugestion is to create a folder called 'workspace' but you can chose whatever folder you want
        mkdir ~/workspace
        cd ~/workspace

5. Clone `djangofw` repo

        # Make sure you have a GitHub account with correct ssh key configurated
        git clone git@github.com:adroaldof/djangofw.git

6. Access you project folder

        cd djangofw

7. Activate your virtual env

        workon djangofw

8. Install needed requirements modules

        pip install -r requirements.txt

9. Make a database synchronization

        python manage.py syncdb

10. Compile translation files

        python manage.py compilemessages -a

---
###And you are good to go

1. Run python server

        python manage.py runserver

2. Go to

    [http://127.0.0.1:8000](http://127.0.0.1:8000 "localhost")

---

Enjoy it