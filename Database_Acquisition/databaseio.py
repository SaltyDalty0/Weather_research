#=====================================================
# File with connection and i/o routines for
# the online weather database
#
# ver 1.0 Oct 6, 2019
# DP
#
#=====================================================

# import libraries for mysql communication
import  mysql.connector
from mysql.connector import errorcode

# import libraries for date objects
from datetime import date, datetime, timedelta

# import config file for database (local)
import databaseconfig as cfg

#=====================================================
# function to initiate a connection with a remote mySQL
# database. The connection information is in the config
# file databaseconfig.py
#
# it returns:
#     cnx: the pointer with the connection
#     cursor: the pointer to the database
#
# ver 1.0 Oct 6, 2019
#
# DP
#
#=====================================================
def databaseConnect():

    # read the parameters from the config file
    dbhost=cfg.mysqlConfig['host']
    dbadminID=cfg.mysqlConfig['admin']
    dbadminPass=cfg.mysqlConfig['adminpasswd']
    dbname=cfg.mysqlConfig['db']


    # attempt the connection
    try:
        cnx = mysql.connector.connect(user=dbadminID,
                                      password=dbadminPass,
                                      host=dbhost,
                                      database=dbname)

    # catch any errors and print appropriate message
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error with mySQL username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("mySQL Database does not exist")
        else:
            print(err)

    # initiate a cursor to the database
    cursor=cnx.cursor()

    # return the pointer and the cursor
    return cnx,cursor


#=====================================================
# function to insert a new row of data to a table
# the following data are needed
# cursor: an active cursor to the database
# table: a string with the name of the table
# datetime: a datetime object with date and time
# temperature: an int with degrees
# rel_humidity: an int with percentage of relative humidity
# wind_dir: an int with direction in degrees of wind (E of N)
# wind_speed: an int with 10*speed of wind (i.e., 5.3 -> 53)
# PWV: a single precision number with pressure of water vapor (in mm)
# tau1: optical depth at one frequency
# tau2=0: optical depth at a different frequency (0 means no measurement)
#
# it returns nothing
#
# ver 1.0 Oct 6, 2019
#
# DP
#
#=====================================================
def insertData(cursor,table,datetime,temperature,rel_humidity,wind_dir,
               wind_speed,PWV,tau1,tau2=0):

    # mySQL command to add row
    add_weather = ("INSERT INTO LMT_Weather "
                "(datetime, temperature, rel_humidity, wind_dir, wind_speed, PWV, tau1, tau2) "
                "VALUES (%(datetime)s, %(temperature)s, %(rel_humidity)s, %(wind_dir)s, %(wind_speed)s, %(PWV)s, %(tau1)s, %(tau2)s)")

    # add all the data into a single structure (with the same names :-)
    weather_data = {
        "datetime" : datetime,
        "temperature" : temperature,
        "rel_humidity": rel_humidity,
        "wind_dir" : wind_dir,
        "wind_speed" : wind_speed,
        "PWV" : PWV,
        "tau1" : tau1,
        "tau2" : tau2
        }

    cursor.execute(add_weather,weather_data)
