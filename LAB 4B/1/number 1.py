
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. Elements in A and B
print(len(A | B))


print(len(B - (A | C)))

print({'h', 'i', 'j', 'k'})  # i
print({'c', 'd', 'f'})  # ii
print({'b', 'c', 'h'})  # iii
print({'d', 'f'})  # iv
print({'c'})  # v
print({'l', 'm', 'o'})  # vi