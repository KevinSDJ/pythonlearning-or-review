
from time import time ,ctime

seconds_time=  time()
hours_rest= int(ctime(seconds_time).split()[3].split(':')[0])
if hours_rest<19:
    print(f'Aun quedan {19-hours_rest} horas de trabajo')
else:
    print(f'Hora de irse a casa')


