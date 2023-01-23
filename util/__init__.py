from glob import glob
import re


def read_str(file, encoding="latin1", as_whole=False):
    with open(file, encoding=encoding) as f:
        if as_whole:
            return f.read()
        return [x.strip() for x in f.readlines()]


def prepare_text_from_uspto(folder):
    start = 0
    xml = glob(folder + "/*.xml")[0]
    begin = 0
    end = 30
    for r in read_str(xml):
        if "<claims-pages>" in r:
            start = 1
        if "</claims-pages>" in r:
            break
        if start:
            if "begin" in r:
                begin = int(re.findall(r"\d+", r)[0])
            if "end" in r:
                end = int(re.findall(r"\d+", r)[0])
    claim_pages = range(begin - 1, end)
    files = []
    for page in claim_pages:
        for f in glob(folder + "/*.txt"):
            if f.endswith(f"{page}.txt"):
                files.append(f)

    data = []
    for f in files:
        data.extend(read_str(f))
