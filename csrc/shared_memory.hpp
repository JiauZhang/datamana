#include <sys/mman.h>
#include <nanobind/nanobind.h>

namespace nb = nanobind;

struct SharedMemory {
    int fd;

    SharedMemory() : fd(-1) {}

    int py_shm_open(const char *name, int oflag, unsigned int mode) {
        int ret = shm_open(name, oflag, (mode_t)mode);
        if (ret == -1) {
            ret = errno;
        } else {
            fd = ret;
            ret = 0;
        }
        return ret;
    }
};

void DEFINE_SHAREDMEMORY_MODULE(nb::module_ & (m)) {
    nb::class_<SharedMemory>(m, "SharedMemory")
        .def(nb::init<>())
        .def("open", &SharedMemory::py_shm_open);
}
