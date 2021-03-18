from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import ItemTypes, Items, Attributes, ItemAttributes


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        t1 = ItemTypes(name="Axe")
        t2 = ItemTypes(name="Sword")
        t3 = ItemTypes(name="Tool")
        a1 = Attributes(name="Magic", description="A magical item")
        a2 = Attributes(name="Sharp", description="A sharp item")
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
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

class TestMainPages(TestBase):
    def test_read_get(self):
        response = self.client.get(url_for("read"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Read Page", response.data)

    def test_create_get(self):
        response = self.client.get(url_for("create"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Page", response.data)

    def test_update_get(self):
        response = self.client.get(url_for("update"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Update Page", response.data)

class TestReadItemTypes(TestBase):
    def test_read_types(self):
        response = self.client.get(url_for("read_item_types"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Axe", response.data)

class TestReadAttribute(TestBase):
    def test_read_attributes(self):
        response = self.client.get(url_for("read_attributes"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Magic", response.data)
        self.assertIn(b"A magical item", response.data)
        self.assertIn(b"Sharp", response.data)
        self.assertIn(b"A sharp item", response.data)

class TestReadItems(TestBase):
    def test_read_items(self):
        response = self.client.get(url_for("read_items"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Vicious Sword", response.data)

class TestReadItem(TestBase):
    def test_read_item(self):
        response = self.client.post(
            url_for("read_item"),
            data = dict(item_id=1),
            follow_redirects=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enchanted Axe", response.data)
        self.assertIn(b"Magic", response.data)
        self.assertIn(b"A magical item", response.data)


class TestAddType(TestBase):
    def test_add_item_type(self):
        response = self.client.get(url_for("read_item_types"))
        self.assertNotIn(b"Mace", response.data)
        response = self.client.post(
            url_for("create_type"),
            data = dict(item_type_name="Mace"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_item_types"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Mace", response.data)

class TestAddAttribute(TestBase):
    def test_add_item_type(self):
        response = self.client.get(url_for("read_attributes"))
        self.assertNotIn(b"Divine", response.data)
        self.assertNotIn(b"Forged by a divine being", response.data)
        response = self.client.post(
            url_for("create_attribute"),
            data = dict(attribute_name="Divine", attribute_description="Forged by a divine being"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_attributes"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Divine", response.data)
        self.assertIn(b"Forged by a divine being", response.data)

class TestAddItem(TestBase):
    def test_add_item(self):
        response = self.client.get(url_for("read_items"))
        self.assertNotIn(b"Hand of Vecna", response.data)
        self.assertNotIn(b"Tool", response.data)
        response = self.client.post(
            url_for("create_item"),
            data = dict(item_name="Hand of Vecna", item_type=3),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_items"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hand of Vecna", response.data)
        self.assertIn(b"Tool", response.data)

class TestAddItemAttribute(TestBase):
    def test_add_item_attribute(self):
        response = self.client.post(
            url_for("read_item"),
            data = dict(item_id=1),
            follow_redirects=True
            )
        self.assertNotIn(b"Sharp", response.data)
        self.assertNotIn(b"A sharp item", response.data)

        response = self.client.post(
            url_for("create_attribute_link"),
            data = dict(item_id=1, attribute_id=2),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("read_item"),
            data = dict(item_id=1),
            follow_redirects=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Sharp", response.data)
        self.assertIn(b"A sharp item", response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(url_for("read_items"))
        self.assertIn(b"Vicious Sword", response.data)
        self.assertIn(b"Sword", response.data)

        response = self.client.post(
            url_for("delete"),
            data = dict(active_table="Items", item_id=2),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(url_for("read_items"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Vicious Sword", response.data)
        self.assertNotIn(b"Sword", response.data)

class TestUpdateType(TestBase):
    def test_update_type(self):
        response = self.client.get(url_for("read_item_types"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Bow", response.data)

        response = self.client.post(
            url_for("update_type"),
            data = dict(item_type_id=1, new_type_name="Bow"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_item_types"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bow", response.data)

class TestUpdateAttribute(TestBase):
    def test_update_attribute(self):
        response = self.client.get(url_for("read_attributes"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Butter Forged", response.data)
        self.assertNotIn(b"A magnificent item crafted through only the finest dairy products", response.data)

        response = self.client.post(
            url_for("update_attribute"),
            data = dict(attribute_id=1, new_attribute_name="Butter Forged", new_attribute_description="A magnificent item crafted through only the finest dairy products"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_attributes"))
        self.assertIn(b"Butter Forged", response.data)
        self.assertIn(b"A magnificent item crafted through only the finest dairy products", response.data)

class TestUpdateItem(TestBase):
    def test_update_item(self):
        response = self.client.get(url_for("read_items"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Hand of Vecna", response.data)
        # self.assertNotIn(b"Tool", response.data)

        response = self.client.post(
            url_for("update_item"),
            data = dict(item_id=1, new_item_name="Hand of Vecna"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for("read_items"))
        self.assertIn(b"Hand of Vecna", response.data)


