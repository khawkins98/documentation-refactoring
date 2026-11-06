# Maintainer inputs

The synthetic reference.csv is the maintained input for project/gate.py. It stays
outside project/ and is deliberately not a project source file. The gate accepts
its path through REFERENCE_TABLE_PATH and checks a pinned SHA-256 before use.
No download or generated replacement is needed.
