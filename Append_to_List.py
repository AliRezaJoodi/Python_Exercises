# GitHub.com/AliRezaJoodi

ledger = []

def AppendToList(name="", age=0):
  thisdict  = {}
  thisdict["Name"] = name
  thisdict["Age"] = age
  ledger.append(thisdict)
  #print(thisdict)

AppendToList("Ali", 20)
print(ledger)

AppendToList("Reza", 32)
print(ledger)