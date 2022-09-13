import os
with open(os.path.expanduser('~/somedir/mykeys.yaml'),encoding='UTF-8') as file:
    for item in file:
        item=item.strip()
        print('ccc item is: ', str(item))
        if "var1" in item:
            print("Found var1")
