# tem.py
tem = input("输入带有符号的温度:")
if tem[-1] in ['f','F']:
    c = (eval(tem[0:-1])-32)/1.8
    print("摄氏度为{:.2f}c".format(c))
elif tem[-1] in ['c','C']:
    f = 1.8*eval(tem[0:-1])+32
    print("华氏度为{:.2f}f".format(f))
else:
    print("格式错误")
