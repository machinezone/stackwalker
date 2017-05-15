
import stackwalker
import json
import sys


def writeJson(data):
    '''JSON Pretty printer'''

    return json.dumps(data, sort_keys=True,
                      indent=4, separators=(',', ': '))


command = {
    'minidump_path': '/projects/crashzone/tests/test_data/symbolicate/1.dmp',
    'symbol_paths': ['/projects/crashzone/tests/test_data/symbolicate/symbol_store'],
    'err_log_path': '/tmp/stackwalker_log'
}

command = {
    'minidump_path': '/projects/crashzone/tests/test_data/symbolicate/1.dmp',
    'bar': ['/projects/crashzone/tests/test_data/symbolicate/symbol_store'],
    'err_log_path': '/tmp/stackwalker_log'
}

out = stackwalker.stackwalk(json.dumps(command))
print writeJson(json.loads(out))
