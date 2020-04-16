import configparser
import json

# Read config.ini
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

# list型の値を取得する場合
ALLOWED_HOSTS = json.loads(config_ini.get("ip_address", "allowed_hosts"))
print(ALLOWED_HOSTS)

# 文字列型の値を取得する場合
DEBUG = config_ini["debug"]["mode"]
print(DEBUG)
