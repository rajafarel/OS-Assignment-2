import sys

def fcfs(requests, start_position):
    head_movements = 0
    current_position = start_position
    for req in requests:
        head_movements += abs(req - current_position)
        current_position = req
    return head_movements

def scan(requests, start_position, max_cylinders):
    requests.sort()
    head_movements = 0
    current_position = start_position
    direction = -1  # -1 for down, 1 for up

    while requests:
        if current_position in requests:
            requests.remove(current_position)
        if current_position == 0 or current_position == max_cylinders - 1:
            direction *= -1
        current_position += direction
        head_movements += 1

    return head_movements

def c_scan(requests, start_position, max_cylinders):
    requests.sort()
    head_movements = 0
    current_position = start_position

    for req in requests:
        if req >= current_position:
            head_movements += req - current_position
            current_position = req

    head_movements += (max_cylinders - 1) - current_position
    head_movements += max_cylinders - 1
    current_position = 0

    for req in requests:
        if req < start_position:
            head_movements += req - current_position
            current_position = req

    return head_movements

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py [start_position] requests.txt")
        return

    start_position = int(sys.argv[1])
    file_name = sys.argv[2]

    try:
        with open(file_name, 'r') as file:
            requests = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print("File not found.")
        return

    max_cylinders = 5000

    print("Task 1:")
    print("FCFS Head Movements:", fcfs(requests.copy(), start_position))
    print("SCAN Head Movements:", scan(requests.copy(), start_position, max_cylinders))
    print("C-SCAN Head Movements:", c_scan(requests.copy(), start_position, max_cylinders))

    print("\nTask 2:")
    unique_sorted_requests = sorted(set(requests))
    print("FCFS Head Movements:", fcfs(unique_sorted_requests, start_position))
    print("SCAN Head Movements:", scan(unique_sorted_requests, start_position, max_cylinders))
    print("C-SCAN Head Movements:", c_scan(unique_sorted_requests, start_position, max_cylinders))

if __name__ == "__main__":
    main()
