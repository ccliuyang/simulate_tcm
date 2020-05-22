# -*- coding: utf-8 -*-
import os
from enum import Enum
import abc
from six import with_metaclass

class Air(Enum):
    """
    六气
    """
    Air_Wind    = "风",
    Air_Hot     = "热",
    Air_Summer  = "暑",
    Air_Damp    = "湿",
    Air_Dry     = "燥",
    Air_Cold    = "寒"

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

class Gallbladder(AbstractOrgan):
    """
    胆囊
    """
    def __init__(self):
        pass


class Stomach(AbstractOrgan):
    """
    胃
    """
    def __init__(self):
        pass

class LargeIntestine(AbstractOrgan):
    """
    大肠
    """
    def __init__(self):
        pass

class LittleIntestine(AbstractOrgan):
    """
    小肠
    """
    def __init__(self):
        pass


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
        self._lung      = Lung()    # 肺脏
        self._heart     = Heart()   # 心脏
        self._kidney    = Kidney()  # 肾脏
        self._spleen    = Spleen()  # 脾脏
        self._hepatic   = Hepatic() # 肝脏


    def treat(self, medician):
        """
        治疗
        """
        pass

    def score(self):
        return self._score
    

