import sys
import os
import inspect


from MapNavigation_v1_0.Common.AbstractClass import AbstractFrame
from MapNavigation_v1_0.settings import InstalledFrame, JumpInfo, QUIT, BASE_DIR


# 此类作为运行框架不要轻易改动
class MainLoop:
    def __init__(self, app_frame):
        self.screen = app_frame.screen
        self.clock = app_frame.clock
        self.window_size = app_frame.window_size
        self.frames = {}
        self.jum_info = {}
        self.import_apps_with_jump_info()

    def loop(self):  # 页面之间跳转需要在settings.py中注册跳转信息
        choice = self.jum_info.get("Start", False)
        if not choice:
            raise ValueError("Not Register Frames for 'Start'")
        choice = self.jum_info["Start"].show(self.screen, self.clock)
        while choice != QUIT and choice in self.jum_info.keys():
            choice = self.jum_info[choice].show(self.screen, self.clock)
        if self.jum_info.get(choice, False):
            self.jum_info[choice].show(self.screen, self.clock)

    def register_app(self, pack_name, module_name):
        pack_path = os.path.join(BASE_DIR,pack_name)
        sys.path.append(pack_path)
        module = __import__(module_name)
        frame = getattr(module,module_name)  # 获得模块中的应用类
        if inspect.isclass(frame) and issubclass(frame, AbstractFrame):
            self.frames[module_name] = frame(self.window_size)
        else:
            raise SyntaxError("Not Inherited from AbstractFrame Or Not Class")

    def register_jump_info(self):
        for key, value in JumpInfo.items():
            if self.frames.get(value, False):
                self.jum_info[key] = self.frames[value]

    def import_apps_with_jump_info(self):
        for pack_name,module_name in InstalledFrame.items():
            self.register_app(pack_name, module_name)
        self.register_jump_info()
