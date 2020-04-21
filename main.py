# -*- coding: utf-8 -*-

from enum import Enum
from human import Human


if __name__ == "__main__":
    patient = Human()
    print('治疗前: score = ', patient.score())

    print('治疗后: score = ', patient.score())
    
    
