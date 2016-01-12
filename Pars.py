# coding: utf-8

import argparse


def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', required=True)
    parser.add_argument('-sr', required=True)
    parser.add_argument('-f', action='store_true', default=False)

    return parser
