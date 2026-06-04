### PostgreSQL B-tree vs GIN: what they store, how they search, and why B-tree ≠ binary tree

In PostgreSQL, B-tree is the default index type for ordering and point/range lookups, while GIN (Generalized Inverted Index) is optimized for multi-valued data such as arrays, JSONB keys/values, and full-text search lexemes.

![The Indexes | Internals for Interns](https://images.openai.com/static-rsc-4/tzVsL0uspr6tVUc7oQMT2KNNbeonkINaYlXK_gYWvg9XYUIYnnqy4cphMYoEB_AfIis9sEoMhOT3pqC_FoO8s_aucf295ehSZnNKus4L0sL4ZgRP9s-Yqjkwfu5IekQdxqLHlEaWPIWyyBnGe8y3hCXzHaCx-ccDuPVtUVtvvRhcc8vRC-MN5h9lCTtIVB78?purpose=fullsize)

![Mastering PostgreSQL GIN Indexes: The Ultimate Guide to Faster JSONB, Array, and Full-Text Search | by Vedant Thakkar | Medium](https://images.openai.com/static-rsc-4/o-P4rU-2OwWdNTVhUBwJ4K4h_Sa-j8JpXNXxaMz2_5grIWRniOtr-N82wKSq7bntPeFI00VJlRqyxMl0QBLttqAVkImS_Z1_R6NMeaWCHWJ8a-paGXGoIJxKMI1bM7_F-yBs0HjVffyc5T7slPN_je6VTjkZqhscsvQ_WJxgCUKe6919ByOx9OojrPb0PO52?purpose=fullsize)

![Why Binary Trees Are Bad for Disk Storage (And What Works Better) | by Chiranjeevi Sutraye | Medium](https://images.openai.com/static-rsc-4/QLj2FkZ9zd4IfXnCldtvQvx0yaDZxUWJ9fRW95NmpNgyU6Qwi3-hrwLa5GKCfNa0b97geABYd9eZJ2RvL-dJs3xqRxyWDZkR6befnH43CViTJksYHyrGXMFl3JGLcN3SE88zWezy8BBM2Qt0A_3r8xHv_WZI5EfAx1nLNPXO0CnLOgOCV2mrnuMG4CilJDXm?purpose=fullsize)

### 1. Binary Search Tree (BST) vs B-tree

| Property            | Binary Search Tree (BST)       | B-tree (database index tree)        |
| ------------------- | ------------------------------ | ----------------------------------- |
| Children per node   | ≤ 2                            | Many (fanout often hundreds)        |
| Node contents       | 1 key (typically)              | Many keys + child pointers          |
| Height              | Can become large if unbalanced | Very small because of high fanout   |
| Disk I/O efficiency | Poor for large datasets        | Excellent for page-oriented storage |
| Typical use         | In-memory data structures      | Database indexes                    |

### Example of Operation

Binary Search Tree (fanout = 2)

To find `60` you may traverse several levels. If the tree becomes skewed, height can approach `N`.

B-tree node (fanout > 2)

One node contains multiple keys and child pointers. A single page read advances you past many keys at once, so the tree height stays tiny even for millions of rows.

### 2. Where Red-Black Trees Fit In

A Red-Black Tree (RBT) is a self-balancing binary search tree. It maintains balance through color rules and rotations.

Why databases usually don't use RBTs as on-disk indexes: an RBT still has fanout 2. Even perfectly balanced, millions of keys produce many levels and therefore many random page reads. B-trees reduce height dramatically by storing many keys per page.

Rule of thumb: RBTs are excellent in-memory ordered maps (e.g., language runtimes, kernels). B-trees are the standard for disk-backed database indexes.

### 3. PostgreSQL B-tree Index

PostgreSQL's default `btree` index is a page-oriented B-tree variant optimized for MVCC, concurrency, and ordered scans.

### What is stored?

Conceptually:

Where `TID` points to the heap row (table tuple).


### Example: equality lookup

The planner can do an Index Scan on `users_email_idx` because B-tree supports equality efficiently.

### Example: range query

B-tree is ideal here because the index is ordered. PostgreSQL can scan the relevant key range directly.

### Page split (simplified)

Suppose a leaf page is full:

B-trees stay balanced through splits/merges while preserving order.

### What B-tree supports well

* `=`, `<`, `<=`, `>`, `>=`

* `BETWEEN`

* `ORDER BY` on the indexed prefix

* Prefix pattern searches when operator classes permit (e.g., text pattern ops)

### What it does not do well

* Arbitrary substring search `%foo%` with a normal B-tree

* Containment queries on arrays/JSONB

* Full-text search

### 4. PostgreSQL GIN Index (Generalized Inverted Index)

A GIN index stores a mapping from token → list of row references. It is fundamentally an inverted index.

### Conceptual structure

That is very different from a B-tree, which stores rows ordered by key.

### Example: array containment

GIN indexes each tag value separately and quickly finds rows containing `'postgres'`.

### Example: JSONB containment

GIN indexes JSONB keys/paths (operator-class dependent) and can accelerate containment queries dramatically.

### Example: full-text search

Here GIN indexes lexemes produced by `to_tsvector`.

### Posting list → posting tree

For rare tokens, PostgreSQL can keep a simple posting list:

For very common tokens, the list becomes too large and is stored in a separate posting tree:

This keeps lookups scalable.

### 5. Side-by-side Example: Why B-tree and GIN Answer Different Questions

Table:

Indexes:

| Query                                                             | Best Index                                                                                             |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| WHERE title = 'PostgreSQL GIN Guide'                              | B-tree                                                                                                 |
| WHERE title >= 'P' AND title < 'Q'                                | B-tree                                                                                                 |
| WHERE tags @> ARRAY['postgres']                                   | GIN                                                                                                    |
| WHERE to_tsvector('english', body) @@ plainto_tsquery('indexing') | GIN                                                                                                    |
| WHERE body LIKE '%index%'                                         | Neither standard B-tree nor GIN FTS directly; consider pg_trgm GIN/GiST or FTS depending on semantics. |

### 6. Complexity and Height Intuition

Suppose an index page holds ~200 separators/pointers.

B-tree

Millions of rows often require only 3–4 page reads from root to leaf.

Red-Black Tree

For 8 million keys, `log2(8,000,000) ≈ 23` comparisons/levels. On disk, that would be far more page traversals than a B-tree.

### 7. Practical PostgreSQL Guidance

| Need                                       | Use                   |
| ------------------------------------------ | --------------------- |
| Primary key, unique lookup                 | btree (default)       |
| Range scans / ORDER BY                     | btree                 |
| Arrays with @>, <@, overlap queries        | GIN                   |
| JSONB containment queries                  | GIN                   |
| Full-text search (@@ tsquery)              | GIN                   |
| Substring/fuzzy search (%foo%, similarity) | pg_trgm with GIN/GiST |

Common mistake

Adding a GIN index and expecting it to speed up ordinary equality/range queries on a scalar column. For `WHERE email = ?`, a B-tree is almost always the correct index. Use GIN when the query asks does this document/array/text contain token X? rather than find rows ordered by scalar key K.

Takeaway

1. Binary tree: fanout 2; can be unbalanced.

2. Red-black tree: balanced binary tree via rotations; great in memory, not ideal as a disk index.

3. B-tree (PostgreSQL btree index): high-fanout, page-oriented, balanced tree optimized for equality, ranges, and ordering.

4. GIN: inverted index mapping token → row references; optimized for arrays, JSONB containment, and full-text search.

5. Choose by query semantics: ordered scalar lookups → B-tree; containment/membership/full-text → GIN.

---

## Let's go deeper with actual text-based visualizations.

# 1. Binary Search Tree (BST)

Insert:

```text
50
├── 30
│   ├── 20
│   └── 40
└── 70
    ├── 60
    └── 80
```

Search for **60**

```text
Start at 50
60 > 50 → go right

       50
         \
          70

60 < 70 → go left

       70
      /
    60

Found
```

Traversal path:

```text
50 → 70 → 60
```

Time complexity:

```text
Balanced:    O(log n)
Unbalanced:  O(n)
```

Example of bad BST:

```text
10
 \
  20
   \
    30
     \
      40
       \
        50
```

This becomes a linked list.

---

# 2. Red-Black Tree

A Red-Black Tree is a self-balancing BST.

Node colors:

```text
(B) = Black
(R) = Red
```

Example:

```text
        50(B)
       /     \
   30(R)    70(R)
   /  \      /  \
20(B)40(B)60(B)80(B)
```

Rules:

```text
1. Root must be black
2. Red node cannot have red child
3. Every path must have same black height
```

Insertion example:

Insert 10

Before balancing:

```text
       50(B)
      /
   30(R)
   /
10(R)
```

Violation:

```text
Red parent
Red child
```

Fix:

```text
Rotation
Recoloring
```

After balancing:

```text
      30(B)
     /     \
 10(R)    50(R)
```

### Why use RBT?

Languages and OS kernels often use them:

* Java TreeMap
* Linux scheduler structures
* C++ std::map (typically)

Because:

```text
Guaranteed O(log n)
```

---

# 3. Why Databases Don't Use Red-Black Trees

Suppose:

```text
100 Million rows
```

RBT height:

```text
log₂(100M)

≈ 27
```

Need ~27 node traversals.

Disk access:

```text
Page
 ↓
Page
 ↓
Page
 ↓
27 times
```

Very expensive.

---

# 4. B-Tree Structure

B-tree nodes contain MANY keys.

Example order 4:

```text
            [40 | 80]
            /   |    \
           /    |     \
          /     |      \
 [10|20|30] [50|60|70] [90|100]
```

One node contains multiple keys.

Search for 60:

```text
Root: [40|80]

60 > 40
60 < 80

Go middle child
```

Middle node:

```text
[50|60|70]
```

Found.

Traversal:

```text
Root
 ↓
Leaf

Only 2 reads
```

---

# 5. PostgreSQL B-Tree Index Internals

Table:

```sql
CREATE TABLE users(
  id BIGINT,
  email TEXT
);
```

Index:

```sql
CREATE INDEX idx_email
ON users(email);
```

Conceptually:

```text
                      [m@x.com]
                     /         \
                    /           \
     [a@x.com ... l@x.com]    [n@x.com ... z@x.com]
```

Leaf pages:

```text
Leaf 1

a@x.com -> TID(1,5)
b@x.com -> TID(1,8)
c@x.com -> TID(2,1)
...
```

TID:

```text
Heap Page + Row Offset
```

Actual workflow:

```sql
SELECT *
FROM users
WHERE email='john@test.com';
```

Execution:

```text
Planner
 ↓
BTree Root
 ↓
Internal Page
 ↓
Leaf Page
 ↓
Get TID
 ↓
Read Heap Row
```

Diagram:

```text
            ROOT
              |
       +------+------+
       |             |
    PAGE A       PAGE B
                    |
               +----+----+
               |         |
           LEAF 1     LEAF 2
                         |
                  john@test.com
                         |
                    TID(201,7)
                         |
                      HEAP
```

---

# 6. PostgreSQL B-Tree Range Scan

Query:

```sql
SELECT *
FROM orders
WHERE amount
BETWEEN 1000 AND 2000;
```

Index:

```text
100
200
500
1000
1100
1200
1300
...
2000
2100
```

Workflow:

```text
Find first matching value

1000
 ↓
Sequentially walk leaf pages
 ↓
1100
 ↓
1200
 ↓
1300
 ↓
...
 ↓
2000
```

This is why B-tree excels at:

```sql
<
>
BETWEEN
ORDER BY
```

---

# 7. PostgreSQL GIN Index

GIN means:

```text
Generalized Inverted Index
```

Think:

```text
Word
 ↓
Rows containing word
```

Instead of:

```text
Row
 ↓
Value
```

---

## Example: Tags

Table:

```sql
id | tags
------------------------
1  | {java,postgres}
2  | {java,kafka}
3  | {python,postgres}
```

GIN index:

```text
java
 ├── row 1
 └── row 2

postgres
 ├── row 1
 └── row 3

kafka
 └── row 2

python
 └── row 3
```

---

Query:

```sql
SELECT *
FROM articles
WHERE tags @> ARRAY['postgres'];
```

Workflow:

```text
Search token:

postgres
      ↓

Posting List

row1
row3
      ↓

Return rows
```

No table scan needed.

---

# 8. GIN Full Text Search

Document table:

```text
Row1:
"Postgres indexing guide"

Row2:
"Kafka architecture"

Row3:
"Postgres GIN index"
```

GIN:

```text
postgres
 ├── row1
 └── row3

index
 ├── row1
 └── row3

kafka
 └── row2

architecture
 └── row2
```

Query:

```sql
SELECT *
FROM docs
WHERE to_tsvector(content)
@@ to_tsquery('postgres');
```

Workflow:

```text
Search word:
postgres
      ↓

Posting List

row1
row3
      ↓

Fetch rows
```

---

# 9. JSONB + GIN

Table:

```json
{
  "name":"John",
  "city":"Gdansk",
  "role":"admin"
}
```

GIN entries:

```text
name -> row1
John -> row1

city -> row1
Gdansk -> row1

role -> row1
admin -> row1
```

Query:

```sql
WHERE data @> '{"role":"admin"}'
```

Workflow:

```text
role
 ↓

admin
 ↓

Matching rows
```

---

# 10. Comparison Summary

```text
                SEARCH STRUCTURES

Binary Tree
     ↓
2 children
May become unbalanced

Red-Black Tree
     ↓
Balanced Binary Tree
O(log n)

B-Tree
     ↓
Many children
Disk optimized
Used by PostgreSQL BTree index

GIN
     ↓
Token -> Row mapping
Inverted Index
Used for:
  - Arrays
  - JSONB
  - Full Text Search
```

### Mental Model

```text
B-Tree

Find rows by ordered value

email
  ↓
row

amount
  ↓
row
```

```text
GIN

Find rows containing token

token
  ↓
rows

postgres
  ↓
row1,row3,row7,row20
```

That's the key distinction: **B-tree navigates a hierarchy of sorted keys**, while **GIN jumps directly from a token to all matching rows through posting lists/posting trees.**

