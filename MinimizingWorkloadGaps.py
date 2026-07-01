def find_smallest_gap(work_sessions):
    n = len(work_sessions)
    if n < 2:
        return 0
    sessions = sorted(work_sessions)
    minGap = float("inf")
    for i in range(1, n):
        prevEnd = sessions[i - 1][1]
        currStart = sessions[i][0]
        prevEnd = (prevEnd // 100) * 60 + (prevEnd % 100)
        currStart = (currStart // 100) * 60 + (currStart % 100)
        gap = currStart - prevEnd
        if gap < minGap:
            minGap = gap
    return minGap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))