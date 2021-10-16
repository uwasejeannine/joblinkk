from django.test import TestCase
from .models import Event


class CalencderModelTestCase(TestCase):
    def setUp(self):
        self.calendary=Event(event_name='JavaScrip',event_task='Callbacks')
    def test_events_contain_event_name(self):
        self.assertIn(self.event.event_name,self.javaScrip.event())
    def test_event_contain_last_task(self):
        self.assertIn(self. event.event_name,self.event.events())


# Create your tests here.
