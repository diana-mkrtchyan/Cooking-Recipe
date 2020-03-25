import json
# read file
with open("data.json") as file:
  receipts = json.load(file)


print('How much time do you have')
user_time = input()
print('User time ' + user_time)

receipts_len = len(receipts)
i = 0

while ( i < receipts_len ):
  if receipts[i]['time'] <= user_time : 
    print(receipts[i]['name']);
    print( receipts[i]['products'])
  i += 1
