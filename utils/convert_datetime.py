import datetime as dt

date_time_str = '2019-11-04T12:12:51Z'

date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%SZ')

print(date_time_obj.timestamp())