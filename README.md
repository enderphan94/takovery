# Takovery
This script detects potential subdomain takeover vulnerabilities

# What it does

1. CNAME Resolution.
2. HTTP Response Analysis
3. Regular Expression Matching
4. WHOIS Lookup
5. Fingerprint Matching
6. Asynchronous Processing

# Usage

For a single domain

```python3.10 takeover.py -d sample.com```

For a list of domain

```python3.10 takeover.py -iL domain.txt```

# Inspired by

Subzy, hackerone, other scripts on github
