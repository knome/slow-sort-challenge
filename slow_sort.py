import time

g_picks     = 0
g_rotations = 0
g_swaps     = 0

def swap_adjacent( numbers, at ):
    numbers[at    ] ^= numbers[at + 1]
    numbers[at + 1] ^= numbers[at    ]
    numbers[at    ] ^= numbers[at + 1]
    global g_swaps
    g_swaps += 1

def rotate_segment( numbers, start ):
    for ii in range( len( numbers[ start : ] ) - 1 ):
        swap_adjacent( numbers, start + ii )
    global g_rotations
    g_rotations += 1

def slow_sort(numbers: list) -> None:
    at = 0
    while at < len( numbers ):
        nn = len( numbers ) - at - 1
        ii = 0
        while ii < nn:
            if numbers[at] > numbers[at + 1]:
                global g_picks
                g_picks += 1
                swap_adjacent( numbers, at )
            rotate_segment( numbers, at + 1 )
            ii += 1
        at += 1

def main() -> None:
    # Uncomment the following line to read from a file.
    
    input_file = open('numbers1000.txt', 'r')
    input = input_file.readline
    
    size = int(input())
    numbers = [0] * size
    
    for i in range(size):
        numbers[i] = int(input())
    
    slow_sort(numbers)
    
    with open(f'output{size}.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number}\n')

if __name__ == '__main__':
    start_time = time.time_ns() / 1000000
    main()    
    end_time = time.time_ns() / 1000000
    
    print(f'Elapsed time: {end_time - start_time} milliseconds.')
    print(f'gPicks={g_picks} gRotations={g_rotations} gSwaps={g_swaps}' )
