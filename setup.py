#!/usr/bin/env python

import platform
import sys
import os

from setuptools import setup, Extension

if sys.version_info[:2] < (2, 7):
    print('Error: stackwalker requires Python >= 2.7')
    sys.exit(1)

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

# The version of stackwalker
with open(os.path.join(ROOT, 'VERSION')) as f:
    VERSION = f.read().strip()


system, node, release, version, machine, processor = platform.uname()
common_flags = [
    '-I./breakpad/src',
    '-I./socorro-minidump-stackwalk/jsoncpp-src-0.5.0/include',
    '-I./socorro-minidump-stackwalk/jsoncpp-src-0.5.0/src/lib_json',
    '-I.',
    '-fno-builtin-memcmp',
    '-O2',
    '-fPIC',
    '-DNDEBUG',
    '-D__STDC_FORMAT_MACROS=1'
]

if system == 'Darwin':
    extra_compile_args = common_flags + [
        '-DOS_MACOSX',
        '-std=c++11'
    ]
elif system == 'Linux':
    extra_compile_args = common_flags + [
        '-pthread',
        '-Wall',
        '-DOS_LINUX',
        '-std=c++11'
    ]
else:
    sys.stderr.write("Don't know how to compile breakpad for %s!\n" % system)
    sys.exit(1)

# Module init C++ file is python version specific to avoid a big mess of #ifdef
module_init_path = 'stackwalker_ext_v{}.cc'.format(sys.version_info[:2][0])

sources = [
    # our module
    module_init_path,
    'stackwalker_ext_common.cc',
    'socorro-minidump-stackwalk/stackwalker_library.cc',
    'socorro-minidump-stackwalk/jsoncpp-src-0.5.0/src/lib_json/json_reader.cpp',
    'socorro-minidump-stackwalk/jsoncpp-src-0.5.0/src/lib_json/json_value.cpp',
    'socorro-minidump-stackwalk/jsoncpp-src-0.5.0/src/lib_json/json_writer.cpp',

    # breakpad common
    'breakpad/src/common/dwarf_cfi_to_module.cc',
    'breakpad/src/common/dwarf_cu_to_module.cc',
    'breakpad/src/common/dwarf_line_to_module.cc',
    'breakpad/src/common/dwarf_range_list_handler.cc',
    'breakpad/src/common/language.cc',
    'breakpad/src/common/long_string_dictionary.cc',
    'breakpad/src/common/md5.cc',
    'breakpad/src/common/module.cc',
    'breakpad/src/common/path_helper.cc',
    'breakpad/src/common/simple_string_dictionary.cc',
    'breakpad/src/common/string_conversion.cc',
    'breakpad/src/common/test_assembler.cc',
    'breakpad/src/common/convert_UTF.cc',
    
    # breakpad processor
    'breakpad/src/processor/basic_code_modules.cc',
    'breakpad/src/processor/basic_source_line_resolver.cc',
    'breakpad/src/processor/call_stack.cc',
    'breakpad/src/processor/cfi_frame_info.cc',
    'breakpad/src/processor/convert_old_arm64_context.cc',
    'breakpad/src/processor/disassembler_x86.cc',
    'breakpad/src/processor/dump_context.cc',
    'breakpad/src/processor/dump_object.cc',
    'breakpad/src/processor/exploitability.cc',
    'breakpad/src/processor/exploitability_linux.cc',
    'breakpad/src/processor/exploitability_win.cc',
    'breakpad/src/processor/fast_source_line_resolver.cc',
    'breakpad/src/processor/logging.cc',
    'breakpad/src/processor/microdump.cc',
    'breakpad/src/processor/microdump_processor.cc',
    'breakpad/src/processor/minidump.cc',
    'breakpad/src/processor/minidump_processor.cc',
    'breakpad/src/processor/module_comparer.cc',
    'breakpad/src/processor/module_serializer.cc',
    'breakpad/src/processor/pathname_stripper.cc',
    'breakpad/src/processor/proc_maps_linux.cc',
    'breakpad/src/processor/process_state.cc',
    'breakpad/src/processor/simple_symbol_supplier.cc',
    'breakpad/src/processor/source_line_resolver_base.cc',
    'breakpad/src/processor/stack_frame_cpu.cc',
    'breakpad/src/processor/stack_frame_symbolizer.cc',
    'breakpad/src/processor/stackwalk_common.cc',
    'breakpad/src/processor/stackwalker.cc',
    'breakpad/src/processor/stackwalker_address_list.cc',
    'breakpad/src/processor/stackwalker_amd64.cc',
    'breakpad/src/processor/stackwalker_arm.cc',
    'breakpad/src/processor/stackwalker_arm64.cc',
    'breakpad/src/processor/stackwalker_mips.cc',
    'breakpad/src/processor/stackwalker_ppc.cc',
    'breakpad/src/processor/stackwalker_ppc64.cc',
    'breakpad/src/processor/stackwalker_sparc.cc',
    'breakpad/src/processor/stackwalker_x86.cc',
    'breakpad/src/processor/symbolic_constants_win.cc',
    'breakpad/src/processor/synth_minidump.cc',
    'breakpad/src/processor/tokenize.cc'
]

libdiasm = [
    'breakpad/src/third_party/libdisasm/ia32_implicit.c',
    'breakpad/src/third_party/libdisasm/ia32_insn.c',
    'breakpad/src/third_party/libdisasm/ia32_invariant.c',
    'breakpad/src/third_party/libdisasm/ia32_modrm.c',
    'breakpad/src/third_party/libdisasm/ia32_opcode_tables.c',
    'breakpad/src/third_party/libdisasm/ia32_operand.c',
    'breakpad/src/third_party/libdisasm/ia32_reg.c',
    'breakpad/src/third_party/libdisasm/ia32_settings.c',
    'breakpad/src/third_party/libdisasm/x86_disasm.c',
    'breakpad/src/third_party/libdisasm/x86_format.c',
    'breakpad/src/third_party/libdisasm/x86_imm.c',
    'breakpad/src/third_party/libdisasm/x86_insn.c',
    'breakpad/src/third_party/libdisasm/x86_misc.c',
    'breakpad/src/third_party/libdisasm/x86_operand_list.c'
]

if system == 'Linux':
    sources.extern(libdiasm)

setup(
    name = 'stackwalker',
    version=VERSION,
    maintainer = 'Benjamin Sergeant',
    maintainer_email = 'bsergean@gmail.com',
    url = 'https://example.com',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries'
    ],

    description = 'Python bindings for google breakpad stack walking',

    ext_modules = [
        Extension('stackwalker',
            sources = sources,
            libraries = ['stdc++'],
            extra_compile_args = extra_compile_args,
        )
    ]
)
