import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# app所在的模块名即py文件必须要与内部的主应用类同名，目录名可以不同

# key为所在目录名，value为所在模块名
# 将应用注册到主循环中
InstalledFrame = {
    "StartApp": "StartApp",
    "NavigationApp": "NavigationApp",
    "OverApp": "OverApp",
}

QUIT = "quit"

# Start 跳转信息必须添加 QUIT跳转信息可以不添加,但是应用如果要结束整个进程，应用类的show方法必须返回QUIT
# key为跳转信息，value为模块中的应用类名
# 将应用何时使用注册到主循环中，如果没有JumpInfo注册则应用类不会被执行
JumpInfo = {
    "START NAVIGATION": "NavigationApp",
    "BACK TO MENU": "StartApp",
    QUIT: "OverApp",
    "Start": "StartApp",
}
