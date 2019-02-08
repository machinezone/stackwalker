
#include <stdio.h>
#include <Python.h>

extern PyObject *
stackwalker_stackwalk(PyObject *self, PyObject *args);


// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
static PyMethodDef stackwalker_methods[] = { 
    {"stackwalk",  stackwalker_stackwalk, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initstackwalker(void)
{
    (void) Py_InitModule("stackwalker", stackwalker_methods);
}
