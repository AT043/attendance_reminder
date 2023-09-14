import datetime as dt
import holidays


#def wkt_absen:

id_holidays = holidays.ID()

x = dt.datetime.now()

print(x.year)
print(x.strftime("%A-%y-%m %H %M %S"))
check_date = x.strftime("%y %m %d")

print(id_holidays.get(check_date))

def test():
    if x.strftime("%A") == 'Thursday':
        print('YAY')
    else:
        return

test()
    
        
