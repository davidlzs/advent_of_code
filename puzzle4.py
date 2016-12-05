def split_encryped_name(encrypted_name):
    encrypted_name = encrypted_name.strip()
    idx_open_open_bracket = encrypted_name.index('[')
    name_id = encrypted_name[:idx_open_open_bracket]
    idx_name_id_sep = name_id.rfind('-')
    name = name_id[:idx_name_id_sep]
    sector_id = int(name_id[(idx_name_id_sep + 1):])
    checksum = encrypted_name[idx_open_open_bracket+1:-1]
    return (name, sector_id, checksum)
def calc_checksum(name):
    name_parts = name.split('-')
    name = ''.join(name_parts)
    char_dict = {}
    for c in name:
        char_dict[c] = char_dict.setdefault(c, 0) + 1
    t = [(k,v) for k,v in char_dict.items()]
    print(t)
    s = sorted(t, key=lambda v: (-v[1], v[0]))
    return ''.join([c[0] for c in s])[:5]

ord_a = ord('a')
ord_z = ord('z')
def shift_char(c, times):
    times = times % 26
    ord_c = ord(c) + times
    if ord_c > ord_z:
        ord_c = ord_c - 26
    return chr(ord_c)

def decrypt(name_sector_id):
    shift_times = name_sector_id[1] % 26
    decrypted = []
    for c in name_sector_id[0]:
        if c == '-':
            decrypted.append(' ')
        else:
            decrypted.append(shift_char(c, shift_times))
    return ''.join(decrypted)


with open('puzzle4_input.txt') as f:
    content = f.readlines()
    real_rooms = []
    sum_sector_ids = 0
    for line in content:
        print(line)
        (name, sector_id, checksum) = split_encryped_name(line)
        print(calc_checksum(name))
        if calc_checksum(name) == checksum:
            sum_sector_ids = sum_sector_ids + sector_id
            real_rooms.append((name, sector_id))
    print("Sum of sector ids for real rooms", sum_sector_ids)
    found = None
    for r in real_rooms:
        real_name = decrypt(r)
        if real_name.find('northpole') >= 0:
            found = real_name
            print(real_name, r)
            break;
        


