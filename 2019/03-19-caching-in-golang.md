Resource: https://blog.dgraph.io/post/caching-in-go/

Takeaway keys:
- Using Go map with a `sync.Mutex or sync.RWMutex`with goroutine could blocing upon one lock, which can lad to contention/confusing
- clear




