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
    return endpoint_video_requests.get((video_id, endpoint_id), 0)


videos_and_caches = {}


def add_video_to_cache(cache_id, video_id):
    videos_and_caches.setdefault(cache_id, [])
    if video_id in videos_and_caches[cache_id]:
        raise Exception("Video already added")
    cache_sizes[cache_id] -= Vsizes[video_id]
    assert cache_sizes[cache_id] >= 0, "There is no enough space on cache"
    videos_and_caches[cache_id] += [video_id]


def can_add_video_to_cache(cache_id, video_id):
    videos = videos_and_caches.get(cache_id, [])
    if video_id in videos:
        return False
    if cache_sizes[cache_id] < Vsizes[video_id]:
        return False
    return True


def generate_output():
    print(len(list(videos_and_caches.keys())))
    for cache, videos in videos_and_caches.items():
        print("%d %s" % (cache, " ".join([str(v) for v in videos])))


# Check if all values are used
eof = input_file.readline()
assert not eof, "I got: `%s`" % eof
# CODE HERE

# for video_id in range(V):
#     for cache_id in range(C):
#         if can_add_video_to_cache(cache_id, video_id):
#             add_video_to_cache(cache_id, video_id)
#             break
add_videos = [] # [cache_id, video_id]
for cache_id in range(C):
    requests  = []
    for endpoint_id in range(E):
        if get_cache_latency(cache_id, endpoint_id) is not None:
            for video_id in range(V):
                number_of_requests = get_endpoint_video_requests(video_id, endpoint_id)
                if number_of_requests:
                    requests.append([video_id, number_of_requests])
    requests = sorted(requests,reverse=True, key=lambda x: x[1])
    requests = [t[0] for t in requests]
    for video_id in requests:
        add_videos.append([cache_id, video_id])
        #if can_add_video_to_cache(cache_id, video_id):
        #    add_video_to_cache(cache_id, video_id)
add_videos = sorted(add_videos, reverse=True, key=lambda x: x[1])
for endpoint_id in range(E):
    # go over add_videos
    video = -1
    for [cache_id, video_id] in add_videos:
        # if that endpoint requests that video
        if get_endpoint_video_requests(video_id, endpoint_id) and video_id != video:
            if can_add_video_to_cache(cache_id, video_id):
                add_video_to_cache(cache_id, video_id)
                video = video_id

generate_output()
