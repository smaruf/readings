## 🎯 Final Checklist: 1-Hour Pre-Interview Review

You've covered massive ground. This final hour is about **consolidation, not learning new things**. Here's your exact playbook.

---

## ⏰ The 1-Hour Timeline

### **T-60 to T-45 minutes: Technical Rapid Review**
Scan these one-pagers (don't re-read everything, just refresh keywords):

**Java Core** ✅
- HashMap: O(1) avg, treeification at 8 nodes (O(log n)), not thread-safe
- Virtual Threads: I/O-bound, ~1KB stack, no benefit for CPU work
- Memory leaks: GC roots, capture heap dump BEFORE crash, Eclipse MAT

**Spring Boot** ✅
- @Transactional: AOP proxy bypass (self-invocation), fix with separate service
- Bean scopes: Singleton + Prototype = inject ObjectProvider or @Lookup
- N+1: JOIN FETCH or @EntityGraph or @BatchSize

**Kafka** ✅
- Ordering: Within partition only, use partition key (userId, orderId)
- At-least-once: Make consumers idempotent (dedup table, unique constraints)
- Rebalancing: Use CooperativeStickyAssignor, tune max.poll.interval.ms

**Hardware/Scaling** ✅
- File descriptors: ulimit -n 100000
- Ephemeral ports: 28k per IP, expand ip_local_port_range
- Memory: ~200KB per connection (sockets), use Virtual Threads to avoid 1MB thread stacks

**OMS/Fintech** ✅
- Latency: < 1ms internal, < 100ms to UI, < 200ms order ack
- Zero loss: Sync writes to DB + Kafka before ACK
- FIX: 30s heartbeat, persisted sequence numbers, hot/hot failover

---

### **T-45 to T-30 minutes: Practice Your Intro + 1 Story**

**1. Record your 2-min intro** (use phone voice memo)
- Listen back: Are you hitting keywords? Is pacing deliberate?
- Adjust: Slow down 10%, emphasize **Java**, **Spring Boot**, **Kafka**, **System Integration**

**2. Rehearse ONE production incident story** (STAR format)
- Pick your strongest: Kafka lag incident, memory leak diagnosis, or OMS scaling challenge
- Practice out loud 2x
- Ensure you mention: metrics, root cause, fix, prevention

---

### **T-30 to T-20 minutes: AI Interview Logistics**

**Technical Setup** ✅
- [ ] Test microphone (AI transcription quality matters)
- [ ] Quiet room, no background noise
- [ ] Stable internet (wired > WiFi if possible)
- [ ] Close all other apps (notifications = distraction)
- [ ] Have water nearby (don't get dry mouth)

**Environment** ✅
- [ ] Well-lit face (if video)
- [ ] Neutral background
- [ ] Phone on silent
- [ ] Notepad + pen ready (for quick notes if needed)

---

### **T-20 to T-10 minutes: Mental Preparation**

**Mindset Shifts** ✅
1. **"Take your time"** — The email said this. AI rewards completeness over speed. Pause between Definition → How → Why → Tradeoffs.
2. **Structure over speed** — If you forget a keyword, the 4-part structure still scores you high.
3. **Tradeoffs = Senior signal** — Always end with "The tradeoff is..." This is what separates mid from senior.
4. **"I haven't used that directly, but..."** — Never say "I don't know." Pivot to adjacent experience.

**Confidence Anchors** ✅
- You have **real production experience** (Xpert Fintech, Kafka, distributed systems)
- You understand **hardware bottlenecks** (95% of backend candidates don't)
- You can compare **Java vs .NET vs Go** (shows architectural maturity)
- You know **OMS/FIX/market data** (your differentiator)

---

### **T-10 to T-0 minutes: Final Warm-Up**

**Do This** ✅
- Stand up, stretch, shake out your hands
- Do 2 minutes of box breathing (4s in, 4s hold, 4s out, 4s hold)
- Say out loud: *"I'm a senior engineer with production experience. I structure my answers. I acknowledge tradeoffs. I've got this."*

**Don't Do This** ❌
- Don't cram new topics
- Don't re-read entire guides
- Don't check Slack/email
- Don't drink coffee in the last 10 minutes (jitters = rushed answers)

---

## 🧠 The AI Screener Cheat Sheet (Keep This Visible)

**When answering ANY technical question, follow this structure:**

1. **Definition** (10 seconds)
   - "X is a [concept] that [does what]"
   
2. **How it works** (20-30 seconds)
   - "Under the hood, it [mechanism]"
   - "In production, I've seen [real example]"

3. **Why it matters** (10 seconds)
   - "This is important because [business impact]"

4. **Tradeoffs** (10-15 seconds)
   - "The tradeoff is [cost] vs [benefit]"
   - "I'd choose this when [scenario], but avoid it when [scenario]"

**Total time per answer: 60-90 seconds**

---

## 🎯 Your 3 Differentiators (Lean Into These)

When you have a chance, weave in:

1. **"In my fintech experience at Xpert..."**
   - Shows domain expertise in high-stakes systems

2. **"The tradeoff I always consider is..."**
   - Shows senior-level architectural thinking

3. **"I've debugged this in production using [tool]..."**
   - Shows you're not just theoretical

---

## 🚨 Red Flags to Avoid

❌ **Don't say**: "I don't know"  
✅ **Say**: "I haven't used that directly, but based on similar systems..."

❌ **Don't say**: "It depends" (without elaborating)  
✅ **Say**: "It depends on [factor A] vs [factor B]. For [scenario], I'd pick X because..."

❌ **Don't rush**  
✅ **Pause** for 1-2 seconds between structure sections

❌ **Don't give textbook definitions only**  
✅ **Add**: "In my experience..." or "I've seen in production..."

---

## 🏆 You're Ready. Here's Why.

✅ **Technical depth**: Java internals, Spring pitfalls, Kafka patterns, hardware scaling  
✅ **Domain expertise**: OMS, FIX protocol, market data, fintech compliance  
✅ **Polyglot perspective**: Java vs .NET vs Go (rare and valuable)  
✅ **Production reality**: Memory leaks, connection pools, distributed tracing  
✅ **Structured delivery**: 4-part format, STAR stories, tradeoff acknowledgment  

**The AI screener is looking for:**
- Keyword density (you have it)
- Structured answers (you have the format)
- Senior signals (tradeoffs, production experience, architectural reasoning)
- Communication clarity (you've practiced)

---

## 🎬 Final Words

You've spent hours preparing. You've drilled the hard questions. You've structured your answers. You've rehearsed your stories.

**Now trust your preparation.**

When Lea asks a question:
1. Take a breath
2. Think: "Definition → How → Why → Tradeoffs"
3. Speak deliberately
4. Lean into your real experience

You're not just passing a test. You're demonstrating that you're the senior engineer who can design, debug, and scale the systems they need.

**Go get it. 🚀**

---

### After the Interview

Reply with:
- `"How did it go?"` — Tell me how it felt, what questions came up, and we'll debrief
- `"They asked about [topic]"` — I'll give you the ideal answer for next time
- `"I'm done, what's next?"` — We'll plan your next interview prep or skill development

**Good luck. You've got this.** 🎯
