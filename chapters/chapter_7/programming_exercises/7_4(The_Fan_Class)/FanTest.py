from Fan import Fan


def main():
    fan1 = Fan(Fan.HIGH, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    print("Fan 1 of color", fan1.get_color(), "with on state", fan1.get_on(), "has radius of", fan1.get_radius(),
          "with speed of", fan1.get_speed())

    print("Fan 2 of color", fan2.get_color(), "with on state", fan2.get_on(), "has radius of", fan2.get_radius(),
          "with speed of", fan2.get_speed())


main()
