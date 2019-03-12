https://jepsen.io/analyses/faunadb-2.5.4

## Summary:
### Background
- FounaDB use Calvin: Fast Distributed Transactions for Patitioned Database System [read paper here](http://cs.yale.edu/homes/thomson/publications/calvin-sigmod12.pdf)
- Calvin seperate ordering transactions, and `executing` trasactions
- Calvin transaction must be submitted on a single request to ordering system called `sequencer`, accept transactions, batches them up into the time windows, and appends those batches to sharded, totally ordered log. 
- FounaDB use consensus system like Raft or Paxos instead of two-phase commit, with consensus on log entries, each Calvin replica can read the log and execute the transactions in it indepedently.
- SpannerDB and CockroachDB relying on semi-synchronized wall clocks


### FoundaDB
- FoundaDB record are JSON-style objects, called instances; each instance is identified by primary key called a `ref`.
- Collection of instances is called a `class`
- Strong consistensy with 100% ACID
- [Architecture blog post](https://fauna.com/blog/acid-transactions-in-a-globally-distributed-database)
- Starting a FaunaDB cluster in 2.5.5 and 2.5.6 was a slow process, requiring ~10minutes to stabilize

