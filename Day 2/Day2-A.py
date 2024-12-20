import fileinput

# Creates an array of tuples containing the difference and whether its increasing or decreasing
# [Diff,Increasing]
def Tuplizer(report):
    prev = None
    _report = []
    tmp = []
    for level in report:
        if prev == None:
            prev = level
        else:
            tmp.append(abs(prev - level))
            tmp.append(prev < level)
            prev = level
            _report.append(tmp)
        tmp = []
    return _report

def CheckRecord(record):
    Increasing = None
    for diff in record:
        if Increasing == None:
            Increasing = diff[1]
        if diff[0] > 3 or diff[0] < 1 or diff[1] != Increasing:
            return False
    return True
        
# Raw import
reports = []
tmp = []

for report in fileinput.input(files='input.txt'):    
    for level in report.split(' '):
        tmp.append(int(level))
    reports.append(tmp)
    tmp = []

# Diff list
diff_report = []
for report in reports:
    diff_report.append(Tuplizer(report))

# Good Report logic
good_count = 0
bad_count = 0

inc = None
good_report = True
for report in diff_report:
    if CheckRecord(report):
        good_count += 1
    else:
        bad_count += 1


print(good_count)
print(bad_count)
#print(len(reports))
