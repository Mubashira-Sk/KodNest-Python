n = int(input())
scores=[]
for i in range(n):
    score=int(input())
    scores.append(score)
search_score=0
print(f"Highest Score:{max(scores)}")
print(f"Lowest Sore: {min(scores)}")
print(f"total Score: {sum(scores)}")
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")

