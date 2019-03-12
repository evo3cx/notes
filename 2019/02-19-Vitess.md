Today reading material:
Abstracting Sharding with Vitess and Distributed Deadlocks (Square)

[medium.com](
https://medium.com/square-corner-blog/abstracting-sharding-with-vitess-and-distributed-deadlocks-3128d7c8ffd1)

Key Takeaway:
1.  CMIIW I think they moved from ACID transaction (locking based trx) to "distributed transaction using trx compensation if fail" strategy due to Vitess distributed locking across shard.
2.  2-phase commit (2 PC) is not scalable, even under Vitess. Reference reading 

Solve:
1. how they solve problem with distributed deadlock on multi shard, [here](https://medium.com/@mikebuckets/hey-sachin-malhotra-great-question-6f3b8528844d)

[Your Coffee Shop Doesn’t
Use Two-Phase Commit -](https://www.enterpriseintegrationpatterns.com/docs/IEEE_Software_Design_2PC.pdf)