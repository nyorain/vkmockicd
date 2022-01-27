from reg import *
from generator import write
from cgenerator import CGeneratorOptions, COutputGenerator
from mock_icd_generator import MockICDGeneratorOptions, MockICDOutputGenerator
from vkconventions import VulkanConventions

# Copyright text prefixing all headers (list of strings).
prefixStrings = [
    '/*',
    '** Copyright (c) 2015-2018 The Khronos Group Inc.',
    '**',
    '** Licensed under the Apache License, Version 2.0 (the "License");',
    '** you may not use this file except in compliance with the License.',
    '** You may obtain a copy of the License at',
    '**',
    '**     http://www.apache.org/licenses/LICENSE-2.0',
    '**',
    '** Unless required by applicable law or agreed to in writing, software',
    '** distributed under the License is distributed on an "AS IS" BASIS,',
    '** WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.',
    '** See the License for the specific language governing permissions and',
    '** limitations under the License.',
    '*/',
    ''
]

# Text specific to Vulkan headers
vkPrefixStrings = [
    '/*',
    '** This header is generated from the Khronos Vulkan XML API Registry.',
    '**',
    '*/',
    ''
]

tree = etree.parse('vk.xml')

# generate cpp
opts = MockICDGeneratorOptions(
    conventions=VulkanConventions(),
    filename='mock_icd.cpp',
    directory='.',
    genpath=None,
    apiname='vulkan',
    profile=None,
    versions='.*',
    emitversions='.*',
    defaultExtensions='vulkan',
    addExtensions='^()$',
    removeExtensions='^()$',
    emitExtensions='.*',
    prefixText=prefixStrings + vkPrefixStrings,
    protectFeature=False,
    apicall='VKAPI_ATTR ',
    apientry='VKAPI_CALL ',
    apientryp='VKAPI_PTR *',
    alignFuncParam=48,
    expandEnumerants=False,
    helper_file_type='mock_icd_source')

errWarn = sys.stderr
diag = None
gen = MockICDOutputGenerator(errFile=errWarn, warnFile=errWarn, diagFile=diag)

reg = Registry(gen, opts)
reg.loadElementTree(tree)
reg.apiGen()

# generate header
opts.filename = 'mock_icd.h'
opts.helper_file_type = 'mock_icd_header'
gen = MockICDOutputGenerator(errFile=errWarn, warnFile=errWarn, diagFile=diag)
# 
reg = Registry(gen, opts)
reg.loadElementTree(tree)
reg.apiGen()
