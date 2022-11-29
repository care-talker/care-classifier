items = []
with open("models.py", "r+") as f:
    item = {}
    for line in f:
        if "class " in line:
            item = {}
            items.append(line[line.find(" ") + 1 : line.find("(")])

output = open("schema.py", "w")

queries = []
mutations = []

queryTemplate = """    {name}: {item} = strawberry_django.field()
    {name}s: List[{item}] = strawberry_django.field()\n"""
mutationTemplate = """    create{item}: {item} = mutations.create({item}PartialInput)
    create{item}s: List[{item}] = mutations.create({item}PartialInput)
    update{item}s: List[{item}] = mutations.update({item}PartialInput)
    delete{item}s: List[{item}] = mutations.delete()\n"""


for item in items:
    queries.append(queryTemplate.format(name=item[0].lower() + item[1:], item=item))
    mutations.append(mutationTemplate.format(item=item))


output.write(
    """from typing import List
import strawberry
import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations
from .types import *
@strawberry.type
class Query:\n"""
)
output.writelines(queries)
output.write(
    """\n@strawberry.type
class Mutation:
    register: User = auth.register(UserInput)\n"""
)
output.writelines(mutations)
output.write("\nschema = strawberry.Schema(query=Query, mutation=Mutation)\n")
