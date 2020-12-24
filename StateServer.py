from MapNavigation_v1_0.Common.AbstractClass import Server
from MapNavigation_v1_0.NavigationApp.NavigatorState import NavigatorState
from MapNavigation_v1_0.QuitState import QuitState
from MapNavigation_v1_0.StartState import StartState
from MapNavigation_v1_0.settings import Request


class StateServer(Server):
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.states = {StartState.name: StartState(), QuitState.name: QuitState(),
                       NavigatorState.name: NavigatorState()}
        self.current_state = self.states[StartState.name]
        self.request = Request()
        self.request.add_server(self)

    def receive(self, state_name):
        self.current_state = self.states[state_name]
        self.execute()

    def execute(self):
        self.current_state.show(self.screen, self.clock)
