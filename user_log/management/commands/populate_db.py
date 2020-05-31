from django.core.management.base import BaseCommand,CommandError
from django.utils.crypto import get_random_string
from user_log.models import users,active_period
from datetime import datetime,timedelta
import random
import pytz

class Command(BaseCommand):

    def _create_users_active_period(self):
        first_names=('John','Andy','Joe','Peter')
        last_names=('Johnson','Smith','Williams','Parker')
 
        for iter in range(10):
            #--------------------------------------------------------------------------------
            #creating new users
            real_name = random.choice(first_names)+" "+random.choice(last_names)
            randZoneName = random.choice(pytz.all_timezones)
            user_id = get_random_string(8).lower()
            _user = users(real_name=real_name,user_id=user_id,tz=randZoneName)
            _user.save()
            #----------------------------------------------------------------------------------
            #creating active period for new users
        
            time_zone = pytz.timezone(randZoneName)
            start_time = datetime.now(time_zone)
            hours = 3
            hours_added = timedelta(hours = hours)
            end_time = start_time + hours_added
            
            _user_active_period = active_period(user_id=user_id,start_time=start_time,end_time=end_time)
            _user_active_period.save()

    def handle(self, *args, **options):
        self._create_users_active_period()
