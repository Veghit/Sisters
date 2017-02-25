from Shift import Shift
from Nurse import Nurse
import openpyxl


def parse_excel(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet1 = workbook.get_active_sheet()
    nurses_list = []
    rows = sheet1.rows
    header = [x._value for x in rows.__next__()]
    for row in rows:
        name = row[header.index("Name")]._value
        is_supervisor = row[header.index("Supervisor")]._value
        is_ladies = row[header.index("Ladies")]._value
        is_general = row[header.index("General")]._value
        workload = row[header.index("workload")]._value
        holidays = row[header.index("Holidays")]._value
        preferred = str(row[header.index("preferred")]._value).split(",")
        unwanted = str(row[header.index("unwanted")]._value).split(",")
        new_nurse = Nurse(name, is_supervisor, is_ladies, is_general, workload, holidays,preferred,unwanted)
        nurses_list.append(new_nurse)
    return nurses_list


def create_shifts():
    shifts = []
    for day in range(1, 6):
        mor_shift = Shift(day, "M", [7, 8, 9, 10, 12], [2, 1, 1, 0, 1], [3, 2, 2, 2, 2])
        ev_shift = Shift(day, "E", [3], [4], [5])
        n_shift = Shift(day, "N", [11], [2], [2])
        shifts.append(mor_shift)
        shifts.append(ev_shift)
        shifts.append(n_shift)
    for day in range(6, 8):
        mor_shift = Shift(day, "M", [7], [2], [3])
        ev_shift = Shift(day, "E", [3], [2], [2])
        n_shift = Shift(day, "N", [11], [2], [2])
        shifts.append(mor_shift)
        shifts.append(ev_shift)
        shifts.append(n_shift)
    return shifts


nurse_list = parse_excel(file_name="input.xlsx")
for n in nurse_list:
    print(n)
shifts = create_shifts()
print(nurse_list[1].is_available(shifts[5]))
