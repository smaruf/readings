Here's a **high-yield question bank** modeled on what an AI screening agent like Lea will actually ask, with **structured answers** in the format AI scorers reward (Definition → How → Why → Tradeoffs).

I've weighted questions by the tier priorities in your guide and woven in your differentiators (Kafka, distributed systems, market data).

---

## 🎯 TIER 1 — Java Core (Very High Weight)

### Q1. *"What is the difference between HashMap and ConcurrentHashMap?"*
**Structured Answer:**
1. **Definition**: `HashMap` is a non-thread-safe map; `ConcurrentHashMap` is a thread-safe alternative.
2. **How it works**:
   - `HashMap` uses an array of buckets + linked lists/trees; single lock for the entire map (pre-Java 8) or no locking at all.
   - `ConcurrentHashMap` uses **lock striping** (Java 8+: CAS + `synchronized` on individual buckets), allowing concurrent reads/writes without locking the whole map.
3. **Why it's used**: `HashMap` is fastest in single-threaded code; `ConcurrentHashMap` scales in concurrent environments without the cost of `Hashtable`'s global lock.
4. **Tradeoffs**: `ConcurrentHashMap` has slightly higher memory/CPU overhead and **does not allow null keys/values** (unlike `HashMap`).

---

### Q2. *"How does `volatile` differ from `synchronized`?"*
1. **Definition**: `volatile` ensures **visibility**; `synchronized` ensures **visibility + atomicity**.
2. **How it works**:
   - `volatile` forces reads/writes to go to main memory, bypassing CPU caches.
   - `synchronized` acquires a monitor lock, ensuring mutual exclusion + memory barriers.
3. **Why it's used**: `volatile` is lightweight for simple flags (e.g., `volatile boolean running`); `synchronized` is for compound operations like `count++`.
4. **Tradeoffs**: `volatile` is faster but **cannot** make `count++` atomic. Overuse of `synchronized` kills throughput.

---

### Q3. *"Explain JVM memory structure."*
1. **Definition**: JVM divides runtime memory into **Heap**, **Stack**, **Method Area/Metaspace**, **PC Register**, and **Native Stack**.
2. **How it works**:
   - **Heap**: Objects (Young Gen + Old Gen). GC lives here.
   - **Stack**: Per-thread, stores frames with local variables & operand stacks. Fast, auto-cleaned.
   - **Metaspace**: Class metadata (moved off-heap since Java 8).
3. **Why it matters**: Memory leaks live in Heap (unreferenced objects still reachable). Stack overflow = deep recursion.
4. **Tradeoffs**: Larger heap = more GC pauses. Tune via `-Xms`, `-Xmx`, GC algorithm (G1, ZGC for low latency).

---

### Q4. *"What is the difference between Interface and Abstract Class?"* (Java 8+)
1. **Definition**: Both define contracts, but with different semantics.
2. **Key differences**:
   - Class can extend **only one** abstract class; implement **multiple** interfaces.
   - Since Java 8, interfaces support `default` and `static` methods.
   - Abstract classes can have **state** (instance fields); interfaces cannot (pre-Java 9).
3. **Why it matters**: Prefer **interfaces** for API contracts (flexibility). Use **abstract classes** when sharing state/implementation across a tight hierarchy.
4. **Tradeoffs**: Multiple inheritance of state is a design smell — abstract classes push you toward it.

---

