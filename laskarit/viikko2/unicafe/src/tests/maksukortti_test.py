import unittest
from maksukortti import Maksukortti # type: ignore

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_rahan_talletus_OK(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_raha_lataa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_rahaa_on_tarpeeksi_nostoon(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_rahat_eivät_riitä(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_nosto_True(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))
    
    def test_nosto_False(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2000))

    def test_standardi_string(self):
        kortti = Maksukortti(1500)
        print(kortti)
        self.assertEqual(str(kortti),"Kortilla on rahaa 15.00 euroa")