import json

with open("random.txt") as f:
  text = f.read()

text = text.split()
seen = []
amount = []
after = []
after_amount = []

for i in text:
  if not i in seen:
    seen.append(i)
    amount.append(0)
  
  if i in seen:
    amount[seen.index(i)] += 1


for i in (seen):
  for k in range(len(text) - 1):
    if text[k] == i:
      after.append(str(text[k + 1]).replace("'", '"'))
  after_amount.append(after)
  after = []

with open("stuff.json", "w") as file:
  file.write("{")
  file.write("  ")
  file.write("}")

with open("stuff.json", "+r") as file:
  data = json.load(file)

  for i in range(len(seen)):
    data[seen[i]] = after_amount[i]
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()


  