# 4. Get first and second best scores

scores_list = [40, 89, 90, 89, 23, 90, 50]

unique_scores = sorted(set(scores_list), reverse=True)

first_best = unique_scores[0]
second_best = unique_scores[1]

print("First score:", first_best)
print("Second score:", second_best)
