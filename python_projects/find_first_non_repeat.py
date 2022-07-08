
n = 'aaabcccdfffsddmmc'
def find_first_repeat(n):
  index = {}
  slist = []
  tn = 0
  ph = n[0]
  for i in n:
    if ph != i and i in index:
      tn = index[i]
    elif ph != i:
      tn = 0
    if i not in index:
      slist.append(i)
    tn = tn + 1
    index[i] = tn
    ph = i

  for answer in slist:
    if index[answer] == 1:
      return answer

print(find_first_repeat(n))