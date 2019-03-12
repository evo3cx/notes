Reading Material:

Mysql Refrence Manual Locking Table:

[Manual refrence](https://www.oreilly.com/library/view/mysql-reference-manual/0596002653/ch05s03.html)

* Mysql will lock table except for InnoDB and BDB tables two of them will lock based on row
* _InnoDB_ type tables automatically acquire their locks 
* _BDB_ types tables their page locks during the processing of SQL statements, not at the start of transaction
* Mysql _WRITE locks_ works as follows:
  * If there are no locs on the table, put a write lock on it.
  * Otherwise, put the lock request in the write lock queue.
* The locking method MYSQL uses for READ locks works as follows:

  * If there are no write locsk on the table, put a read lock on it.
  * Otherwise, put the lock request in the read lock queue