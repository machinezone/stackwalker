
import stackwalker
import json
import sys


def writeJson(data):
    '''JSON Pretty printer'''

    return json.dumps(data, sort_keys=True,
                      indent=4, separators=(',', ': '))


command = {
    'minidump_path': 'breakpad/src/processor/testdata//linux_null_dereference.dmp',
    'symbol_paths': ['breakpad/src/processor/testdata//symbols'],
    'err_log_path': '/tmp/stackwalker_log'
}

out = stackwalker.stackwalk(json.dumps(command))
print(writeJson(json.loads(out)))

# /tmp/stackwalker_log will contains log information
