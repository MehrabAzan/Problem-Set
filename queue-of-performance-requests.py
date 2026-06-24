from collections import deque

def process_performance_requests(requests):
    sortedRequests = sorted(requests, reverse=True)
    queue = deque(sortedRequests)
    results = []
    for performance in queue:
        results.append(performance[1])
    return results

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))