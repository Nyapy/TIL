def solution(registered_list, new_id):
    d = len(new_id)
    for i, idx in enumerate(new_id):
        if '0' <= idx <= '9':
            d = i
            break

    new_id_char = new_id[:d]
    new_id_number = new_id[d:]

    if new_id in registered_list:
        if new_id[d:]:
            new_id_number = int(new_id[d:])
        else:
            new_id_number = 1

        while new_id_char + str(new_id_number) in registered_list:
            new_id_number += 1

    return new_id_char + str(new_id_number)