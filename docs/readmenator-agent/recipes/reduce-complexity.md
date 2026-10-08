# Recipe: Reduce File Complexity

Target hotspot: `maxwell_crystallography_suite.py`
(complexity 0.7, centrality 1.0)

1. Read dependents: `grep -n 'maxwell_crystallography_suite.py' readmenator-agent/ARCHITECTURE*.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
