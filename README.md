#Django Framework

This is a practical example to show how to work with Django Framework.

The present tutorial assumes that you are familiar with command line tools and Git, some modules are used here just run this project with no intention to show what it does and how it works.

##Enviroment Setup
---
###Mac OS X

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

5. Install `Virtual Env` and `Virtual Env Wrapper`

        sudo pip install virtualenv virtualenvwrapper

6. Add the follow lines to the end of your `.bash_profile` or `.profile` file

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

7. Create a virtual enviroment project

        # You can give the same project name or any name you want
        # This command will create and activate a new virtualenv
        mkvirtualenv djangofw

        # To activate
        # It will add a `(djangofw)` in front of your command line header
        # (djangofw)user@machine$
        workon djangofw
        
        # To deactivate
        deactivate

---

---
###Fetching GitHub Repo

1. Chose a place to checkout your local repo
2. Clone `djangofw` repo

        git clone git@github.com:adroaldof/djangofw.git

3. Access you project folder

        cd djangofw

4. Activate your virtual env

        workon djangofw

5. Install needed requirements modules

        pip install -r requirements.txt

6. Make a database synchronization

        python manage.py syncdb

---
###And you are good to go

1. Run python server

        python manage.py runserver

2. Go to

    [http://127.0.0.1:8000](http://127.0.0.1:8000 "localhost")

---

Enjoy it