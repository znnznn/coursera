stud = [{input() for j in range(int(input()))} for i in range(int(input()))]
k_by_everyone, k_by_someone = set.intersection(*stud), set.union(*stud)
print(len(k_by_everyone), *sorted(k_by_everyone), sep='\n')
print(len(k_by_someone), *sorted(k_by_someone), sep='\n')
