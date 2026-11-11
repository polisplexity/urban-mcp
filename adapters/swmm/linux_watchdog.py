"""Watch owning process pidfds outside the native worker's Python/GIL thread."""
import os
import select
import signal
import sys


def main():
    owner_fd,worker_fd=map(int,sys.argv[1:])
    # pidfds refer to process identity rather than recyclable numeric PIDs.
    # An AnyIO creator thread exiting must not terminate a live simulation.
    ready,_,_=select.select([owner_fd,worker_fd],[],[])
    if owner_fd in ready and worker_fd not in ready:
        try:signal.pidfd_send_signal(worker_fd,signal.SIGKILL)
        except ProcessLookupError:pass
    os.close(owner_fd);os.close(worker_fd)


if __name__=='__main__':main()
