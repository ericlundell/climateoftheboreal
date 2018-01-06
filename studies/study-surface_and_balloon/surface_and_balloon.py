#! /usr/bin python3

from random import randint

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from get_data import soundings
from extras import since_bc

# Read sqlite query results into a pandas DataFrame
db = "soundings-all.db"
query = '''
    select
        substr('0000' || m.year, -4) || '-' || substr('0' || m.month, -2) || '-' || substr('0' || m.day, -2) as DOY, 
        v.gph, 
        v.press/10.0 as PRESS, 
        v.TEMP/10.0 as TEMP 
    from levels v 
        join meta m on v.idfk = m.idpk 
    where v.lvltyp2 = 1  -- surface
        --and m.month = 12
        --and m.day = 25
        and m.hour = 0
    '''
df = soundings(query, db)

# Graph
#x_arr = df['GPH']
x_arr = df['TEMP']
y_arr = since_bc(list(df['DOY']))

plt.plot_date(y_arr, x_arr)
plot_name = "sounding_test_{0}.png".format(randint(0, 10000))
plt.savefig(plot_name)
print("Saved to {0}".format(plot_name))
