Resource: https://blog.dgraph.io/post/caching-in-go/

Takeaway keys:
- Using Go map with a `sync.Mutex or sync.RWMutex`with goroutine could bloci
ng upon one lock, which can lad to contention/confusing
- Popular Cache Implementations -> on golang allocating fewer, large byte sl
ice and storing many cache entries in each slice  can reducing GC time spent
 on the map shard
- Use of sync.Map is discouraged by go team for various reasons.

Cache Techhnique:
- Bigcache -> divides the data into shards based on the hash of the key [det
ail](https://github.com/allegro/bigcache)
- FreeCache -> [read more](https://github.com/coocood/freecache)
- Summary: currently go suck for cache the beaten with java with service cal
led Cafeine

