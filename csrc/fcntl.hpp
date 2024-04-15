#include <fcntl.h>           /* For O_* constants */

struct FCNTL {
    inline static int o_creat = O_CREAT;
    inline static int o_excl = O_EXCL;
    inline static int o_trunc = O_TRUNC;
    inline static int o_rdonly = O_RDONLY;
    inline static int o_wronly = O_WRONLY;
    inline static int o_rdwr = O_RDWR;
    inline static int o_nonblock = O_NONBLOCK;
};
