import pywhatkit
from decouple import config


phone_number = config('phone_number', default='')
group_id = config('group_id', default='')

#pywhatkit.sendwhatmsg("+940718195601", "Hello1", 00, 44, 40)

# Group
pywhatkit.sendwhatmsg_to_group("iPCbMZPbQHHBKIRE7SMp", "Automated msg", 00, 47, 35)# 