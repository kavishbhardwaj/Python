s1 = input()
if isinstance(s1, int):
    print("Integer")
elif isinstance(s1, float):
    print("Float")
elif isinstance(s1, str):
    print("String")
else:
    print("None")
    
a = input()
if a.isdigit():
   print("Integer")
elif a.replace('.','',1).isdigit() and a.count('.') < 2:
   print("Float")
else:
   print("None")