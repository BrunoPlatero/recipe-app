"""
Django command to wait fot the database to be available
"""
import time

from psycopg2 import OperationalError as Psycop2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycop2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting one second..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
