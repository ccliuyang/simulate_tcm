# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()
import click

from simulate_tcm.human import Human


@click.group()
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(ctx, verbose):
    ctx.obj["VERBOSE"] = verbose


@cli.command()
@click.option('-p', '--port', 'port', type=click.INT, default=5000)
@click.option('-r', 'autoreload', is_flag=True, default=False)
@click.option('--debug/--no-debug', 'debug', is_flag=True, default=True)
def run(**kwargs):
    pass


def entry_point():
    cli(obj={})


if __name__ == '__main__':
    entry_point()

    patient = Human()
    print('治疗前: score = ', patient.score())

    print('治疗后: score = ', patient.score())
    
    
