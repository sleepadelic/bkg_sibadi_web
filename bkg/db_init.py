import bkg.models
from bkg.models import *

IssueTypes = ['Тротуары', 'Пешеходные переходы', 'Освещение', 'Автомобильные  дороги', 'Ливневая канализация',
              'Заброшенные объекты', 'Детские площадки', 'Свалки', 'Проведение капитального ремонта',
              'Доступная среда', 'Другое']

def init_types():
    for type_name in IssueTypes:
        t = bkg.models.IssueType()
        t.name=type_name
        t.save()

