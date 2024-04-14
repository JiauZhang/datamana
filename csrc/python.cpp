#include "semaphore.hpp"
#include "mqueue.hpp"
#include <nanobind/nanobind.h>

namespace nb = nanobind;

NB_MODULE(core, m) {
    nb::class_<Semaphore>(m, "Semaphore")
        .def(nb::init<>())
        .def("open", &Semaphore::py_sem_open)
        .def("close", &Semaphore::py_sem_close)
        .def("unlink", &Semaphore::py_sem_unlink)
        .def("wait", &Semaphore::py_sem_wait)
        .def("post", &Semaphore::py_sem_post)
        .def_prop_ro("O_CREAT", [](Semaphore &sem) { return sem.o_creat; })
        .def_prop_ro("O_EXCL", [](Semaphore &sem) { return sem.o_excl; })
        .def_prop_ro("O_TRUNC", [](Semaphore &sem) { return sem.o_trunc; });

    nb::class_<MQueue>(m, "MQueue")
        .def(nb::init<>())
        .def("open", &MQueue::py_mq_open)
        .def("close", &MQueue::py_mq_close)
        .def("unlink", &MQueue::py_mq_unlink)
        .def("send", &MQueue::py_mq_send)
        .def("receive", &MQueue::py_mq_receive)
        .def_prop_ro("O_RDONLY", [](MQueue &mq) { return mq.o_rdonly; })
        .def_prop_ro("O_WRONLY", [](MQueue &mq) { return mq.o_wronly; })
        .def_prop_ro("O_RDWR", [](MQueue &mq) { return mq.o_rdwr; })
        .def_prop_ro("O_CREAT", [](MQueue &mq) { return mq.o_creat; })
        .def_prop_ro("O_EXCL", [](MQueue &mq) { return mq.o_excl; })
        .def_prop_ro("O_NONBLOCK", [](MQueue &mq) { return mq.o_nonblock; });
}
