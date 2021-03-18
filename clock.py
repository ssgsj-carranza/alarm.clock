class AlarmClock:
    def __init__(self):
        self.current_time = ""
        self.alarm_on_off = ""
        self.alarm_time = ""

    def change_time(self):
        self.current_time = input("Please set the time")
        print("The time is: ", self.current_time)

    def toggle_alarm(self):
        self.alarm_on_off = input("Alarm on or off?")
        if input == "on":
            print("alarm is on")
        elif input == "off":
            print("alarm is off")

    def set_alarm(self):
        self.alarm_time = input("Please set alarm time")
        print("Your alarm is set for: ", self.alarm_time)

