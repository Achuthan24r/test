mark={
    "math":0,
    "science":0,
    "english":0,
    "computer science":0
}
for subject in mark:
mark[subject]=float(input(f"enter mark for{subject}:"))
total_mark=sum(mark.values())
print(f"total mark:{total_mark}/{len(mark)*100}")
precentage=(total_marh/(len(mark)*100))*100
print(f"precentage:{precentage:.2f}%")