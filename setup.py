# -*- coding: utf-8 -*-

from setuptools import (
    Extension,
    find_packages,
    setup,
)

setup(
    name='simulate_tcm',
    version = '0.0.1',
    description='',
    author='liuyang',
    author_email='416954509@qq.com',
    license='MIT',
    entry_points={
        'console_scripts':[
            "simulate_tcm = simulate_tcm.__main__:entry_point",
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
