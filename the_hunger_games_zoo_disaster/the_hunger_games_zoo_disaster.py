# -*- coding: utf-8 -*-

def who_eats_who(zoo):
    # Your code here
    # menu = ['antelope eats grass', 'big-fish eats little-fish', 'bug eats leaves', 'bear eats big-fish',
    #         'bear eats bug', 'bear eats chicken', 'bear eats cow', 'bear eats leaves', 'bear eats sheep',
    #         'chicken eats bug', 'cow eats grass', 'fox eats chicken', 'fox eats sheep', 'giraffe eats leaves',
    #         'lion eats antelope', 'lion eats cow', 'panda eats leaves', 'sheep eats grass']
    # eat = dict()
    # for j in map(lambda s: s.split(' eats '), menu):
    #     eat.setdefault(j[0], set()).add(j[1])

    eat = {
        'antelope': {'grass'}, 'big-fish': {'little-fish'}, 'bug': {'leaves'},
        'bear': {'sheep', 'chicken', 'leaves', 'cow', 'big-fish', 'bug'}, 'chicken': {'bug'}, 'cow': {'grass'},
        'fox': {'sheep', 'chicken'}, 'giraffe': {'leaves'}, 'lion': {'cow', 'antelope'}, 'panda': {'leaves'},
        'sheep': {'grass'}
    }

    story = [zoo, ]
    who_eat = '%s eats %s'
    animals_list = zoo.split(',')

    feeding_time = True
    while feeding_time:
        zoo_len = len(animals_list) - 1
        for index, subject in enumerate(animals_list):
            treats = eat.get(subject)
            if treats is None:
                continue
            # print(treats, subject, index, zoo_len, story)
            hungry = True

            hunted = None
            if index > 0:
                hunted = animals_list[index - 1]
            if hunted in treats:
                del animals_list[index - 1]
                hungry = False
            else:
                if index < zoo_len:
                    hunted = animals_list[index + 1]
                if hunted in treats:
                    del animals_list[index + 1]
                    hungry = False
            if not hungry:
                story.append(who_eat % (subject, hunted))
                break
        else:
            break
    story.append(','.join(animals_list))

    return story


if __name__ == '__main__':
    zoo = "fox,bug,chicken,grass,sheep"
    story = who_eats_who(zoo)
    print(story)
