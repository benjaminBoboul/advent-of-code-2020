#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from os.path import isfile, isdir
from os import mkdir
import logging

tmpdir = "tmp"


def get_session_id():
    with open("secrets.txt") as f:
        session_id: str = f.read()
    f.close()
    return session_id


def assert_tmp_dir_exists() -> None:
    if not isdir(tmpdir):
        mkdir(tmpdir)


def check_inputs_is_cached(day: int) -> bool:
    assert_tmp_dir_exists()
    return isfile("%s/%d.txt" % (tmpdir, day))


def fetch_challenge_input(day: int, session_id: str = get_session_id()):
    if not check_inputs_is_cached(day):
        request = get(f"https://adventofcode.com/2020/day/{day}/input", cookies={"session": session_id})
        request.raise_for_status()
        with open("%s/%d.txt" % (tmpdir, day), 'w') as f:
            f.writelines(request.text)
        f.close()

    logging.debug("Inputs is cached")
    with open("%s/%d.txt" % (tmpdir, day)) as f:
        inputs = f.read().splitlines()
    f.close()

    return inputs


if __name__ == '__main__':
    fetch_challenge_input(1)
