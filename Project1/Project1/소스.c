#include "python.h" 

static PyObject *

spam_strlen(PyObject *self, PyObject *args)
{
	const char* str = NULL;
	int len;

	if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
		return NULL;

	len = strlen(str);

	return Py_BuildValue("i", len);
}

static PyMethodDef SpamMethods[] = {
   { "strlen", spam_strlen, METH_VARARGS,
   "count a string length." },
   { NULL, NULL, 0, NULL } // �迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef spammodule = {
   PyModuleDef_HEAD_INIT,
   "spam",            // ��� �̸�
   "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
   -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}