import unittest
from studinfo import studinfo

class Teststudinfo(unittest.TestCase):

   def test_fullname(self):

      stud_1 = studinfo('pratik','santhosh',230601)
      stud_2 = studinfo('adarshh', 'nm', 120500)

      self.assertEqual(stud_1.fullname,'pratik santhosh')
      self.assertEqual(stud_2.fullname,'adarshh nm')

      stud_1.first ='sam'
      stud_2.first ='john'

      self.assertEqual(stud_1.fullname, 'sam santhosh')
      self.assertEqual(stud_2.fullname, 'john nm')

   def test_email(self):
       stud_1 = studinfo('pratik', 'santhosh', 230601)
       stud_2 = studinfo('adarshh', 'nm', 120500)

       self.assertEqual(stud_1.email, 'pratik.santhosh@btech.christuniverity.in')
       self.assertEqual(stud_2.email, 'adarshh.nm@btech.christuniverity.in')


       stud_1.first = 'sam'
       stud_2.first = 'john'

   def test_regist_num(self):
       stud_1 = studinfo('pratik', 'santhosh', 230601)
       stud_2 = studinfo('adarshh', 'nm', 120500)

       stud_1.regist_num()
       stud_2.regist_num()


       self.assertEqual(stud_1.regno, 2306019)
       self.assertEqual(stud_2.regno, 1205000)











