from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import ItemTypes, Items, Attributes, ItemAttributes


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        t1 = ItemTypes(name="Axe")
        t2 = ItemTypes(name="Sword")
        a1 = Attributes(name="Magic", description="A magical item")
        a2 = Attributes(name="Sharp", description="A sharp item")     
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(a1)
        db.session.add(a2)
        db.session.commit()

        i1 = Items(name="Enchanted Axe", fk_item_type=1)
        i2 = Items(name="Vicious Sword", fk_item_type=2)
        db.session.add(i1)
        db.session.add(i2)
        db.session.commit()

        it1 = ItemAttributes(fk_item_id=1, fk_attribute_id=1)
        it2 = ItemAttributes(fk_item_id=2, fk_attribute_id=1)
        it3 = ItemAttributes(fk_item_id=2, fk_attribute_id=2)
        db.session.add(it1)
        db.session.add(it2)
        db.session.add(it3)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestReadItemTypes(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('read_item_types'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Axe", response.data)

class TestReadAttribute(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('read_attributes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Magic", response.data)
        self.assertIn(b"A magical item", response.data)
        self.assertIn(b"Sharp", response.data)
        self.assertIn(b"A sharp item", response.data)

class TestReadItems(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('read_items'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Vicious Sword", response.data)

class TestReadItem(TestBase):
    def test_home_get(self):
        response = self.client.post(
            url_for('read_item'),
            data = dict(item_id=1),
            follow_redirects=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enchanted Axe", response.data)
        self.assertIn(b"Magic", response.data)
        self.assertIn(b"A magical item", response.data)


class TestAdd(TestBase):
    def test_add_item_type(self):
        response = self.client.post(
            url_for('create_type'),
            data = dict(item_type_name="Mace"),
            follow_redirects=True
        )
        read = self.client.get(url_for('read_item_types'))
        self.assertIn(b"Mace", read.data)