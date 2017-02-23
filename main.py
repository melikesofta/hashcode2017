import sys

input_file = open(sys.argv[1])
vars_from_file = lambda: [int(x) for x in input_file.readline().split()]

V, E, R, C, X = vars_from_file()
Vsizes = vars_from_file()

assert V == len(Vsizes), "%d != %s" % (V, Vsizes)  # Number of cache servers
cache_sizes = [X] * C
cache_latencies = {}
datacenter_latencies = {}

for endpoint_id in range(E):
    datacenter_latency, number_of_caches = vars_from_file()
    datacenter_latencies[endpoint_id] = datacenter_latency
    for cache in range(number_of_caches):
        cache_id, cache_latency = vars_from_file()

        cache_latencies[(cache_id, endpoint_id)] = cache_latency


def get_cache_latency(cache_id, endpoint_id):
    return cache_latencies.get((cache_id, endpoint_id), None)
    # eger None'sa baglanti yok


def get_datacenter_latency(endpoint_id):
    r = datacenter_latencies.get(endpoint_id, None)
    assert r is not None, "Oup"
    return r
    # eger none geliyorsa bi yerde hata yapilmis


endpoint_video_requests = {}
for request in range(R):
    video_id, endpoint_id, number_of_requests = vars_from_file()
    endpoint_video_requests[(video_id, endpoint_id)] = number_of_requests


def get_endpoint_video_requests(video_id, endpoint_id):
    return endpoint_video_requests.get([video_id, endpoint_id], 0)


videos_and_caches = {}


def add_video_to_cache(cache_id, video_id):
    videos_and_caches.setdefault(cache_id, [])
    if video_id in videos_and_caches[cache_id]:
        raise Exception("Video already added")
    cache_sizes[cache_id] -= Vsizes[video_id]
    assert  cache_sizes[cache_id] >= 0, "There is no enough space on cache"
    videos_and_caches[cache_id] += [video_id]

def generate_output():
    print(len(list(videos_and_caches.keys())))
    for cache, videos in  videos_and_caches.items():
        print("%d %s"%(cache, " ".join([str(v) for v in videos])))

# Check if all values are used
eof = input_file.readline()
assert not eof, "I got: `%s`" % eof
# CODE HERE

add_video_to_cache(1,1)
add_video_to_cache(1,2)
add_video_to_cache(1,3)
add_video_to_cache(2,1)


generate_output()