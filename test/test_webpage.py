from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index

        mobile_page = requests.get("http://localhost:8000/mobile.html")
        soup_mobile = BeautifulSoup(mobile_page.content, 'html.parser')
        self._mobile = soup_mobile

        accessories_page = requests.get("http://localhost:8000/accessories.html")
        soup_accessories = BeautifulSoup(accessories_page.content, 'html.parser')
        self._accessories = soup_accessories

    # testing index.html
    def test_indexpage(self):
        assert self._index.find_all('header')
        for h1 in self._index.find_all('h1'):
            if (h1.string=='Mobile Services'):
                assert 1==1
            elif (h1.string=='Deals Of The Day'):
                assert 1==1
        assert self._index.find('input', {'type': 'button'}, {'value': 'Home'})
        assert self._index.find('a', {'href': 'index.html'})
        assert self._index.find('input', {'type': 'text'}, {'placeholder': 'Search..'})
        assert self._index.find('input', {'type': 'submit'}, {'value': 'Search'})
        site= self._index.find('nav')
        a=0
        for p in self._index.find_all('a'):
            if p.contents[0]=='Mobile':
                assert p['href'] == "mobile.html"
                a=a+1;
            if p.contents[0]=='Accessories':
                assert p['href'] == "accessories.html"
                a=a+1; 
        assert a==2
        site= self._index.find('footer')
        assert site.find('p').text == 'Copyright 2019 HTML5'

        sites = self._index.find_all('div',{'class' :'product'})
        for product in sites:
            assert product.find('img')
            assert product.find('b')
            assert product.find('p')
            assert product.find('input', {'type': 'button'}, {'value': 'Buy Now'})

        assert 2 == len(self._index.find_all('div',{'class' :'row'}))
        assert 10 == len(self._index.find_all('div',{'class' :'product'}))


 #---------------------------------------------------------------------------------------------------
     
    # testing mobile.html
    def test_mobilepage(self):
        assert self._mobile.find_all('header')
        for h1 in self._mobile.find_all('h1'):
            if (h1.text=='Mobile Services'):
                assert h1.text == 'Mobile Services'
            elif (h1.test=='Mobiles'):
                assert h1.text == 'Mobiles'
        
        assert self._mobile.find('input', {'type': 'button'}, {'value': 'Home'})
        assert self._mobile.find('a', {'href': 'index.html'})
        assert self._mobile.find('input', {'type': 'text'}, {'placeholder': 'Search..'})
        assert self._mobile.find('input', {'type': 'submit'}, {'value': 'Search'})
        site= self._mobile.find('nav')
        assert site.find('a', {'class': 'active'})
        a=0
        for p in self._mobile.find_all('a'):
            if p.contents[0]=='Mobile':
                assert p['href'] == "mobile.html"
                a=a+1;
            if p.contents[0]=='Accessories':
                assert p['href'] == "accessories.html"
                a=a+1; 
        assert a==2
        site= self._mobile.find('footer')
        assert site.find('p').text == 'Copyright 2019 HTML5'
        sites = self._mobile.find_all('div',{'class' :'product'})
        for product in sites:
            assert product.find('img')
            assert product.find('b')
            assert product.find('input', {'type': 'button'}, {'value': 'Buy Now'})
            assert 2 == len(self._index.find_all('div',{'class' :'row'}))
        assert 8 == len(self._mobile.find_all('div',{'class' :'product'}))


 #---------------------------------------------------------------------------------------------------
    
    # testing accessory.html
    def test_accessorypage(self):
        assert self._accessories.find_all('header')
        for h1 in self._accessories.find_all('h1'):
            if (h1.text == 'Mobile Services'):
                assert h1.text == 'Mobile Services'
            elif (h1.text== 'Mobile Accessories'):
                assert h1.text =='Mobile Accessories'
        
        assert self._accessories.find('input', {'type': 'button'}, {'value': 'Home'})
        assert self._accessories.find('a', {'href': 'index.html'})
        assert self._accessories.find('input', {'type': 'text'}, {'placeholder': 'Search..'})
        assert self._accessories.find('input', {'type': 'submit'}, {'value': 'Search'})
        site= self._accessories.find('nav')
        assert site.find('a', {'class': 'active'})
        a=0
        for p in self._accessories.find_all('a'):
            if p.contents[0]=='Mobile':
                assert p['href'] == "mobile.html"
                a=a+1;
            if p.contents[0]=='Accessories':
                assert p['href'] == "accessories.html"
                a=a+1; 
        assert a==2
        site= self._accessories.find('footer')
        assert site.find('p').text == 'Copyright 2019 HTML5'
        assert 4 == len(self._accessories.find_all('div',{'class' :'product'}))
        assert 2 == len(self._accessories.find_all('div',{'class' :'row'}))
        sites = self._accessories.find_all('div',{'class' :'product'})
        x=0
        for product in sites:
            assert product.find('img')
            assert product.find('b')
            assert product.find('input', {'type': 'button'}, {'value': 'Buy Now'})
            site=product.find_all('b')
            for b in site:
                if(b.text == '+'):
                    x+=1
        assert x>4
