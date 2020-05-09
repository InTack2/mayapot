#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" For command line execution.
Todo:
    * create test comand line.
    * create build for ci tool(goal).
    * create function to open fbx files.
    * create function to get object list.
"""
import click


@click.group()
def cmd():
    pass


@cmd.command()
def get_object_list():
    click.echo("maya ls command.")


@cmd.command()
def change_soft_edge():
    click.echo("all object soft edges.")


def main():
    cmd()


if __name__ == "__main__":
    main()
