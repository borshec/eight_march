import random
import datetime
import pdb

from settings import *

days_of_week = {1:'ПН', 2:'ВТ', 3:'СР', 4:'ЧТ', 5:'ПТ', 6:'СБ', 7:'ВС'}

qty_staff_m = len(staff_m) + 1 
qty_staff_w = len(staff_w)
date_of_8_march = datetime.datetime(datetime.datetime.now().year,3,8)
day_of_week_8_march = date_of_8_march.isoweekday()
if (day_of_week_8_march == 1) or (day_of_week_8_march == 6) or (day_of_week_8_march == 7):
    day_of_compliment = 5
else:
    day_of_compliment = day_of_week_8_march - 1
date_of_compliment = date_of_8_march - datetime.timedelta(abs(day_of_week_8_march - day_of_compliment))
payment = int(qty_staff_w*budget_per_w_person/qty_staff_m)
     
print('\nВ этом году 8 марта это ', days_of_week[day_of_week_8_march], '. Поздравлять надо в(во) ', days_of_week[day_of_compliment], ' (',date_of_compliment.strftime('%d.%m.%Y'), ')\n', sep='')
print('Всего женщин в этом году - ', qty_staff_w, sep='')
print('Всего мужчин в этом году - ', qty_staff_w, '\n', sep='')
print('Бюджет на одну даму установлен равным ', budget_per_w_person, ' руб. Каждый участник поздравления должен будет сдать ', payment , ' руб.\n', sep='')
#pdb.set_trace()

print('Распределение людей по подготовительным задачам следующее: \n')
random.seed()
for task in tasks:
    random_number = random.randint(0, len(staff_m)-1)
    print(task, ' - ', staff_m[random_number], sep='')
    staff_m.remove(staff_m[random_number])
print('Готовиться к произнесению речи - ', boss, sep='')
    
