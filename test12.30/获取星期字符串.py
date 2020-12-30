#
# # Weeknameprint.py
# weekstr = "星期一星期二星期三星期四星期五星期六星期天"
# weekid = eval(input("输入星期数字（1-7）:"))
# pos = (weekid - 1)*3
# print(weekstr[pos:pos+3])

weekstr = "一二三四五六七"
weekid = eval(input("输入星期数字:"))
print("星期"+weekstr[weekid-1])