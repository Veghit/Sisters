class Shift:
    def __init__(self, day, shift_type, hour_list, min_nurses, max_nurses):
        self.day = day
        self.shift_type = shift_type
        self.hour_list = hour_list
        self.min_nurses = min_nurses
        self.max_nurses = max_nurses

    def __repr__(self):
        return ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][self.day - 1] + ":" + self.shift_type
