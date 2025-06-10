def appearance(intervals: dict[str, list[int]]) -> int:
    def merge_intervals(times: list[int]) -> list[tuple[int, int]]:
        return [(times[i], times[i + 1]) for i in range(0, len(times), 2)]

    def intersect(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
        start = max(a[0], b[0])
        end = min(a[1], b[1])
        if start < end:
            return (start, end)
        return None

    lesson = (intervals['lesson'][0], intervals['lesson'][1])
    pupil_times = merge_intervals(intervals['pupil'])
    tutor_times = merge_intervals(intervals['tutor'])

    timeline = []
    for p in pupil_times:
        for t in tutor_times:
            overlap = intersect(p, t)
            if overlap:
                overlap = intersect(overlap, lesson)
                if overlap:
                    timeline.append(overlap)

    timeline.sort()
    merged = []
    for start, end in timeline:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return sum(end - start for start, end in merged)
