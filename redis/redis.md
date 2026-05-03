## 🧠 What use cases can Redis support?

- **String** → `GET`, `SET`, `DEL`  
- **List** → `RPUSH`, `LPOP`, `LRANGE`, `LINDEX`  
- **Set** → `SADD`, `SREM`, `SMEMBERS`, `SISMEMBER`  
- **Sorted Set** → `ZADD`, `ZREM`, `ZRANGE`, `ZRANGEBYSCORE`, `ZINCRBY`, `ZREVRANGEBYSCORE`, `ZINTERSTORE`  
- **Pub / Sub** → `SUBSCRIBE`, `UNSUBSCRIBE`, `PUBLISH`, `PSUBSCRIBE`, `PUNSUBSCRIBE`  
- **Auto Expiry** → `PERSIST`, `TTL`, `EXPIRE`, `EXPIREAT`  

## ⚙️ How is availability guaranteed?

- Data can be saved to disk via:
  - **Snapshotting** → `BGSAVE`, `SAVE`, `SYNC`, `SHUTDOWN`  
  - **AOF (Append Only File)** → `always`, `everysec`, `no`  

- During replication:
  - Perform `BGSAVE` dump  
  - Write to replication backlog  
  - Stream write commands to replicas  

## 🔁 How to configure Master–Slave?

- Use `SLAVEOF` property on replicas  
- Automatic failover via **Redis Sentinel**

## 📊 Performance

- Actual performance is typically **~50–60%** of `redis-benchmark` results

## ❓ Open Questions

- How much time does replication take?  
- How does consistency behave with multiple replicas?  
- How can scalability be achieved?  
- Pros and cons of using Redis  
- Is custom data type implementation possible?  
- Cloud offerings of Redis in AWS, GCP, and Azure  
