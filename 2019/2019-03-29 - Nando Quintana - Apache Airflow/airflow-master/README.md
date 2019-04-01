# Demo de Apache Airflow para ExtrePython

## postgresql

```
ssh root@68.183.221.130
service postgresql start
```

## redis

```
ssh root@68.183.221.130
service redis-server start
```


## webserver

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
airflow webserver
```

[http://68.183.221.130:8080](http://68.183.221.130:8080)


## flower

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
airflow flower
```

[http://68.183.221.130:5555](http://68.183.221.130:5555)


## scheduler

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
airflow scheduler
```


## pgAdmin

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
python3 /usr/local/lib/python3.6/dist-packages/pgadmin4/pgAdmin4.py
```

[http://68.183.221.130:5050](http://68.183.221.130:5050)


# Credenciales

## ubuntu

user: root
pass: extrepython

## postgresql

user:airflow
pass: extrepython

## webserver

user: airflow
pass: extrepython


# Instalación en ubuntu


```
ssh root@68.183.221.130
apt-get update
apt-get install emacs

adduser airflow
emacs /etc/sudoers

apt-get install postgresql postgresql-contrib
emacs /etc/postgresql/10/main/pg_hba.conf
service postgresql restart
sudo -u postgres createuser -P --interactive
sudo -u airflow createdb airflow

apt-get install redis-server
apt-get install emacs
emacs /etc/redis/redis.conf
service redis-server restart
redis-cli -u redis://h:extrepython@localhost:6379

su airflow

wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.3/pip/pgadmin4-4.3-py2.py3-none-any.whl
pip3 install pgadmin4-4.3-py2.py3-none-any.whl
emacs /usr/local/lib/python3.6/dist-packages/pgadmin4/config_local.py
python3 /usr/local/lib/python3.6/dist-packages/pgadmin4/pgAdmin4.py

apt-get install python3-distutils
apt-get install python3-pip

pip3 install -U "celery[redis]"

export AIRFLOW_GPL_UNIDECODE=yes
apt-get install libmysqlclient-dev
pip3 install apache-airflow[crypto,celery,postgres,hive,jdbc,mysql,ssh]


```

## Crear un usuario para el webserver

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
airflow create_user -r Admin -u airflow -e my@email.com -f Admin -l User -p extrepython
```

## Instalar DAGs demos

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
git clone https://github.com/nandoquintana/airflow.git github_nandoquintana_airflow
ln -s github_nandoquintana_airflow/dags
```

## links sobre la instalación

https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-16-04-es
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04

https://pip.pypa.io/en/stable/installing/
http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html

https://bcb.github.io/airflow/fernet-key

https://linuxhint.com/install-pgadmin4-ubuntu/


# Notas

https://airflow.apache.org/code.html#macros

## Cómo borrar un DAG de la base de datos de metadatos

```
delete from xcom where dag_id = 'hola_mundo';
delete from task_instance where dag_id = 'hola_mundo';
delete from task_fail where dag_id = 'hola_mundo';
delete from sla_miss where dag_id = 'hola_mundo';
delete from log where dag_id = 'hola_mundo';
delete from job where dag_id = 'hola_mundo';
delete from dag_stats where dag_id = 'hola_mundo';
delete from dag_run where dag_id = 'hola_mundo';
delete from dag where dag_id = 'hola_mundo';
```
## Cómo actualizar el DagBag del webserver sin reiniciarlo

```
ssh root@68.183.221.130
su airflow
cd /home/airflow
python3 -c "from airflow.models import DagBag; d = DagBag();"
```
