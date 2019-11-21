from django.test import TestCase
from .models import User,Profile,Comment

# # Create your tests here.
# class UserTestClass(TestCase):
    
#   # Set up method
#     def setUp(self):
#         self.logue= User(first_name='Flacko', last_name ='Hearts', email ='logue54@gmail.com')
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.logue,User))
#        # Testing Save Method
#     def test_save_method(self):
#         self.logue.save_user()
#         users = User.objects.all()
#         self.assertTrue(len(users) > 0)
        
class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_two = Profile(profile_image='images/mine.jpg',bio='i love anime',user_id=3)
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_two,Profile)) 

    def test_save_method(self):
        
        self.profile_two.save_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile_two.save_user_profile()
        self.profile_two.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) is 0)

    def tearDown(self):
        Profile.objects.all().delete()
    