#include <semaphore.h>
#include <nanobind/nanobind.h>

int add(int a, int b) {
    return a + b;
}

NB_MODULE(sem, m) {
    m.def("add", &add);
}
