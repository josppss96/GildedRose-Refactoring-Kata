# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose



class GildedRoseTest(unittest.TestCase):
    aged_brie = "Aged Brie"
    sulfuras = "Sulfuras, Hand of Ragnaros"
    elixir = "Elixir of the Mongoose"
    conjured = "Conjured Mana Cake"
    passes = "Backstage passes to a TAFKAL80ETC concert"

    #sell in, quality
    def test_sulfuras(self):
        items = [Item("fixme", 0, 0), Item(self.aged_brie, 2, 2), Item(self.sulfuras, -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((self.sulfuras, -1, 80), (items[2].name, items[2].quality, items[2].sell_in))

    def test_aged_brie(self):
        items = [Item("fixme", 0, 0), Item(self.aged_brie, 2, 2), Item(self.sulfuras, -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((self.aged_brie, 1, 3), (items[1].name, items[1].sell_in, items[1].quality))

    def test_backstage_passes(self):
        items = [Item(self.passes, 15, 20), Item(self.aged_brie, 2, 2), Item(self.sulfuras, -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((self.passes, 14, 21), (items[0].name, items[0].sell_in, items[0].quality))

    def test_elixir(self):
        items = [Item(self.elixir, 7, 5), Item(self.aged_brie, 2, 2), Item(self.sulfuras, -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((self.elixir, 6, 4), (items[0].name, items[0].sell_in, items[0].quality))

    def test_conjure(self):
        items = [Item(self.conjured, 7, 6), Item(self.aged_brie, 2, 2), Item(self.sulfuras, -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((self.conjured, 6, 4), (items[0].name, items[0].sell_in, items[0].quality))

if __name__ == '__main__':
    unittest.main()
