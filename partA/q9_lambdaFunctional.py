from functools import reduce

intern_score = [78, 90, 65, 88, 95]

top_scores = list(filter(lambda x : x > 80, intern_score))
print("top scoring interns score", top_scores)

average_scores = (int)(reduce(lambda x, y: x+y, intern_score)) / len(intern_score)
print("average score: ", average_scores)

def remarks(x):
    if x < 30: return "fail"
    elif x >= 30 and x < 70: return "good"
    else: return "excellent"

remark_list = list(map(remarks, intern_score))
print("remarks: ", remark_list)

