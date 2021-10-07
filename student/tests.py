from django.test import TestCase
from .models import Student


class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name='Jeannine',last_name='Uwase',age=20)
    def test_full_name_contain_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    def test_full_name_contain_last_name(self):
        self.assertIn(self. student.first_name,self.student.full_name())

    # def test_year_of_Birth(self):
    #     year = datetime.datetime.now().year-self.student.age
    #     self.assertIn(year,self.student.year_of_birth())

    # def test_student_registation_view(student):
    #     data={"first_name":self.first_name,"last_name":self.student.last_name}
    #     url=revers("register_student")
    #     response=self.client.post(url,data)
    #     self.assertEquel(response.status-code,200)

# Create your tests here.
