
#include <Python.h>

#include <string>

extern std::string stackwalker(const std::string& command);

PyObject *
stackwalker_stackwalk(PyObject *self, PyObject *args)
{
    const char *command;

    if (!PyArg_ParseTuple(args, "s", &command)) {
        return NULL;
    }

    std::string str = stackwalker(command);

    if (str.empty()) {
        PyErr_SetString(PyExc_ValueError, "error parsing command");
        return NULL;
    }

    return Py_BuildValue("s", str.c_str());
}
