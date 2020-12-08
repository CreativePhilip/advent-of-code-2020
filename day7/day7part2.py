import pprint


TARGET_BAG = "shiny gold"


def parse_rule(rule: str):
    rule = rule.strip().replace(".", "").replace(" bag", "")
    count = rule[:rule.find(" ")]
    bag_color = rule[rule.find(" "):].strip()

    if bag_color[-1] == "s":
        bag_color = bag_color[:-1]

    return {"color": bag_color, "valid_count": int(count)}


def parse_rules(arr: list[str]):
    all_rules = {}
    for r in arr:

        color: str
        color, remaining = r.split("contain")
        color = color.strip().replace(" bags", "")

        all_rules.update({color: []})

        count_rules = remaining.split(", ")
        if len(count_rules) > 1:
            for i in count_rules:
                all_rules[color].append(parse_rule(i))
        else:
            rule: str = count_rules[0].strip()
            if "no other bags" in rule:
                all_rules[color] = None
            else:
                all_rules[color].append(parse_rule(rule))
    return all_rules


def solve(arr: dict):
    ans = []
    for node in arr.keys():
        discovered = [node]
        q = [node]

        while len(q) != 0:
            v = q.pop(0)
            if v == TARGET_BAG:
                ans.append(discovered)
                break
            if arr[v] is not None:
                for edge in arr[v]:
                    if edge["color"] not in discovered:
                        discovered.append(edge["color"])
                        q.append(edge['color'])
    final_ans = filter(lambda x: len(x) > 1, ans)
    print(len(list(final_ans)))
    pprint.pprint(ans)


if __name__ == '__main__':
    file = open("data.txt", "r")
    rules = file.read().split(".\n")
    rules = parse_rules(rules)
    # pprint.pprint(rules)
    solve(rules)
