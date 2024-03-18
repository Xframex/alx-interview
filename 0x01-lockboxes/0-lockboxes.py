#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    visited = set()
    visited.add(0)

    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)

