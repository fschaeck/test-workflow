import os
with open(os.path.expanduser('~/somedir/mykeys.yaml'),encoding='UTF-8') as file:
    for item in file:
        # strip the new-line characters \r and \n from the end of the line
        item=item.rstrip('\r\n')
        print('ccc item is: ', str(item))
        if "var1" in item:
            print("Found var1")
