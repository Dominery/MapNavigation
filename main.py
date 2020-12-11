from MapNavigation_v1_0.MainLoop import MainLoop
from MapNavigation_v1_0.InitFrame import InitFrame


def main():
    app_frame = InitFrame((1080,680),"MapNavigation")
    app_loop = MainLoop(app_frame)
    app_loop.loop()


if __name__ == '__main__':
    main()
