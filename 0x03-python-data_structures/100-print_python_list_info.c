#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: PyObject variable
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i = 0;
	long int sz;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i; i < sz; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);

	}
}

