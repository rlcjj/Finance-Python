# -*- coding: utf-8 -*-
u"""
Created on 2015-10-22

@author: cheng.li
"""

import copy
from PyFin.Analysis.SecurityValueHolders import SecurityValueHolder
from PyFin.Math.Accumulators import Latest
from PyFin.Math.Accumulators import XAverage
from PyFin.Math.Accumulators import MACD


class SecurityStatelessSingleValueHolder(SecurityValueHolder):
    def __init__(self, holderType, dependency='x', symbolList=None, **kwargs):
        super(SecurityStatelessSingleValueHolder, self).__init__(dependency, symbolList)

        if isinstance(dependency, SecurityValueHolder):
            self._symbolList = dependency.symbolList
            self._dependency = dependency._dependency
            self._innerHolders = \
                {
                    name: holderType(dependency=copy.deepcopy(dependency.holders[name]), **kwargs) for name in self._symbolList
                    }

        else:
            self._innerHolders = \
                {
                    name: holderType(dependency=self._dependency, **kwargs) for name in self._symbolList
                    }


class SecurityLatestValueHolder(SecurityStatelessSingleValueHolder):
    def __init__(self, dependency='x', symbolList=None):
        super(SecurityLatestValueHolder, self).__init__(holderType=Latest,
                                                        dependency=dependency,
                                                        symbolList=symbolList)


class SecurityXAverageValueHolder(SecurityStatelessSingleValueHolder):
    def __init__(self, window, dependency='x', symbolList=None):
        super(SecurityXAverageValueHolder, self).__init__(holderType=XAverage,
                                                          dependency=dependency,
                                                          symbolList=symbolList,
                                                          window=window)


class SecurityMACDValueHolder(SecurityStatelessSingleValueHolder):
    def __init__(self, short, long, dependency='x', symbolList=None):
        super(SecurityMACDValueHolder, self).__init__(holderType=MACD,
                                                      dependency=dependency,
                                                      symbolList=symbolList,
                                                      short=short,
                                                      long=long)

