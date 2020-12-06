import pprint


def count_unique(arr: list[str]) -> int:
    unique_ans = set()
    for person in arr:
        for ans in person:
            unique_ans.add(ans)
    return len(unique_ans)


def count_unique_all(arr: list[str]) -> int:
    all_unique = {}
    people = len(arr)
    valid_questions = set()

    for person in arr:
        for ans in person:
            if ans in all_unique:
                all_unique[ans] += 1
            else:
                all_unique.update({ans: 1})

    for k, v in all_unique.items():
        if v == people:
            valid_questions.add(k)

    return valid_questions.__len__()


file = open("data.txt", "r")

groups = file.read().split("\n\n")
groups = [i.split("\n") for i in groups]

answer = sum(count_unique(g) for g in groups)
answer2 = sum(count_unique_all(g) for g in groups)

print(answer, answer2)
