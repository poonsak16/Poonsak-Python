scores = [78,85,92,67,88,95,73,84]

max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores) /len(scores)
count_morethan_80 = len([s for s in scores if s > 80])

print("MaxScore: ",max_score)
print("MinScore: ",min_score)
print("AvgScore: ",avg_score)
print("CountMorethan 80 Score: ",count_morethan_80)