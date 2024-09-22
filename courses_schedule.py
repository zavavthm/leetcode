from collections import deque, defaultdict
from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # Create an adjacency list and an in-degree count
    adj_list = defaultdict(list)
    in_degree = [0] * num_courses

    # Build the graph
    for dest, src in prerequisites:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    # Initialize a queue with all courses having zero in-degree
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])

    visited_courses = 0

    # Process nodes with zero in-degree
    while queue:
        node = queue.popleft()
        visited_courses += 1
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if we visited all courses
    return visited_courses == num_courses