### Q5. *"How do Streams work? What are common pitfalls?"*
1. **Definition**: Streams are a declarative API for processing sequences of elements.
2. **How it works**: Source → intermediate ops (lazy: `filter`, `map`) → terminal op (eager: `collect`, `forEach`).
3. **Common pitfalls**:
   - Side effects in `map`/`filter` (violates functional style)
   - Using parallel streams on small collections or I/O-bound work → overhead outweighs gains
   - Forgetting that streams are **consumed once** (can't reuse)
4. **Tradeoffs**: Clean code vs. sometimes harder to debug than loops. Parallel streams need thread-safe sources.

---

## 🎯 TIER 2 — Spring Boot (Very High Weight)

### Q6. *"Explain Dependency Injection and Bean scopes."*
1. **Definition**: DI is an IoC pattern where Spring manages object creation and wiring.
2. **Bean scopes**:
   - `singleton` (default): one per `ApplicationContext`
   - `prototype`: new instance every injection
   - `request`/`session`: web-aware, tied to HTTP lifecycle
3. **Why it's used**: Decouples components, enables testing via mocks, centralizes lifecycle.
4. **Tradeoffs**: Singletons must be **thread-safe**; prototype beans can cause memory leaks if not released.

---

### Q7. *"What is the N+1 problem in JPA and how do you fix it?"*
1. **Definition**: N+1 = 1 query to fetch parents + N queries to fetch children (one per parent).
2. **How it happens**: Lazy loading triggered in a loop.
3. **Fixes**:
   - `JOIN FETCH` in JPQL
   - `@EntityGraph`
   - `@BatchSize`
4. **Tradeoffs**: `JOIN FETCH` can explode result set size; `@BatchSize` trades queries for row count.

---

### Q8. *"How does Spring manage transactions?"*
1. **Definition**: Declarative TX via `@Transactional` using AOP proxies.
2. **How it works**: Proxy wraps the method → begins TX → commits on success → rolls back on `RuntimeException` by default.
3. **Gotchas**:
   - Calling `@Transactional` method **from the same class** bypasses the proxy → TX not applied.
   - Checked exceptions don't trigger rollback unless configured.
   - `propagation=REQUIRES_NEW` opens a new TX (use for audit logs).
4. **Tradeoffs**: Convenience vs. hidden coupling. Always verify proxy is actually being used.

---

### Q9. *"JWT vs Session-based auth — tradeoffs?"*
1. **JWT**: Stateless, self-contained, scales horizontally, harder to revoke.
2. **Session**: Stateful on server, easy to revoke, requires shared session store for scale.
3. **My pick**: JWT for **public APIs/microservices**; sessions for **server-rendered apps** where revocation matters.

---

## 🎯 TIER 3 — REST & Microservices

### Q10. *"Why is PUT idempotent but POST is not?"*
1. **Definition**: Idempotent = same request repeated = same server state.
2. **PUT**: Replaces resource at URI. `PUT /users/1` with same body 5x → final state = 1 user.
3. **POST**: Creates. `POST /users` 5x → 5 users.
4. **Tradeoffs**: PUT requires client to know URI; POST lets server assign IDs.

---

### Q11. *"How do you manage transactions across microservices?"*
1. **Answer**: **Saga pattern** (choreography or orchestration).
2. **How it works**: Each service has a local TX + compensating action. Coordinator (or events) orchestrates.
3. **Why not 2PC**: Blocks resources, single point of failure, doesn't scale.
4. **Tradeoffs**: Sagas are eventually consistent — UI must handle partial states (e.g., "payment pending").

---

### Q12. *"What does a Circuit Breaker do?"*
1. **Definition**: Prevents cascading failures by short-circuiting calls to a failing dependency.
2. **States**: Closed → Open (fast fail) → Half-Open (probe).
3. **Implementation**: Resilience4j in Spring.
4. **Tradeoffs**: Adds complexity; must tune thresholds per service.

---

## 🎯 TIER 4 — System Integration & Messaging (Your Differentiator)

### Q13. *"How does Kafka guarantee ordering?"*
1. **Answer**: Ordering is guaranteed **within a partition only**.
2. **How**: Use a partition key (e.g., `orderId`) → all events for that key hit the same partition → FIFO.
3. **Tradeoffs**: Global ordering requires 1 partition → kills parallelism. Design key carefully.

---

### Q14. *"How do you handle duplicates in at-least-once delivery?"*
1. **Answer**: Make consumers **idempotent**.
2. **Techniques**:
   - Dedup via unique message ID in DB (`INSERT ... ON CONFLICT DO NOTHING`)
   - Idempotency keys from producer
   - Database constraints (unique + conditional)
3. **Tradeoffs**: Exactly-once (Kafka transactions) is heavier; idempotent consumers scale better.

> **Your differentiator**: *"In market data systems handling FIX/ITCH feeds, I used idempotent consumers backed by dedup tables because replay is part of the design — we treat 'at-least-once + idempotency' as the primitive rather than chasing exactly-once semantics."*

---

### Q15. *"Request/Response vs Event-Driven — when do you pick each?"*
1. **Request/Response**: Simple, synchronous, strong consistency, tight coupling.
2. **Event-driven**: Async, decoupled, scalable, eventual consistency, replayable.
3. **Tradeoffs**: EDA adds operational complexity (observability, schema evolution, DLQ).

---

## 🎯 TIER 5 — Cloud & Containers

### Q16. *"Image vs Container?"*
1. **Image**: Read-only template (layers).
2. **Container**: Running instance of an image with its own writable layer.
3. **Analogy**: Image = class; Container = object instance.

---

### Q17. *"What happens when a Pod crashes in Kubernetes?"*
1. **Kubelet** detects crash (via liveness probe or exit code).
2. Depending on `restartPolicy` (`Always`/`OnFailure`/`Never`), Kubelet restarts the container.
3. Deployment controller maintains replica count.
4. If node is dead, controller reschedules Pod to another node.

---

### Q18. *"Security Group vs NACL in AWS?"*
| | Security Group | NACL |
|---|---|---|
| **Level** | Instance | Subnet |
| **State** | Stateful | Stateless |
| **Rules** | Allow only | Allow + Deny |
| **Evaluation** | All rules before allow | In order, first match wins |

---

## 🎯 TIER 6 — System Design (Likely AI Question)

### Q19. *"Design a notification system."*
**Structured design**:
1. **Ingest**: API Gateway → Notification Service (validates, persists to DB as `PENDING`)
2. **Queue**: Publish `NotificationCreated` event to Kafka (topic partitioned by `userId`)
3. **Workers**: Consumer group per channel (email/SMS/push). Each has rate limiters + retry with exponential backoff.
4. **DLQ**: After N retries → DLQ + alert → manual/SRE review.
5. **Idempotency**: Message ID dedup table so retries don't double-send.
6. **Scaling**: Horizontal workers; per-user partitioning prevents head-of-line blocking.

---

### Q20. *"Design an order processing system."*
1. **Order Service** receives order → writes `CREATED` to DB → emits `OrderCreated` event.
2. **Payment Service** consumes → processes → emits `PaymentCompleted/Failed`.
3. **Inventory Service** consumes → reserves stock.
4. **Saga orchestrator** listens to all events. On any failure, triggers compensating actions (refund, release stock).
5. **Idempotency** at every step via order IDs.

---

## 🎯 BEHAVIORAL (STAR Format — AI-Friendly)

### Q21. *"Tell me about a production incident."*
**Model answer structure:**
- **Situation**: "During a market data feed migration, our Kafka consumers started lagging 15 minutes behind."
- **Task**: "I was the on-call senior; needed to restore SLA and find root cause."
- **Action**: "1) Checked consumer lag dashboard. 2) Found one partition 10x hotter than others — hot key issue. 3) Mitigated immediately by scaling partitions. 4) Added salt to partition key. 5) Implemented lag-based autoscaling alert."
- **Result**: "Lag dropped to <10s within 20 min. No client impact. Added runbook for future incidents."
- **Learning**: "Partition design is as critical as consumer scaling."

---

## 🎯 AI INTERVIEW DELIVERY TIPS (Critical for Lea)

1. **Always use the 4-part structure**: Definition → How → Why → Tradeoffs. AI scorers check for these markers.
2. **Use signpost language**: *"There are three main differences…"*, *"The tradeoff here is X vs Y…"*
3. **If you don't know**: *"I haven't used that directly, but based on similar systems I've worked with, I'd reason that…"*
4. **Pause deliberately**. The email says "take your time" — AI rewards completeness over speed.
5. **Name-drop your expertise** where relevant: *"In my market data systems using FIX protocols…"* — differentiates you from generic candidates.

---
