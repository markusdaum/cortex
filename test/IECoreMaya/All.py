##########################################################################
#
#  Copyright (c) 2008-2009, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import warnings
warnings.filterwarnings( "error", "Access to Parameters as attributes is deprecated - please use item style access instead.", DeprecationWarning )
warnings.filterwarnings( "error", "Access to CompoundObject children as attributes is deprecated - please use item style access instead.", DeprecationWarning )
warnings.filterwarnings( "error", "Access to CompoundParameter children as attributes is deprecated - please use item style access instead.", DeprecationWarning )
warnings.filterwarnings( "error", "Specifying presets as a dictionary is deprecated - pass a tuple of tuples instead.", DeprecationWarning )

import unittest

from ConverterHolder import *
from PlaybackFrameList import *
from ParameterisedHolder import *
from FromMayaCurveConverterTest import *
from PluginLoadUnload import *
from NamespacePollution import *
from FromMayaMeshConverterTest import *
from FromMayaParticleConverterTest import *
from FromMayaPlugConverterTest import *
from FromMayaUnitPlugConverterTest import *
from FromMayaGroupConverterTest import *
from FromMayaCameraConverterTest import *
from FromMayaConverterTest import *
from FromMayaObjectConverterTest import *
from FnParameterisedHolderTest import *
from ToMayaPlugConverterTest import *
from ToMayaMeshConverterTest import *
from MayaTypeIdTest import *
from FromMayaTransformConverterTest import *
from CallbackIdTest import *
from TemporaryAttributeValuesTest import *
from SplineParameterHandlerTest import *

import MayaUnitTest

if __name__ == "__main__":
	MayaUnitTest.TestProgram()
