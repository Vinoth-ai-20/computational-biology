# Module 12 — Mini Projects

## MP01 — PPI Network Analysis Pipeline (Portfolio artifact)

**Portfolio artifact:** `portfolio/module12_ppi_network_analysis.png`

**Goal:** Build and fully characterize a synthetic PPI network with planted biological
structure. Demonstrate all key network analysis techniques from the module in one
integrated pipeline.

**Steps:**
1. Generate a 300-node network with 4 planted modules (Stochastic Block Model) + BA
   hub structure — represents a realistic disease-relevant PPI network
2. Compute: degree distribution (log-log), clustering coefficient, average path length,
   diameter; compare to ER null model
3. Compute centrality measures (degree, betweenness, PageRank); identify top 10 hubs
   and top 10 bottlenecks (high betweenness, moderate degree)
4. Apply Louvain community detection; compute modularity Q; ARI vs. planted partition
5. Simulate "disease gene" deletion — remove top hub nodes and re-compute connected
   components (fragility under targeted attack vs. random failure)
6. Produce a 4-panel portfolio figure:
   - Panel A: Network visualization (node size = degree, color = community)
   - Panel B: Degree distribution (log-log, power-law fit)
   - Panel C: Centrality comparison (hub vs. bottleneck scatter)
   - Panel D: Attack tolerance (fraction of nodes removed vs. largest component size)

**Implementation rules:**
- Graph construction, degree distribution, clustering coefficient: from scratch (numpy + dict)
- Shortest paths, centrality: NetworkX (Tier 2 — tool usage)
- Louvain: leidenalg or community (python-louvain)
- All scipy/numpy for the linear algebra; no igraph-level graph algorithms written from scratch
