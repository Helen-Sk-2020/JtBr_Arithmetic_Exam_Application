# import time
#
# current_time = time.gmtime()
# action = "to feed the cat"
#
# current_time = time.asctime(time.gmtime())
#
# current_time = time.strftime('%H:%M', time.gmtime())
# current_time = time.strftime("%H:%M", time.localtime())
# print(f"It's {current_time}. Time {action}.")
#
# action2 = "to feed the dog"
#
# time.sleep(5)  # NB! the time to wait is given in seconds
#
# current_time = time.strftime("%H:%M", time.localtime())
#
# print(f"It's {current_time}. Time {action2}.")
#
# print(time.asctime())
# print(time.ctime())
# print(time.gmtime(0))
# print(time.time())
# start = time.perf_counter()
#
# print("Oh no! The cat's breaking his diet!")
#
# end = time.perf_counter()
# total_time = end - start
#
# print(f"Your program has executed for {total_time} seconds.")
import time

print(time.timezone / 3600)
print(time.tzname)
print(time.daylight)