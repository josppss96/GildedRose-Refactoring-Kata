# -*- coding: utf-8 -*-
import unittest
from abc import ABC

class GildedRose(object):
    aged_brie = "Aged Brie"
    sulfuras = "Sulfuras, Hand of Ragnaros"
    conjured = "Conjured Mana Cake"
    passes = "Backstage passes to a TAFKAL80ETC concert"


    def __init__(self, items):
        self.items = items

    def parseItems(self, item):
        if item == self.sulfuras:
            sulfuras_item = Sulfuras(item)
            return sulfuras_item
        if item[0] == self.aged_brie:
            aged_brie_item = Aged_Brie(item[0],item[1], item[2])
            return aged_brie_item
        if item[0] == self.conjured:
            conjured_item = Conjured(item[0], item[1], item[2])
            return conjured_item
        if item[0] == self.passes:
            passes_item = Backstage_Passes(item[0], item[1], item[2])
            return passes_item
        else:
            general_item = General_Item(item[0], item[1], item[2])
            return general_item

    def new_day(self, item):
        if hasattr(item, "adjustSellIn"):
            item.adjustSellIn()
        if hasattr(item, "adjustQuality"):
            item.adjustQuality()

    def new_day_list(self):
        updated_items = []
        for item in self.items:
            item = self.parseItems(item)
            self.new_day(item)
            updated_items.append(item)
        return updated_items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def adjustQuality(Item, update_by):
        if Item.quality > 0 and Item.quality < 50:
            Item.quality = Item.quality + update_by


class Abstract_Item(ABC):
    def __init__(self, name):
        self.name = name


class General_Item(Abstract_Item):
    def __init__(self, name, sell_in: int, quality: int):
        super().__init__(name)
        self.sell_in = sell_in
        self.quality = quality

    def adjustSellIn(self):
        self.sell_in -= 1

    def adjustQuality(self):
        if 0 < self.quality < 50:
            self.quality -= 1
        pass


class Aged_Brie(General_Item):
     def adjustQuality(self):
         if 0 < self.quality < 50:
             self.quality += 1

class Sulfuras(Abstract_Item):
    def __init__(self, name):
        super().__init__(name)
        self.quality = 80
        self.sell_in = -1

class Backstage_Passes(General_Item):
    def adjustQuality(self):
        if 0 < self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                self.quality += 1
            if self.sell_in < 6:
                self.quality += 1

class Conjured(General_Item):
    def adjustQuality(self):
        if 0 < self.quality < 50:
            self.quality -= 2




#
# class Conjured(Item):
#     pass
#
# class Backstage_passes(Item):
#     pass

class GildedRoseTest(unittest.TestCase):
    aged_brie = "Aged Brie"
    sulfuras = "Sulfuras, Hand of Ragnaros"
    elixir = "Elixir of the Mongoose"
    conjured = "Conjured Mana Cake"
    passes = "Backstage passes to a TAFKAL80ETC concert"

    # sell in, quality
    def test_sulfuras(self):
        items = [("fixme", 0, 0), ("san jose", 2, 2), "Sulfuras, Hand of Ragnaros"]
        gilded_rose = GildedRose(items)
        result_list = gilded_rose.new_day_list()
        self.assertEqual((self.sulfuras, -1, 80), (result_list[2].name, result_list[2].sell_in, result_list[2].quality))

    def test_aged_brie(self):
        items = [("fixme", 0, 0), (self.aged_brie, 2, 2), self.sulfuras]
        gilded_rose = GildedRose(items)
        result_list = gilded_rose.new_day_list()
        self.assertEqual((self.aged_brie, 1, 3), (result_list[1].name, result_list[1].sell_in, result_list[1].quality))

    def test_backstage_passes(self):
        items = [(self.passes, 15, 20), (self.aged_brie, 2, 2), self.sulfuras]
        gilded_rose = GildedRose(items)
        result_list = gilded_rose.new_day_list()
        self.assertEqual((self.passes, 14, 21), (result_list[0].name, result_list[0].sell_in, result_list[0].quality))

    def test_elixir(self):
        items = [(self.elixir, 7, 5), (self.aged_brie, 2, 2), self.sulfuras]
        gilded_rose = GildedRose(items)
        result_list = gilded_rose.new_day_list()
        self.assertEqual((self.elixir, 6, 4), (result_list[0].name, result_list[0].sell_in, result_list[0].quality))

    def test_conjure(self):
        items = [(self.conjured, 7, 6), (self.aged_brie, 2, 2), self.sulfuras]
        gilded_rose = GildedRose(items)
        result_list = gilded_rose.new_day_list()
        self.assertEqual((self.conjured, 6, 4), (result_list[0].name, result_list[0].sell_in, result_list[0].quality))

if __name__ == '__main__':
    unittest.main()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
