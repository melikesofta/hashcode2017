import sys

input_file = open(sys.argv[1])
vars_from_file = lambda: [int(x) for x in input_file.readline().split()]

V, E, R, C, X = vars_from_file()
Vsizes = vars_from_file()

assert V == len(Vsizes), "%d != %s"%(V, Vsizes)  # Number of cache servers

latencies = {}
for endpoint_id in range(E):
    datacenter_latency, number_of_caches = vars_from_file()
    for cache in range(number_of_caches):
        cache_id, cache_latency = vars_from_file()
        pass

for request in range(R):
    video_id, endpoint_id, number_of_requests = vars_from_file()


# Check if all values are used
eof = input_file.readline()
assert not eof, "I got: `%s`"%eof
print(C)
for i in range(C):
    print( "%d %d"%(i,i))