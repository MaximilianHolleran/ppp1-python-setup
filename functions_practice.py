def hello():
    print('hello user')
hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]
print(pack('Turkey Sandwich', 'Banana', 'Cookie'))

def eat_lunch(lunch_items):
    if lunch_items:
        print('First I eat', lunch_items[0])
        for lunch_item in lunch_items[1:]:
            print('Next I eat', lunch_item)
    else:
        print('My lunch box is empty')

eat_lunch(['Turkey Sandwich', 'Banana', 'Cookie'])
eat_lunch([])