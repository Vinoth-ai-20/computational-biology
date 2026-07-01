# Module 12 — Systems and Network Biology Roadmap

**Tier:** 2 — Working competence  
**Total notebooks:** 12

## Part 1 — Systems Thinking (NB01)

1. `01_systems_thinking_and_emergence.ipynb`  
   Reductionism vs. holism; emergent properties; feedback loops (positive/negative);
   robustness and fragility; the systems biology paradigm; key historical experiments
   (Monod, Jacob — lac operon); why networks matter.

## Part 2 — Graph Theory Foundations (NB02–NB04)

2. `02_graph_theory_for_biological_networks.ipynb`  
   Undirected/directed/weighted/bipartite graphs; adjacency matrix and edge list
   representations; NetworkX from scratch (build, query, visualize); biological network
   types (PPI, GRN, metabolic, signaling, co-expression).

3. `03_network_topology_and_properties.ipynb`  
   Degree distribution; clustering coefficient; shortest path length; diameter;
   average path length; connected components; Erdős–Rényi random graph as null model;
   small-world property (Watts-Strogatz).

4. `04_scale_free_networks_and_barabasi_albert.ipynb`  
   Power-law degree distribution; preferential attachment; Barabási-Albert model
   from scratch; hub nodes; biological implications (hub proteins as essential genes);
   robustness to random failure, fragility to targeted attack.

## Part 3 — Network Analysis (NB05–NB06)

5. `05_network_centrality_measures.ipynb`  
   Degree centrality; betweenness centrality (Brandes algorithm concept); closeness
   centrality; eigenvector centrality; PageRank; biological interpretation of each;
   hub vs. bottleneck proteins.

6. `06_community_detection_in_networks.ipynb`  
   Modularity Q; Louvain algorithm; hierarchical clustering of networks; biological
   modules; pathway modules; applying to a PPI network.

## Part 4 — Biological Networks (NB07–NB08)

7. `07_ppi_network_analysis.ipynb`  
   STRING database overview; load PPI network; degree distribution; identify hubs and
   bottlenecks; overlap with disease genes; network-based drug target identification.

8. `08_gene_regulatory_networks_boolean_models.ipynb`  
   Gene regulatory network (GRN) structure; Boolean network model; update rules;
   attractors and basins of attraction; random Boolean networks (Kauffman NK model);
   stability and criticality.

## Part 5 — Dynamical Models (NB09–NB10)

9. `09_ode_models_of_biological_systems.ipynb`  
   Systems of ODEs for biological dynamics; Lotka-Volterra predator-prey; SIR epidemic
   model; repressilator (synthetic gene network); scipy.integrate.solve_ivp;
   fixed points and stability analysis (Jacobian eigenvalues).

10. `10_metabolic_networks_and_fba.ipynb`  
    Stoichiometric matrix S; flux balance analysis (FBA) as linear programming;
    steady-state constraint S·v = 0; objective function (maximize growth);
    COBRApy tool usage; shadow prices and reduced costs.

## Part 6 — Network Medicine + Assessment (NB11–NB12)

11. `11_network_medicine_and_disease_modules.ipynb`  
    Disease gene clustering; disease module hypothesis; shortest path between disease
    genes; drug-target network; repurposing via network proximity; DisGeNET, OMIM
    databases (survey).

12. `12_mini_project_and_assessment.ipynb`  
    **Mini project MP01:** Build and analyze a synthetic PPI network (300 nodes, planted
    modules, hub structure) — topology, centrality, community detection, hub annotation.  
    **Assessment:** 50 points — graph algorithms (20 pts), ODE model (15 pts),
    conceptual questions (15 pts).
