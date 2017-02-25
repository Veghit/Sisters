from Shift import Shift


class Nurse:
    def __init__(self, name, is_supervisor, is_ladies, is_general_rec, workload, holidays, preferred=[], unwanted=[]):
        self.name = name  # not one to one
        self.is_supervisor = is_supervisor
        self.is_ladies = is_ladies  # capable of working in a ladies recovery room
        self.is_general_rec = is_general_rec
        self.workload = workload  # full-time or less
        self.holidays = holidays
        self.preferred = preferred
        self.unwanted = unwanted
        self.personal_constraints = []

    def __str__(self):
        return self.name + "\n" + "\tladies:" + str(self.is_ladies)

    def set_preference(self, preferred):
        self.preferred = preferred

    def set_unwanted(self, unwanted):
        self.unwanted = unwanted

    def is_available(self, shift):

        day = shift.day
        shift_type = shift.shift_type
        available = True
        for s in self.unwanted:
            if len(s) == 1:
                if str(day) == s:
                    available= False
                    break
            elif str(day) == s[0] and shift_type == s[1]:
                available = False
                break
        if available:
            print(self.name + " is available at shift-" + str(shift))
        else:
            print(self.name + " is not available at shift-" + str(shift))
        return available
