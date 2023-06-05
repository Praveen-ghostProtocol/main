#CSV programs

import csv

fp = open('students.csv','w',newline='')

bot = csv.writer(fp)

bot.writerow([1001,'Y SUHAS',12,'Computer Science with Python','ys.suhas29@gmail.com'])
bot.writerow([1002, 'Aaron Abraham', 12, 'Computer Science with Python', '5aaron7abraham@gmail.com'])
bot.writerow([1003, 'Archit Rishabh', 12,  'Computer Science with Python', 'a.rishabh2011@gmail.com'])
bot.writerow([1004, 'Prardhna Prathap', 12, 'Computer Science with Python', 'prardhna.prathap@outlook.com'])
bot.writerow([1005, 'Pavan Sankar', 12, 'Computer Science with Python', 'pavansankar2u@gmail.com'])
bot.writerow([1006, 'Aditya Menon', 12, 'Computer Science with Python', '214adi10@gmail.com'])
bot.writerow([1007, 'Praveen Kumar S', 12, 'Computer Science with Python', 's4spraveen.2005@gmail.com'])

fp.close()