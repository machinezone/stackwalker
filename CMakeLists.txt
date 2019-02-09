#
# Author: Benjamin Sergeant
# Copyright (c) 2019 Machine Zone, Inc. All rights reserved.
#
# CMakeLists file to build dump_syms_elf on macOS.
# That should work on Linux too (need to be tested)
#

cmake_minimum_required (VERSION 3.4.1)
project (dump_syms_elf)

set (CMAKE_CXX_STANDARD 11)

set (SOURCES 
    breakpad/src/common/dwarf_cfi_to_module.cc
    breakpad/src/common/dwarf_cu_to_module.cc
    breakpad/src/common/dwarf_line_to_module.cc
    breakpad/src/common/dwarf_range_list_handler.cc
    breakpad/src/common/language.cc
    breakpad/src/common/long_string_dictionary.cc
    breakpad/src/common/md5.cc
    breakpad/src/common/module.cc
    breakpad/src/common/path_helper.cc
    breakpad/src/common/simple_string_dictionary.cc
    breakpad/src/common/string_conversion.cc
    breakpad/src/common/test_assembler.cc
    breakpad/src/common/convert_UTF.cc
    breakpad/src/common/stabs_reader.cc
    breakpad/src/common/stabs_to_module.cc

    breakpad/src/common/dwarf/functioninfo.cc
    breakpad/src/common/dwarf/bytereader.cc
    breakpad/src/common/dwarf/elf_reader.cc
    breakpad/src/common/dwarf/dwarf2reader.cc
    breakpad/src/common/dwarf/dwarf2diehandler.cc
    breakpad/src/common/dwarf/cfi_assembler.cc

    breakpad/src/common/linux/synth_elf.cc
    breakpad/src/common/linux/dump_symbols.cc
    breakpad/src/common/linux/file_id.cc
    breakpad/src/common/linux/memory_mapped_file.cc
    breakpad/src/common/linux/crc32.cc
    breakpad/src/common/linux/elfutils.cc
    breakpad/src/common/linux/guid_creator.cc
    breakpad/src/common/linux/linux_libc_support.cc
    breakpad/src/common/linux/elf_symbols_to_module.cc
    breakpad/src/common/linux/elf_core_dump.cc

    dump_syms_linux/memrchr.cc

    breakpad/src/tools/linux/dump_syms/dump_syms.cc

)    

include_directories(${PROJECT_SOURCE_DIR}/breakpad/src)
include_directories(${PROJECT_SOURCE_DIR}/dump_syms_linux)

add_executable(dump_syms_elf ${SOURCES})
