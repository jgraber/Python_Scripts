import pandas as pd

def to_seconds(input):
    print(input)
    parts = input.split(":")
    print(parts)
    seconds = float(parts[1]) + float(parts[0]) * 60
    return seconds

def split_parts(input):
    # print(input)
    parts = cleaned.split(" ")
    if len(parts) == 2:
        return parts[0], parts[1][1:][:-1]
    else:
        name = " ".join(parts[:-2])
        # print(name)
        time = parts[-2]
        # print(time)
        return name, time[1:][:-1]


tests = []

with open("all_tests.txt", "r", encoding="utf-8") as x:
    while True:
        line = x.readline()
        
        # stop when end of file is reached
        if not line:
            break
        if " tests) [" in line:
            continue
        if " test) [" in line:
            continue
        if " [2] " in line:
            continue
        if "[" not in line:
            continue
        if "] Inconclusive: " in line:
            continue
        if "] Ignored:" in line:
            continue

        # print(line)
        cleaned = line.strip()
        name, duration = split_parts(cleaned)
        tests.append([name, to_seconds(duration)])


column_names=['name','duration']

# for row in tests:
#     print(row)
df = pd.DataFrame(tests, index=None,)

print(df.shape)
print(df.head)
df.to_csv('tests_converted.csv', encoding="utf-8", index=False, sep=";")