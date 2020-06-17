#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For command line execution.
Todo:
    * create test comand line.
    * create build for ci tool(goal).
    * create function to open fbx files.
    * create function to get object list.
"""
import os
import subprocess

import click

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
MAYA_SCRIPTS_PATH = os.path.join(SCRIPT_PATH, "maya")


@click.group()
def cmd():
    pass


@cmd.command()
def get_object_list():
    test_command = os.path.join(MAYA_SCRIPTS_PATH, "get_object_list.py")
    subprocess.call(['mayapy', test_command])


@cmd.command()
def change_soft_edge():
    test_command = os.path.join(MAYA_SCRIPTS_PATH, "change_soft_edge.py")
    subprocess.call(['mayapy', test_command])
    # print(result)
    # subprocess.Popen(["mayabach", "-command", "{}".format(exec_file)])
    #click.echo("all object soft edges.")


def main():
    cmd()


if __name__ == "__main__":
    main()


"pipenv run python -m mayapot get-object-list"