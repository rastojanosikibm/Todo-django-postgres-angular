from django.core.management.base import BaseCommand
from django.conf import settings
import psycopg2

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('create database ' + settings.DATABASES['default']['NAME'] + ';')
        conn = psycopg2.connect(host=settings.DATABASES['default']['HOST']
                                , user=settings.DATABASES['default']['USER']
                                , password=settings.DATABASES['default']['PASSWORD'])
        conn.autocommit = True
        c = conn.cursor()
        c.execute('create database ' + settings.DATABASES['default']['NAME'] + ';')
        c.close()