import pytest
from application.extra_functions import GetDbTableNameFromPassedValue
from application.models import ItemTypes, Items, Attributes, ItemAttributes

def test_ReturnFromInvalidTableName_isNone():
    assert GetDbTableNameFromPassedValue("Not a table") == None


def test_ReturnFromAttributeTableName_returnTable():
    assert GetDbTableNameFromPassedValue("Attributes") == Attributes


def test_ReturnFromItemTypesTableName_returnTable():
    assert GetDbTableNameFromPassedValue("Item Types") == ItemTypes


def test_ReturnFromItemsName_returnTable():
    assert GetDbTableNameFromPassedValue("Items") == Items


def test_ReturnFromItemAttributesName_returnTable():
    assert GetDbTableNameFromPassedValue("Item Attributes") == ItemAttributes
