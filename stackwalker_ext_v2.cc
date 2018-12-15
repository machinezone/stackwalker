
#include <Python.h>

#include <string>

extern PyObject * stackwalker_stackwalk(PyObject *self, PyObject *args);

static PyMethodDef StackwalkerMethods[] = {
    {"stackwalk",  stackwalker_stackwalk, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initstackwalker(void)
{
    (void) Py_InitModule("stackwalker", StackwalkerMethods);
}
