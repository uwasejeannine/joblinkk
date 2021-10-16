from django.test import TestCase
from .models import Trainer


class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(first_name='Jemus',last_name='Mwai',age=20)
    def test_full_name_contain_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    def test_full_name_contain_last_name(self):
        self.assertIn(self. trainer.first_name,self.trainer.full_name())

# Create your tests here.
