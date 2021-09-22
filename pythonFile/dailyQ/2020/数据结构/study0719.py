# 你想排序类型相同的对象，但是他们不支持原生的比较操作

from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

# def sort_notcompare():
users = [User(23), User(3), User(99)]
print(users)
# print(sorted(users, key=lambda u: u.user_id))
print(sorted(users,key=attrgetter('user_id')))#两种方法 下面的可以接受多个参数

# *********************************************************************************************************************************

#你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
from operator import itemgetter
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

