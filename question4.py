#question4
#display html table

from flask_table import Table, Col

class ItemTable(Table):
    name = Col('Country')
    description = Col('Date')

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
items = [Item('India', '  '),
         Item('India', '  '),
         Item('India', '  ')]

table = ItemTable(items)

print(table.__html__())
