from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import render_to_string
from blog.models import CV
from blog.models import CV2
from django.utils import timezone
# Create your tests here.

class URLTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/homePage.html')

    def test_uses_example_cv_template(self):
        response = self.client.get('/CV')
        self.assertTemplateUsed(response, 'blog/CV_list.html')

    def test_uses_cv_builder(self):
        response = self.client.get('/CV_list')
        self.assertTemplateUsed(response, 'blog/CV2_list.html')

#tests whether the the model that i have created will save the items that
#I have given it to take and saves those items this is what i planned before
#before creating my actual CV builder. This was a test run did the same for
#CV but both the same so left CV2 rather then CV.
class ModelsTest(TestCase):

    def test_saving_items(self):
        first_item = CV2()
        first_item.author = 'Jhon makarov'
        first_item.Number = '01212343335'
        first_item.Email = 'jhon.makarov@yahoo.com'
        first_item.Date_of_birth = '09/09/1993'
        first_item.published_date = timezone.now()
        first_item.Personal_Profile = 'I am a hard working individual'
        first_item.Education = 'A levels psychology:B  Maths:A  Biology:C, GCSES 8 A*-C'
        first_item.Employement_History = 'Worked for pharmacy for a week'
        first_item.Acheivements = 'won a maths comeptiton'
        first_item.Interests = 'Like computers'
        first_item.Skills = 'Killed private miller in modern warefare 2'
        first_item.References = 'private miller KIA'
        first_item.save()

        second_item = CV2()
        second_item.author = 'Captain Price'
        second_item.Number = '0800001066'
        second_item.Email = 'price@yahoo.com'
        second_item.Date_of_birth = '10/11/1978'
        second_item.published_date = timezone.now()
        second_item.Personal_Profile = 'I am a hard working individual'
        second_item.Education = 'A levels psychology:B  Maths:A  Biology:C, GCSES 8 A*-C'
        second_item.Employement_History = 'Worked for goverment on top secret missions'
        second_item.Acheivements = 'Killed makarov and watched my friend soap die'
        second_item.Interests = 'Like guns and warzone'
        second_item.Skills = 'surviver'
        second_item.References = 'up yours'
        second_item.save()

        saved_items = CV2.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.author, 'Jhon makarov')
        self.assertEqual(second_saved_item.author, 'Captain Price')
