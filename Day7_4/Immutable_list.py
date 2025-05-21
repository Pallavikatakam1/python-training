count=10
def update_count():
    global count
    count += 1
print("Before update count: ", count)
update_count()
print("After update count: ", count)