# Etape de déploiement
##### Le projet consiste à déployer une application Flask avec Apache et WSGI
#### Création d'une VM sur Azure
Paramètres notables :
> Région : East US (ça coûte beaucoup moins cher)

> Bien sélectionner les ports d'entrée : 22, 80, 443

> Une fois la machine virtuell, on peut également créer un nom DNS

#### Mise en place de l'environnement

On se position dans root pour éviter les sudo :
> sudo su (puis le mdp)

On va créer une clé ssh pour le projet github :
> ssh-keygen -t rsa -b 4096
> exec ssh-agent bash
> ssh-add ~/.ssh/id_rsa

On va installer les outils dont on va avoir besoin :
- Installation d'Apache2:
    > apt-get update
    > apt-get upgrade
    > apt-get install apache2
- Installation de wsgi:
    > apt-get install libapache2-mod-wsgi-py3
    > a2enmod wsgi
- Installation de python et ses bibliothèques:
    > apt-get install python3.8
    > apt-get install python3-pip
    > pip3 install virtualenv
    > pip3 install Flask
- Installation de Redis :
    > apt install lsb-release
    > apt install curl
    > curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
    > sudo apt-get install redis
- Création d'un environment virtuel : 
    > virtualenv venv
    > source venv/bin/activate

On va créer notre application Flask :
> On clone notre repo github dans le répertoire : "/var/www/"

    L'arborescence de notre repo :
    repo
    |   app
    |   |   template
    |   |   |   index.html
    |   |   |
    |   |    __init__.py (ou app.py)
    |   |
    |   app.wsgi
    |   requirements.txt

On va créer le ficher de config de notre app :
Dans le répertoire : "/etc/apache2/sites-available/app.conf"

> <VirtualHost *:80>
  ServerName mechanosqlcheaper.eastus.cloudapp.azure.com
  WSGIScriptAlias / /var/www/repo/app.wsgi
  <Directory /var/www/repo/app/>
    Order allow,deny
    Allow from all
  </Directory>
  Alias /templates /var/www/repo/app/templates
   <Directory /var/www/repo/app/templates/>
    Order allow,deny
    Allow from all
  </Directory>
  ErrorLog \${APACHE_LOG_DIR}/error.log
  LogLevel warn
  CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

Dans le répertoire : "/var/www/repo/app.wsgi"
> #!/usr/bin/python
> import sys
> import logging
> logging.basicConfig(stream=sys.stderr)
> sys.path.insert(0,"/var/www/repo/")
>
> from app import app as application

On ajoute notre application à Apache2:
> a2ensite FlaskApp

On peut maintenant lancer notre serveur Apache2:
> service apache2 restart

# Comment se servir de l'application

#### But
Jeu de hasard où l'on doit parier sur une carte un nombre de jetons.

100 jetons sont offerts dès le début, mais il est également possible d'en acheter gratuitement en cliquant sur les jetons en haut à droite.


