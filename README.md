# SmartHome Project

# Installation

Before starting, be sure you installed python 3.
* Clone the project on your Raspberry Pi : `git clone https://github.com/BrokenSwing/SmartHomeProject`
* Install dependencies for `RoutineConfig` submodule : `cd SmartHomeProject/routineconfig/` then `pip install -r requirements.txt`
* Install apache and the apache WSGI module : `sudo apt-get install apache2 libapache2-mod-wsgi-py3`
* Enable WSGI module : `sudo a2enmod wsgi`

You now have to configure apache server :
* Move to apache config directory : `cd /etc/apache2/sites-available/`
* Edit or create `000-default.conf` file (sudo perms will be needed):

```
<VirtualHost *>
        ServerName smarthome.fr
        WSGIDaemonProcess start user=pi threads=5
        WSGIScriptAlias / /path/to/SmartHomeProject/start.wsgi

        <Directory /home/pi>
                WSGIProcessGroup start
                WSGIApplicationGroup %{GLOBAL}
                Require all granted
        </Directory>
</VirtualHost>
```

* Set apache to start on boot : `sudo update-rc.d apache2 defaults`
* Start/Restart apache : `sudo apachectl restart`

* Add reboot task with the command : `crontab -e` and paste `@reboot python3 /path/to/SmartHomeProject/libs/start.py`
