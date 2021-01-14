import json

with open('/Users/marineluciani/Desktop/exopok/pokemon.json') as file:
  jsonData = json.load(file)

number = (len(jsonData["pokemon"]))
print (number)

# for i in jsonData ["pokemon"]:
#   print (i ["weight"])


# def name():
#     for i in jsonData ["pokemon"]:
#         print (i ["name"])

# b = ["10.00kg"]

# if weight > b:
#      print (name)