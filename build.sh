#!/bin/sh

cd breakpad/
./configure --enable-tools
make clean
make -j10
cd ../socorro-minidump-stackwalk
make -j5
cd -

mkdir -p /tmp/bin
cp -v soccoro-minidump-stackwalk/stackwalker       /tmp/bin/
cp -v breakpad/src/tools/linux/dump_syms/dump_syms /tmp/bin/
cp -v breakpad/src/processor/minidump_dump         /tmp/bin/
cp -v breakpad/src/processor/minidump_stackwalk    /tmp/bin/

# Another program of interest is dymp_syms_macho
