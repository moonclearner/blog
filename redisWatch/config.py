#coding: utf-8
# the format of every redis_server in  REDIS_SERVER should like this: "myip:redisport" or "anotherip:redisport:mypassword"
REDIS_SERVER = ["127.0.0.1:6379", "172.17.0.1:6379"]
#  ['ip:port:pawword', 'ip:port', .....]
# interval which you monitor the redis info.
INFO_INTERVAL = 2.0
# in the index, the table is set to show 10 rows redis data by default. you can change it.
TABLE_MAX_ROWS = 10
# flaks debug mode
DEBUG = False
SECRET_KEY = 'moonclearner_secret_key'

