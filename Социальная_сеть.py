file = open('social_net_stats.txt', encoding='utf-8')
lines = file.readlines()
cnt = 0
posts = 0
for line in lines[1:]:
    data = line.split(',')
    print(data)
    if data[1]:
        if float(data[1]) >= 60 and int(data[4]) >= 1:
            cnt += 1
            posts += int(data[6])
print(posts / cnt)
