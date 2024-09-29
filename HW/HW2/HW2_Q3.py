# import time

# num_digit_max = 9
# iteration_max = 1


# for num_digit in range(num_digit_max):
#     size = 1 * 10 ** num_digit
#     front_add_time, middle_add_time, end_add_time = 0, 0, 0
#     front_del_time, middle_del_time, end_del_time = 0, 0, 0

#     for _ in range(iteration_max):
#         lst = []
#         start = time.time()
#         for _ in range(size):
#             lst.insert(0, 0)
#         front_add_time += (time.time() - start) / size / iteration_max

#         lst = []
#         start = time.time()
#         for _ in range(size):
#             lst.insert(len(lst)//2, 0)
#         middle_add_time += (time.time() - start) / size / iteration_max

#         lst = []
#         start = time.time()
#         for _ in range(size):
#             lst.append(0)
#         end_add_time += (time.time() - start) / size / iteration_max

#         lst = [0 for _ in range(size)]
#         start = time.time()
#         for _ in range(size):
#             lst.pop(0)
#         front_del_time += (time.time() - start) / size / iteration_max

#         lst = [0 for _ in range(size)]
#         start = time.time()
#         for _ in range(size):
#             lst.pop(len(lst)//2)
#         middle_del_time += (time.time() - start) / size / iteration_max

#         lst = [0 for _ in range(size)]
#         start = time.time()
#         for _ in range(size):
#             lst.pop()
#         end_del_time += (time.time() - start) / size / iteration_max

#     print(f"Size: {size}")
#     print(f"Add Front: {front_add_time:f}s, Add Middle: {
#           middle_add_time:f}s, Add End: {end_add_time:f}s")
#     print(f"Del Front: {front_del_time:f}s, Del Middle: {
#           middle_del_time:f}s, Del End: {end_del_time:f}s")
import time
import random

# Function to add elements to the front, back, and middle of a list


def add_elements(size):
    front_times, back_times, middle_times = [], [], []

    for _ in range(10):  # Repeat 10 times to average the results
        # Add to the front
        lst = []
        start = time.time()
        for _ in range(size):
            lst.insert(0, random.randint(0, 100))  # Adding to the front
        front_times.append((time.time() - start) / size)

        # Add to the back
        lst = []
        start = time.time()
        for _ in range(size):
            lst.append(random.randint(0, 100))  # Adding to the back
        back_times.append((time.time() - start) / size)

        # Add to the middle
        lst = []
        start = time.time()
        for _ in range(size):
            # Adding to the middle
            lst.insert(len(lst)//2, random.randint(0, 100))
        middle_times.append((time.time() - start) / size)

    return sum(front_times) / 10, sum(back_times) / 10, sum(middle_times) / 10

# Function to delete elements from the front, back, and middle of a list


def delete_elements(size):
    front_times, back_times, middle_times = [], [], []

    for _ in range(10):  # Repeat 10 times to average the results
        # Delete from the front
        lst = [random.randint(0, 100) for _ in range(size)]
        start = time.time()
        for _ in range(size):
            lst.pop(0)  # Deleting from the front
        front_times.append((time.time() - start) / size)

        # Delete from the back
        lst = [random.randint(0, 100) for _ in range(size)]
        start = time.time()
        for _ in range(size):
            lst.pop()  # Deleting from the back
        back_times.append((time.time() - start) / size)

        # Delete from the middle
        lst = [random.randint(0, 100) for _ in range(size)]
        start = time.time()
        for _ in range(size):
            lst.pop(len(lst)//2)  # Deleting from the middle
        middle_times.append((time.time() - start) / size)

    return sum(front_times) / 10, sum(back_times) / 10, sum(middle_times) / 10


# Test the performance for different sizes
sizes = [1000, 10000, 100000]
for size in sizes:
    print(f"Size: {size}")

    # Adding elements
    add_front, add_back, add_middle = add_elements(size)
    print(f"Add Front: {add_front:.6f}s, Add Back: {
          add_back:.6f}s, Add Middle: {add_middle:.6f}s")

    # Deleting elements
    del_front, del_back, del_middle = delete_elements(size)
    print(f"Delete Front: {del_front:.6f}s, Delete Back: {
          del_back:.6f}s, Delete Middle: {del_middle:.6f}s")
    print("-" * 40)
