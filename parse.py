from typing import List
from glob import glob


def parse_claim(patnum, data) -> List:
    num = dict()
    i = 1
    for r in data:
        if "witness" in r.lower() and num:
            break
        if r.startswith(f"{i}. "):
            num[i] = list()
            num[i].append(r)
            i += 1
        else:
            if num:
                num[i - 1].append(r)

    if num:  # if we do find claims by numberings
        return [(patnum, k, " ".join(v)) for k, v in num.items()]
    else:
        start = 0
        claim_rows = []
        for i, r in enumerate(data):
            if "claim" in r or "desire to" in r or "secure by" in r or "is-" in r:
                claim_rows.append(i)
        res = []
        if len(claim_rows) == 0:
            return []
        for r in data[claim_rows[-1] + 1 :]:
            if not r.strip() and start == 0:
                start = 1
                continue
            if not r.strip() and start == 1:
                break
            if start:
                res.append(r)
        return [(patnum, 1, "1. " + " ".join(res))]
