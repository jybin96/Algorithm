def reorderLogFiles(logs: [str]) -> [str]:
    digit = []
    letter = []
    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letter.append(log)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letter+digit

log_list = []

for _ in range(5):
    log_list.append(str(input()))


print(reorderLogFiles(log_list))