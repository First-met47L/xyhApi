import unittest
from ApiClass.ParamObj import BaseParamObj
from ApiClass.Field import *
from ApiException import ApiException


class SearchCondition(BaseParamObj):
    id = IntegerField()
    brand = StringField()
    gender = StringField()
    category = StringField()
    price = FloatField()
    tags = ListField()


class ParamUnitTest(unittest.TestCase):
    def test_init(self):
        condition = SearchCondition(id=1, brand="me", gender="first", category="et", price=float(30),
                                    tags=['1', '2', '3'])
        # self.assertEqual(condition.id, 1)
        self.assertEqual(condition['id'], 1)
        self.assertEqual(condition['brand'], 'me')
        self.assertEqual(condition['category'], 'et')
        self.assertEqual(condition['price'], 30)
        self.assertEqual(condition['tags'], ['1', '2', '3'])
        self.assertTrue(isinstance(condition, dict))

        with self.assertRaises(ApiException.ParamTypeException):
            SearchCondition(id='1')

    def test_key(self):
        condition = SearchCondition()
        condition['id'] = 1
        self.assertEqual(condition.id, 1)

    def test_attr(self):
        condition = SearchCondition()
        condition.id = 1
        self.assertTrue('id' in condition)
        self.assertEqual(condition.id, 1)



    def test_keyError(self):
        condition = SearchCondition()
        with self.assertRaises(KeyError):
            value = condition['id']


    def test_attrError(self):
        condition = SearchCondition()
        with self.assertRaises(AttributeError):
            value = condition.id

    def test_setKeyParamTypeException(self):
        condition = SearchCondition()
        with self.assertRaises(ApiException.ParamTypeException):
            condition['id'] = 'str'


    def test_setAttrParamTypeException(self):
        condition = SearchCondition()
        with self.assertRaises(ApiException.ParamTypeException):
            condition.id = 'str'



if __name__ == '__main__':
    unittest.main()
