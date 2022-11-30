#swaping two list.
#we have two list a and b of n integers.
#we need to return the value so that max(a)*max(b) is minimum of all other possible combinations.

#here is the solution of the code.
def minmax(a,b):
  for i in range(a,b):
    if a[i] < b[i]:
      a[i], b[i] = b[i], a[i]
  return max(a)*max(b)

    