
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

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef stackwalker_definition = { 
    PyModuleDef_HEAD_INIT,
    "stackwalker",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    stackwalker_methods
};

// Module initialization
// Python calls this function when importing your extension. It is important
// that this function is named PyInit_[[your_module_name]] exactly, and matches
// the name keyword argument in setup.py's setup() call.
PyMODINIT_FUNC PyInit_stackwalker(void) {
    Py_Initialize();
    return PyModule_Create(&stackwalker_definition);
}
