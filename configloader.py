#!/usr/bin/python
# -*- coding: UTF-8 -*-
import importloader
import json

g_config = None


def load():
    with open('data.json', 'r') as f:
        data = json.load(f)
        return data


def load_config():
    global g_config
    g_config = importloader.loads(['userapiconfig', 'apiconfig'])
    load4json()



def load4json():
    with open('userconfig.json', 'r') as f:
        data = json.load(f)
        g_config.NODE_ID = data["NODE_ID"]
        g_config.SPEEDTEST = data["SPEEDTEST"]
        g_config.CLOUDSAFE = data["CLOUDSAFE"]
        g_config.ANTISSATTACK = data["ANTISSATTACK"]
        g_config.AUTOEXEC = data["AUTOEXEC"]
        g_config.MU_SUFFIX = data["MU_SUFFIX"]
        g_config.MU_REGEX = data["MU_REGEX"]
        g_config.SERVER_PUB_ADDR = data["SERVER_PUB_ADDR"]
        g_config.API_INTERFACE = data["API_INTERFACE"]
        g_config.WEBAPI_URL = data["WEBAPI_URL"]
        g_config.WEBAPI_TOKEN = data["WEBAPI_TOKEN"]
        g_config.MUDB_FILE = data["MUDB_FILE"]
        g_config.MYSQL_HOST = data["MYSQL_HOST"]
        g_config.MYSQL_PORT = data["MYSQL_PORT"]
        g_config.MYSQL_USER = data["MYSQL_USER"]
        g_config.MYSQL_PASS = data["MYSQL_PASS"]
        g_config.MYSQL_DB = data["MYSQL_DB"]
        g_config.MYSQL_SSL_ENABLE = data["MYSQL_SSL_ENABLE"]
        g_config.MYSQL_SSL_CA = data["MYSQL_SSL_CA"]
        g_config.MYSQL_SSL_CERT = data["MYSQL_SSL_CERT"]
        g_config.MYSQL_SSL_KEY = data["MYSQL_SSL_KEY"]
        g_config.API_HOST = data["API_HOST"]
        g_config.API_PORT = data["API_PORT"]
        g_config.API_PATH = data["API_PATH"]
        g_config.API_TOKEN = data["API_TOKEN"]
        g_config.API_UPDATE_TIME = data["API_UPDATE_TIME"]
        g_config.MANAGE_BIND_IP = data["MANAGE_BIND_IP"]
        g_config.MANAGE_PORT = data["MANAGE_PORT"]
        g_config.IP_MD5_SALT = data["IP_MD5_SALT"]
        return data


def get_config():
    return g_config


load_config()
