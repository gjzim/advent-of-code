with open("input.txt") as f:
    data = f.read().strip()

blocks = list(map(int, data))

def fill_disk():
    disk = []
    for i, size in enumerate(blocks):
        is_data_block = (i % 2) == 0
        block_id = i // 2
        while size:
            disk.append(str(block_id) if is_data_block else ".")
            size -= 1
    return disk

def compact_disk_by_block():
    disk = fill_disk()
    left, right = 0, len(disk) - 1
    while left < right:
        while disk[left] != '.' and left < right:
            left += 1
        while disk[right] == '.' and left < right:
            right -= 1

        disk[left], disk[right] = disk[right], disk[left]
        left += 1
        right -= 1
    return disk

def calculate_checksum(disk):
    return sum(i * int(disk[i]) for i in range(len(disk)) if disk[i] != '.')

def compact_disk_by_file():
    def calculate_range_sum(start, length):
        end = start + length - 1
        return (start + end) * length // 2

    checksum = 0
    free_spaces = {} # { index: (block_index, length) }
    file_positions = {} # { index: block_index }
    index, block_index = 1, 0

    # Store free spaces and file positions
    while index < len(blocks):
        file_positions[index - 1] = block_index
        file_length = blocks[index - 1]
        block_index += file_length

        free_space_length = blocks[index]
        free_spaces[index] = (block_index, free_space_length)
        block_index += free_space_length

        index += 2

    # Move files from the end
    index = len(blocks) - 1

    # We can not move the first file anywhere to its left,
    # so it's not necessary process index 0.
    while index > 1:
        file_id = index // 2
        file_size = blocks[index]
        moved = False

        for key, (block_index, space) in free_spaces.items():
            # File is moved, update the checksum based on its updated position which is the starting
            # position of the empty space
            if space >= file_size:
                checksum += calculate_range_sum(block_index, file_size) * file_id

                space -= file_size
                if space == 0:
                    del free_spaces[key]
                else:
                    free_spaces[key] = (block_index + file_size, space)
                moved = True
                break

        # If the file is not moved, add it's checksum based on its previous position
        if not moved:
            checksum += calculate_range_sum(file_positions[index], file_size) * file_id

        # We can only move a file to its left and try only once. So, the space that's left to it
        # can not ever be used by other files again. so delete them from the free space array
        if index - 1 in free_spaces:
            del free_spaces[index - 1]

        index -= 2

    return checksum

solution1 = calculate_checksum(compact_disk_by_block())
solution2 = compact_disk_by_file()
print(solution1)
print(solution2)