seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

unused_dict = dict()

all_digits = set(range(10))


def find_num(n):
    if len(seq) > n:
        return seq[n]

    for _ in range(len(seq), n + 1):
        digits = str(seq[-1])

        possible = all_digits - set(map(int, set(digits)))

        all_possible = set()
        for k, v in unused_dict.items():
            if not set(k) - possible:
                all_possible |= v

        if all_possible:
            present = min(all_possible)
            seq.append(present)
            unused_dict[tuple(sorted(map(int, set(str(present)))))].remove(present)
            continue

        else:
            present = max(seq) + 1
            while True:
                present_str = str(present)
                for d in present_str:
                    if d in digits:
                        unused_dict.setdefault(tuple(sorted(map(int, set(present_str)))), set()).add(present)
                        break
                else:
                    seq.append(present)
                    break
                present += 1
    return seq[-1]