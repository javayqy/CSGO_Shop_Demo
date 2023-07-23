import buff
import dmarket
from tkinter import *


def main():
    root = Tk()
    root.title("饰品查询")

    label = Label(root, text="输入物品名称:")
    label.grid()

    entry = Entry(root, font=("宋体", 25), fg="red")
    entry.grid()
    # 创建按钮
    button = Button(root, text="START", )
    button.grid(row=1, column=1)
    root.mainloop()


# 定义物品名称

# goods_name = buff.get_goods_name()
#
# # 获取buffdata
# buffdata = buff.getdata(timestamp=buff.get_time(), goods_id=buff.set_goods_id(goods_name))
#
# buffLowPrice_CNY = buff.get_buff_low_price(buffdata)
# buffLowPrice_USD = round(buffLowPrice_CNY / 7.2, 2)
#
# steamLowPrice = buff.get_steam_low_price(buffdata)
# steamLowPrice_US = buff.get_steam_low_price(buffdata)
#
# dmdata = dmarket.getdata(goods_name)
# dmlowPrice_USD = round(dmarket.get_low_price(dmdata), 2)
# dmlowPrice_CNY = round(dmlowPrice_USD * 7.2, 2)
#
# print("steam最低价格(人民币):" + steamLowPrice + "  steam最低价格(美元):" + steamLowPrice_US)
# print("buff最低价格(人民币）：" + str(buffLowPrice_CNY) + "  （美元）" + str(buffLowPrice_USD))
# print("DM最低价格（人民币）：" + str(dmlowPrice_CNY) + "  DM最低价格(美元)：" + str(dmlowPrice_USD))
#
# buff.save_josn_data(buffdata)
# dmarket.save_josn_data(dmdata)

main()
