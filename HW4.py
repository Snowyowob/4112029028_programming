# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:10:04 2023

@author: User
"""
import inventory_module as im

while True:
        print("\n進銷存系統\n1.新增物品\n2.移除物品\n3.查看庫存\n4.退出")
        choice = input("請選擇操作：")
        if choice == "1":
            item_name = input("請輸入物品名稱：")
            quantity = int(input("請輸入數量："))
            im.add_item(item_name, quantity)
        elif choice == "2":
            item_name = input("請輸入物品名稱：")
            quantity = int(input("請輸入數量："))
            im.remove_item(item_name, quantity)
        elif choice == "3":
            im.view_inventory()
        elif choice == "4":
            break
