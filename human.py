# -*- coding: utf-8 -*-
import os
from enum import Enum
import abc
from six import with_metaclass


class FivePhases(Enum):
    PHASE_JIN   = "金",
    PHASE_MU    = "木",
    PHASE_SHUI  = "水",
    PHASE_HUO   = "火",
    PHASE_TU    = "土"

class Pulse(Enum):
    PLUSE_FU = "脉浮",
    PLUSE_CHEN = "脉沉",
    

class AbstractOrgan(with_metaclass(abc.ABCMeta)):
    """
    脏器
    """
    @abc.abstractproperty
    def five_phases(self):
        """
        [Required]
        返回当前脏器的五行属性
        """
        raise NotImplementedError



class Hepatic(AbstractOrgan):
    """
    肝脏
    """
    def __init__(self):
        pass

    def five_phases(self):
        return FivePhases.PHASE_MU


class Spleen(AbstractOrgan):
    """
    脾脏
    """
    def __init__(self):
        pass

    def five_phases(self):
        return FivePhases.PHASE_TU

class Kidney(AbstractOrgan):
    """
    肾脏
    """
    def __init__(self):
        pass

    def five_phases(self):
        return FivePhases.PHASE_SHUI

class Heart(AbstractOrgan):
    """
    心脏
    """
    def __init__(self):
        pass

    def five_phases(self):
        return FivePhases.PHASE_HUO


class Lung(AbstractOrgan):
    """
    肺脏
    """
    def __init__(self):
        pass

    def five_phases(self):
        return FivePhases.PHASE_JIN


class Human(object):
    def __init__(self):
        self._score = 100   #健康指数，满分100分
        self._lung      = Lung()
        self._heart     = Heart()
        self._kidney    = Kidney()
        self._spleen    = Spleen()
        self._hepatic   = Hepatic()

    def treat(self, medician):
        """
        治疗
        """
        pass

    def score(self):
        return self._score
    

