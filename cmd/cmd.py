import os
from datetime import timedelta, datetime
from typing import List


def commit(date: str):
    os.system(f'GIT_COMMITTER_DATE={date} git commit -m "auto commit" --date={date}')


def add_file(n: int):
    with open('autocommit.log', 'w') as fp:
        fp.write(f'{n}')
    os.system(f'git add autocommit.log')


def run(timestamp: datetime, mark: List[int], path: str, base: int):
    os.chdir(path)
    for i in range(len(mark)):
        if mark[i] == 1:
            t = timestamp + timedelta(days=i)
            for j in range(base):
                add_file(j)
                commit(t.strftime("%Y-%m-%dT%H:%M:%S"))


if __name__ == '__main__':
    run(datetime(2020, 10, 4, 8), [
        1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 1, 1, 1,
    ], '/Users/edz/workspace/codes/github/beauty-committer/ignore', 30)
