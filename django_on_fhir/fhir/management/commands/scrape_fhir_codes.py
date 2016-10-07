import requests

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'script to scrape JSON codes from FHIR'

    def handle(self, *args, **options):

        # command logic
        url = 'https://www.hl7.org/fhir/terminologies-valuesets.html'
        rqst = requests.get(url)
        if rqst.status_code is not 200:
            raise AssertionError('could not access the url: ' + url)
        soup = BeautifulSoup(rqst.content, "html.parser")
        code_table = soup.find('table', {'class' : 'codes'})

        # iterate through table
        data = []
        rows = code_table.find_all('tr')
        for row in rows:
            # append link only if if can find link
            if row.find('a'):
                temp_lst = [row.find('a').get('href')]

                # append description
                cols = row.find_all('td')
                cols = [x.text.strip() for x in cols]
                for col in cols:
                    temp_lst.append()
                temp_lst.append([x for x in cols if x])
                data.append(temp_lst)
        import pdb; pdb.set_trace()

        self.stdout.write(self.style.SUCCESS('Added definations of FHIR codes'))
