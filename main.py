import json
import os

ab = {}  # 通讯录保存在字典中
# 从字典中读取通讯录
if os.path.exists('addressbook20201303096杨泽林.json'):
    with open(r'addressbook20201303096杨泽林.json', 'r', encoding='utf-8') as f:
        ab = json.load(f)
while True:
    print('|---欢迎使用通讯录程序---|')
    print('|---1.显示通讯录清单----|')
    print('|---2.查询联系人资料----|')
    print('|---3.插入新联系人------|')
    print('|---4.删除已有联系人----|')
    print('|---0.退出------------|')
    choice = input("请选择功能菜单（0-4）：")
    if choice == '1':
        if len(ab) == 0:
            print('通讯录为空')
        else:
            for k, v in ab.items():
                print('姓名 = {}, 联系电话 = {}'.format(k, v))
    elif choice == '2':
        name = input('请输入联系人姓名')
        if name not in ab:
            ask = input('联系人不存在是否增加用户资料（Y/N）')
            if ask in ['Y', 'y']:
                tel = input('请输入用户电话')
                ab[name] = tel
        else:
            print('联系人信息：{}{}'.format(name, ab[name]))
    elif choice == '3':
        name = input('请输入联系人姓名')
        if name in ab:
            print('已存在联系人，联系人信息：{}{}'.format(name, ab[name]))
            ask = input('是否修改用户资料（Y/N）')
            if ask in ['Y', 'y']:
                tel = input('请输入用户电话')
                dict[name] = tel
        else:
            tel = input('请输入用户电话')
            ab[name] = tel
    elif choice == '4':
        name = input('请输入联系人姓名')
        if name not in ab:
            print('联系人{}不存在'.format(name))
        else:
            tel = ab.pop(name)
            print('删除联系人{}{}'.format(name, tel))
    elif choice == '0':
        with open(r'addressbook20201303096杨泽林.json', 'w', encoding='utf-8') as f:
            json.dump(ab, f)
        break
