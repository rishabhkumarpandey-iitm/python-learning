empty_list = []
empty_set = set()
empty_tuple = ()

print(empty_list)
print(empty_set, type(empty_set))
print(empty_tuple, type(empty_tuple))


singleton_list = [1]
singleton_set = {1}
singleton_tuple =(1,)

print(singleton_list, type(singleton_list))
print(singleton_set, type(singleton_set))
print(singleton_tuple, type(singleton_tuple))


print(bool(empty_list))
print(bool(singleton_list))




int_iterable = range(1,10,3)
print(list(int_iterable), type(int_iterable))
print(type(min(list(int_iterable))))

print(sum(list(int_iterable)))

print(sorted(list(int_iterable), reverse=True))

int_iterable = [4,2,4,6,7,3,-2,3]
if type(int_iterable)!='tuple':
    
