#Example Program 5_2
total=0.0
Max=6
for n in range(1,Max):
    score = float(input(f"Enter Score #(n):"))
    total = total+score
print()
print("Total score value :",total)
print("Average score :",total/5) 