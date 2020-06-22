from collections import defaultdict

# user_dict = {}
# users = ["zhuhai1", "zhuhai2", "zhuhai3", "zhuhai1", "zhuhai2", "zhuhai2"]
# for user in users:
#     user_dict.setdefault(user, 0)
#     user_dict[user] += 1

    # if user in user_dict:
    #     user_dict[user] += 1
    # else:
    #     user_dict[user] = 1

# print(user_dict)



# defaultdict如果key值不存在则默认赋值为0，这样不会报错
# default_dict = defaultdict(int)
# users = ["zhuhai1", "zhuhai2", "zhuhai3", "zhuhai1", "zhuhai2", "zhuhai2"]
# for user in users:
#     default_dict[user] += 1

def gen_default():
    # 用函数的方法设置默认值
    return {
        "name": "",
        "nums": 0
    }
default_dict = defaultdict(gen_default)
default_dict["group1"]
# group_dict = {
#     "group": {
#         "name": "",
#         "nums": 0
#     }
# }
pass