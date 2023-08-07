#Example Program 5_5
Total1 = 0.0
Score = ""
Count = 1
while Score != "-1":
    Score = input(f"Enter Score value #{Count}:")
    if Score != "-1":
        Count += 1
        Total1 += float(Score)

Count -= 1
print()
print("Number of score :",Count)
print("Total Score value :",Total1)
print("Average Score :",Total1/Count)