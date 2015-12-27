from django.db import models

class Person(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class ItemCategory(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Item(models.Model):
  name = models.CharField(max_length=200)
  category = models.ForeignKey(ItemCategory)

  def __str__(self):
    return "{name} ({type})".format(name=self.name, type=self.category)

class Selection(models.Model):
  person = models.ForeignKey(Person)
  item = models.ForeignKey(Item)
  quantity = models.IntegerField()

  def __str__(self):
    return "{qty} {item} for {person}".format(
      person=self.person,
      item=self.item,
      qty=self.quantity)