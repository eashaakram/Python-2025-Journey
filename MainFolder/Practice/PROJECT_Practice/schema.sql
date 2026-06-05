-- ============================================================
--  Easha Aqram  |  DSA Learning Platform  |  Database Schema
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username    TEXT    NOT NULL UNIQUE,
    email       TEXT    NOT NULL UNIQUE,
    password    TEXT    NOT NULL,           -- bcrypt hash
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS topics (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    slug        TEXT    NOT NULL UNIQUE,
    description TEXT,
    category    TEXT    NOT NULL,           -- e.g. 'Sorting', 'Trees', 'Graphs'
    difficulty  TEXT    CHECK(difficulty IN ('Beginner','Intermediate','Advanced')),
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_progress (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    topic_id    INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    completed   INTEGER DEFAULT 0,          -- 0 = not started, 1 = completed
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, topic_id)
);

-- ── Seed Topics ──────────────────────────────────────────────
INSERT OR IGNORE INTO topics (title, slug, description, category, difficulty) VALUES
  ('Arrays & Strings',     'arrays-strings',    'Foundation of data storage and manipulation.',           'Arrays',    'Beginner'),
  ('Linked Lists',         'linked-lists',      'Singly, doubly, and circular linked structures.',        'Lists',     'Beginner'),
  ('Stacks & Queues',      'stacks-queues',     'LIFO and FIFO abstract data types.',                     'Linear',    'Beginner'),
  ('Binary Search',        'binary-search',     'Divide and conquer search technique.',                   'Searching', 'Beginner'),
  ('Bubble Sort',          'bubble-sort',       'Classic O(n²) comparison-based sorting.',                'Sorting',   'Beginner'),
  ('Merge Sort',           'merge-sort',        'Efficient O(n log n) divide-and-conquer sort.',          'Sorting',   'Intermediate'),
  ('Quick Sort',           'quick-sort',        'Average O(n log n) in-place partitioning sort.',         'Sorting',   'Intermediate'),
  ('Binary Trees',         'binary-trees',      'Hierarchical node structures with at most 2 children.',  'Trees',     'Intermediate'),
  ('Binary Search Trees',  'bst',               'Ordered trees enabling O(log n) lookup.',                'Trees',     'Intermediate'),
  ('Heaps & Priority Queues','heaps',           'Complete binary trees for priority-based access.',       'Trees',     'Intermediate'),
  ('Hash Tables',          'hash-tables',       'Key-value mapping with O(1) average access.',            'Hashing',   'Intermediate'),
  ('Graphs – BFS',         'graphs-bfs',        'Level-order graph traversal using a queue.',             'Graphs',    'Advanced'),
  ('Graphs – DFS',         'graphs-dfs',        'Depth-first graph traversal using recursion/stack.',     'Graphs',    'Advanced'),
  ("Dijkstra's Algorithm", 'dijkstra',          'Shortest-path algorithm for weighted graphs.',           'Graphs',    'Advanced'),
  ('Dynamic Programming',  'dynamic-programming','Memoization and tabulation for optimal subproblems.',   'DP',        'Advanced');
