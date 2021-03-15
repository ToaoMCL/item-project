from application.models import Attributes, Items, ItemAttributes, ItemTypes
from application import db

db.drop_all()
db.create_all()

db.session.add(ItemTypes(name="Axe"))
db.session.add(ItemTypes(name="Hammer"))
db.session.add(ItemTypes(name="Sword"))
db.session.add(ItemTypes(name="Bow"))
db.session.add(ItemTypes(name="Crossbow"))
db.session.add(ItemTypes(name="Potion"))
db.session.add(ItemTypes(name="Ration"))
db.session.add(ItemTypes(name="Tool"))


db.session.add(Attributes(
    name="Weapon", description="This item can be used to make attacks"))
db.session.add(Attributes(
    name="Magic", description="This item has magical properties making it resiliant"))
db.session.add(Attributes(
    name="Sentient", description="This item has a mind of its own, it can make choices and communicate as well as have its own moral compass"))
db.session.add(Attributes(
    name="Loading", description="This item has to be loaded before use"))
db.session.add(Attributes(
    name="Poisonous", description="This item is poisonous, it can damage whoever consumes it or gets wounded by it"))
db.session.add(Attributes(
    name="Artistic", description="This item allows you to spend a day to create a painting or a sculpture"))
db.session.add(Attributes(
    name="Shelter", description="This item provides its user with shelter from non extreme weather"))
db.session.add(Attributes(
    name="Healing", description="This item can restore vitality to its user"))
db.session.add(Attributes(
    name="Ranged", description="This item can be used from a distance"))
db.session.add(Attributes(
    name="Bludgeoning", description="This item can inflict non lethal damage to an oponent"))
db.session.add(Attributes(
    name="Piercing", description="This item can penetrate armor"))

db.session.commit()



