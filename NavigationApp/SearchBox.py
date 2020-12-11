from MapNavigation_v1_0.Common.InpuBox import TextBox
from MapNavigation_v1_0.NavigationApp.RollDownLabel import RollDownLabel
from MapNavigation_v1_0.Common.Label import Label


class SearchBox:
    def __init__(self, points, map_manger):
        self.pA_down_label = RollDownLabel(0, 70, points)
        self.pA_box = TextBox(150, 20, 0, 50, callback=self.pA_down_label.create_surf)
        self.map_manger = map_manger
        self.pA_left_label = Label("Enter Address:", 15)

    def event(self, event):
        state = self.pA_box.safe_key_down(event)
        if state:
            self.pA_down_label.reset()
        point = self.pA_down_label.get_point(event, state)
        if point:
            self.pA_box.text = point.name
            self.pA_down_label.reset()  # 选择到输入框中后将下拉提示清除
            self.map_manger.add_goal_point(point)

    def draw(self, screen):
        self.pA_left_label.draw(screen)
        self.pA_down_label.draw(screen)
        self.pA_box.draw(screen)
