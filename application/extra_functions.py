from application.models import Attributes, Items, ItemAttributes, ItemTypes

def GetDbTableNameFromPassedValue(value):
    if value == "Attributes":
        return Attributes
    elif value == "Item Types":
        return ItemTypes
    elif value == "Items":
        return Items
    elif value == "Item Attributes":
        return ItemAttributes
    else:
        return None