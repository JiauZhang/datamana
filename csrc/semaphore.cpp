#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <semaphore.h>
#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <stdio.h>

namespace nb = nanobind;

struct Semaphore {
    sem_t *sem;

    Semaphore() : sem((sem_t *)0) {}

    void py_sem_open(const char *name, unsigned int value) {
        sem = sem_open(name, O_CREAT | O_EXCL, 0666, value);
    }
    int py_sem_unlink(const char *name) {
        return sem_unlink(name);
    }
    int py_sem_close() {
        return sem_close(sem);
    }
    int py_sem_post() {
        return sem_post(sem);
    }
    int py_sem_wait() {
        return sem_wait(sem);
    }
};

NB_MODULE(semaphore, m) {
    nb::class_<Semaphore>(m, "Semaphore")
        .def(nb::init<>())
        .def("open", &Semaphore::py_sem_open)
        .def("close", &Semaphore::py_sem_close)
        .def("unlink", &Semaphore::py_sem_unlink)
        .def("wait", &Semaphore::py_sem_wait)
        .def("post", &Semaphore::py_sem_post);
}
