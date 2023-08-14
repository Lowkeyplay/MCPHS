# 本程序由BlueCloudTeam的BlueGa制作
# 版本:0.0.6
# 更新日期:2023.8.1
# 禁止搬运!


import pyautogui as gui
import time
import sys

gui.size()
gui.position()
gui.FAILSAFE = True

# ------------------------------------------------↓更新内容↓------------------------------------------------------------
with open("UpdateContent.txt", "w", encoding="utf-8") as UC:
    UC.write("Minecraft脚本更新内容\n版本:0.0.6\n更新内容:\n1.新增注意事项;2.优化程序使用\n禁止搬运!\nMade By BlueCloudTeam")

# ----------------------------------------------↓主体↓---------------------------------------------------------------------


def start():  # 开始菜单部分
    print("""
        minecraft脚本
    1.开启脚本   2.打开教程
    3.联系我们   4.版本详情
    5.认识程序   6.注意事项
    0.退出程序   0.退出程序
    
    Made By BlueCloudTeam
    """)
    StartQ1 = input("选择:")
    if StartQ1 == "1":
        minecraftscript()
    elif StartQ1 == "2":
        cos()
    elif StartQ1 == "3":
        print("联系我们请加入QQ群:906798648(团队群)")
        start()
    elif StartQ1 == "4":
        print("此版本为0.0.6,更新日期:2023.8.1")
        print("Made By BlueCloudTeam")
        start()
    elif StartQ1 == "5":
        rtp()
    elif StartQ1 == "6":
        notes()
    elif StartQ1 == "0":
        print("已退出!欢迎下次光临!awa!")
        sys.exit(0)
    else:
        start()


def minecraftscript():  # 脚本部分
    print("""
        minecraft脚本
    1.自动挖石头(刷石机)
    2.自动挖矿(直线矿道)
    3.自动打怪(刷怪塔)
    4.敬请期待
    0.返回
    """)
    ScriptQ1 = input("选择:")
    if ScriptQ1 == "1":
        matictime = int(input("挖的时间(秒):"))
        time.sleep(5)
        gui.mouseDown(button="left")
        time.sleep(matictime)
        gui.mouseUp(button="left")
        print("运行结束!欢迎下次光临!awa!")
        start()
    elif ScriptQ1 == "2":
        autominingtime = int(input("持续时间(秒):"))
        time.sleep(5)
        gui.mouseDown(button="left")
        gui.keyDown("w")
        time.sleep(autominingtime)
        gui.mouseUp(button="left")
        gui.keyUp("w")
        print("运行结束!欢迎下次光临!awa!")
        start()
    elif ScriptQ1 == "3":
        autokillzombiletime = int(input("持续次数(次):"))
        time.sleep(5)
        for autokillzombile in range(autokillzombiletime):
            gui.mouseDown(button="left")
            gui.mouseUp(button="left")
            time.sleep(1.2)
        time.sleep(1)
        print("运行结束!欢迎下次光临!awa!")
        start()
    elif ScriptQ1 == "4":
        print("都说了敬请期待!咋不听呢!哼!")
        minecraftscript()
    elif ScriptQ1 == "0":
        print("已返回!")
        start()
    else:
        minecraftscript()


def cos():  # 教程部分
    print("""
        minecraft脚本教程
    1.自动挖石头(刷石机)
    2.自动挖矿(直线矿道)
    3.自动打怪(刷怪塔)
    4.敬请期待
    0.返回
    """)
    cosQ1 = input("选择:")
    if cosQ1 == "1":
        print("自动挖石头(刷石机)教程:1.将稿子拿在手中;2.启动程序;3.在5秒内返回游戏内;4.启动后在短时间内对准石头")
        time.sleep(3)
        cos()
    elif cosQ1 == "2":
        print(
            "自动挖矿(直线矿道)教程:1.打开F3,将准星对准两个方块的缝隙往上一像素并且确保准星为90°(0°,90°,-90°,180°)1.身处两格高的直线矿道中;2.将稿子拿在手中;3.启动程序;4.在5秒内返回游戏内;5.启动成功:DDDDDDDDDDD")
        time.sleep(5)
        cos()
    elif cosQ1 == "3":
        print("自动打怪(刷怪塔)教程:1.将武器拿在手中;2.启动程序;3.在5秒内返回游戏内;4.启动后在短时间内对准怪物落点中心")
        time.sleep(2)
        cos()
    elif cosQ1 == "4":
        print("都说了敬请期待!哼!")
        cos()
    elif cosQ1 == "0":
        print("已返回!")
        start()
    else:
        cos()


def rtp():  # 认识程序部分
    print(
        "本程序是专门做给Minecraft的,此程序会大大帮助我们解决玩Minecraft时遇到的简单且繁琐的事,例如挖石头,刷怪等!并且此程序不会影响到其他玩家的游戏,非常适合玩生存类存档或服务器.此程序目前版本为0.0.6!温馨提示:如果是玩服务器的话,一定要注意服务器规则哦! ")
    print("""
	Made By BlueCloudTeam
    """)
    time.sleep(3)
    start()


def notes():
    print("可使用本程序的Minecraft版本:1.8,1.12.2,1.18.2,1.19.2[测试过]")
    print("如果遇到问题,可以进行反馈,如何反馈请看联系我们")
    print("感谢支持:DDDDDDDDDDDDDDDDDD")
    time.sleep(3)
    start()


# ------------------------------------------------↓启动部分↓------------------------------------------------------------

start()



