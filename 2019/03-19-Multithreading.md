Resource: https://www.internalpointers.com/post/gentle-introduction-multithreading

Takeaway keys:
- Multithreading is about running multiple threads withing a single process.
- Thread share the same chunk of memory assigned to their parent process by the OS
- Thread will proces by CPU Core CPU only one operation at a time

### Concurrency
- CPU Core can only running one process at a time.
- OS use Preemptive multitasking to interrupting a task, switching to another one and then resuming the first task at  a later time,
  with this we can 
- With preemptive os can run multiple process even when hardware only have 1 core

### Problem
- Data race -- while a writer thread modifies the memory, a reader thread might be reading from it. if the writer has not finish the work yet, 
the reader will get corrupted data;
- Race condition -- when two thread write to same memory at the same time.

### Concurrency Control
- Synchronization --  a way to unsure that resources will be used by only one thread at a time.
- atomic operations -- a bunch of non-atomic operations can be turned into atomic
- immutable data -- shared data is mareked as immutable, nothing can change it; threads are only can allowrd to read from it.

