from application import db


class Attributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    items = db.relationship("ItemAttributes", backref="attributes")

class ItemTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    items = db.relationship("Items", backref="item_types")

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    fk_item_type = db.Column(db.Integer, db.ForeignKey(
        "item_types.id"), nullable=False)
    items = db.relationship("ItemAttributes", backref="items")

class ItemAttributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_item_id = db.Column(db.Integer, db.ForeignKey(
        "items.id"), nullable=False)
    fk_attribute_id = db.Column(db.Integer, db.ForeignKey(
        "attributes.id"), nullable=False)
