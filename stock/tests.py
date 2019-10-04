from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from stock.models import Stock


class StockViewTestCase(APITestCase):
    #url_reverse = reverse('stocks:stock-list')
    url = '/stock/info/'
    url_detail = '/stock/info/{}/'


    def setUp(self):
        print('setUp')

        self.client = APIClient()
        User.objects.create_user(username='test_user', password='password123')

        self.client.login(username='test_user', password='password123')

        self.request_data = {
            'stock_name': 'fake_stock',
            'stock_price': 20
        }

        self.test_stock = Stock.objects.create(stock_name='fake_stock', stock_price=20)

    def test_restapi_stock_create(self):
        print('test_restapi_stock_create')
        self.response = self.client.post(
            self.url,
            self.request_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stock.objects.count(), 2)
        self.assertEqual(Stock.objects.get(pk=self.test_stock.id).stock_name, 'fake_stock')
        self.assertEqual(Stock.objects.get(pk=self.test_stock.id).stock_price, 20)

    def test_restapi_stock_retrieve(self):
        print('test_restapi_stock_retrieve')
        stock = Stock.objects.get(pk=self.test_stock.id)
        response = self.client.get(self.url_detail.format(self.test_stock.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('stock_name', None), stock.stock_name)
        self.assertEqual(int(response.data.get('stock_price', None)), stock.stock_price)
    
    def test_restapi_stock_partial_update(self):
        print('test_restapi_stock_partial_update')
        update_stock = {'stock_name': 'update_stock'}
        response = self.client.patch(self.url_detail.format(self.test_stock.id), update_stock, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('stock_name', None), update_stock.get('stock_name', None))

    def test_restapi_stock_update(self):
        print('test_restapi_stock_update')
        update_stock = {'stock_name': 'update_stock', 'stock_price': 100}
        response = self.client.put(self.url_detail.format(self.test_stock.id), update_stock, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('stock_name', None), update_stock.get('stock_name'))
        self.assertEqual(int(response.data.get('stock_price', None)), update_stock.get('stock_price'))

    def test_restapi_stock_delete(self):
        print('test_restapi_stock_delete')
        response = self.client.delete(self.url_detail.format(self.test_stock.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)