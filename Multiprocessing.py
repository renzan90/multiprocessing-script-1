import time
import multiprocessing
start=time.perf_counter()
def do_something():
	print('Sleeping for 5 seconds')
	time.sleep(5)
	print('Done sleeping')


p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something) 
p1.start()
p2.start()
finish=time.perf_counter()
print(f'Finished in {round(finish-start)} seconds')

# Finished in 0 seconds	: This actually happens in 1 second, however, it shows 0 seconds because, while
# p1.start()	:<----
#  						: while these two processes were sleeping, the "start=time.perf_counter()" began and ended at "finish=time.perf_counter()"
# p2.start()	:<----

#And then the sleep process within p1.start() and p2.start() ends. 

# Finished in 0 seconds	: These messages appear simultaneously since their respective functions get executed at the same time.
# Sleeping in 1 second
# Sleeping in 1 second

#End result:
# Finished in 0 seconds
# Sleeping in 1 second
# Sleeping in 1 second
# Done sleeping
# Done sleeping