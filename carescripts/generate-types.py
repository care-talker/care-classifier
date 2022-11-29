items = []
foreignkeys = []
with open("models.py", "r+") as f:
    item = {}
    for line in f:
        if "class " in line:
            item = {}
            item["name"] = line[line.find(" ") + 1 : line.find("(")]
            item["fields"] = []
            print(item)
        if " = " in line:
            field = {}
            line = line.split()
            field["item"] = line[0]
            if "Foreign" in line[2]:
                temp = f.readline()
                temp = temp.split()[0]
                field["value"] = temp[1 : temp.find('"', 1)]
                foreignkeys.append(
                    {"parent": field["value"].lower(), "child": item["name"]}
                )
            else:
                field["value"] = "auto"
            field["child"] = False
            item["fields"].append(field)
        if line == "\n" and item:
            items.append(item)
            item = False
    items.append(item)

output = open("types.py", "w")

filters = []
orders = []
definitions = []
inputs = []
partials = []

# input
inputTemplate = """@strawberry_django.input(models.{item})
class {item}Input:
    id: auto
{inputfields}

"""

# partial
partialTemplate = """@strawberry_django.input(models.{item}, partial=True)
class {item}PartialInput({item}Input):
    pass

"""

# filter

filterTemplate = """@strawberry_django.filters.filter(models.{item}, lookups=True)
class {item}Filter:
    id: auto
{filterfields}

"""

# order
orderTemplate = """@strawberry_django.ordering.order(models.{item})
class {item}Order:
{orderfields}

"""

# definition
typeTemplate = """@strawberry_django.type(
    models.{item}, filters={item}Filter, order={item}Order, pagination=True
)
class {item}:
    id: auto
{fields}

"""


for item in items:
    children = [k for k in foreignkeys if k["parent"] == item["name"].lower()]
    for child in children:
        item["fields"].append(
            {
                "item": child["child"].lower() + "s",
                "value": child["child"],
                "child": True,
            }
        )

    fields = ""
    orderfields = ""
    filterfields = ""
    inputfields = ""
    for field in item["fields"]:
        fields = fields + """    {var}: {val}\n""".format(
            var=field["item"],
            val=(
                "auto"
                if field["value"] == "auto"
                else ('"' + field["value"] + '"' if field["child"] else field["value"])
            ),
        )
        inputfields = inputfields + """    {var}: auto\n""".format(var=field["item"])
        orderfields = orderfields + """    {var}: {val}\n""".format(
            var=field["item"],
            val=(
                "auto"
                if field["value"] == "auto"
                else (
                    '"' + field["value"] + "Order" + '"'
                    if field["child"]
                    else field["value"] + "Order"
                )
            ),
        )
        filterfields = filterfields + """    {var}: {val}\n""".format(
            var=field["item"],
            val=(
                "auto"
                if field["value"] == "auto"
                else (
                    '"' + field["value"] + "Filter" + '"'
                    if field["child"]
                    else field["value"] + "Filter"
                )
            ),
        )
    inputs.append(
        inputTemplate.format(
            item=item["name"],
            inputfields=inputfields,
        )
    )
    partials.append(partialTemplate.format(item=item["name"]))
    filters.append(
        filterTemplate.format(
            item=item["name"],
            filterfields=filterfields,
        )
    )
    orders.append(
        orderTemplate.format(
            item=item["name"],
            orderfields=orderfields,
        )
    )
    definitions.append(
        typeTemplate.format(
            item=item["name"],
            fields=fields,
        )
    )
output.write(
    """from typing import List
from django.contrib.auth import get_user_model
from strawberry import auto
import strawberry_django
from . import models

@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto
@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
    email: auto

    """
)
output.write("\n# filters\n")
output.writelines(filters)
output.write("\n# orders\n")
output.writelines(orders)
output.write("\n# types\n")
output.writelines(definitions)
output.write("\n# input types\n")
output.writelines(inputs)
output.write("\n# partial inputs\n")
output.writelines(partials)
