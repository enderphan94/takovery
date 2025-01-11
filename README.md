# Takovery
This script detects potential subdomain takeover vulnerabilities

# What it does

1. CNAME Resolution
* Identify subdomains pointing to third-party services that might be misconfigured or abandoned.
* The script resolves the CNAME records of the given subdomains using:
  - A DNS resolver library for programmatic resolution.
  - The dig command-line tool for cross-verification.
  - The resolved CNAMEs are compared with a known database of vulnerable service patterns to determine if the subdomain points to a service that is potentially exploitable.

4. HTTP Response Analysis
* Detect clues of misconfiguration or abandonment in the subdomain’s HTTP response.
* Method:
  -	The script sends HTTP requests to the subdomain and analyzes the response body (HTML or text).
  -	Known vulnerable service-specific fingerprints (e.g., specific error messages or placeholder text) are matched against the response to detect misconfigurations.
  -	This technique identifies vulnerabilities even if DNS resolution alone does not indicate an issue.

5. Regular Expression Matching
* Purpose: Identify potential vulnerabilities through generic or service-specific patterns in the HTTP response.
* Method:
  -	The script uses a set of predefined regular expressions to analyze the HTTP response content for indicators of misconfigured or abandoned subdomains.
  - These patterns include error messages, unclaimed pages, or service-specific text that are commonly associated with takeover scenarios.

6. WHOIS Lookup
* Purpose: Gather ownership and administrative details about the subdomain to aid in understanding its configuration.
* Method:
  -	A WHOIS query is performed to fetch information like the organization name (OrgName) associated with the subdomain.
  - This information provides context about whether the subdomain is controlled by the expected entity or potentially abandoned/misconfigured.

7. Fingerprint Matching
* Purpose: Validate the resolved CNAME and HTTP response content against known service-specific vulnerabilities.
* Method:
  -	The script checks the resolved CNAME or HTTP response against a curated database of fingerprints for popular services known to be vulnerable to subdomain takeovers.
  - If a match is found, the script flags the subdomain as potentially vulnerable and outputs details about the vulnerable service.

8. Asynchronous Processing
* Purpose: Enhance performance and efficiency when scanning multiple subdomains.
* Method:
  -	The script uses asynchronous HTTP requests to fetch responses concurrently for multiple subdomains.
  - This reduces the overall scan time and enables efficient handling of large-scale subdomain enumeration tasks.


# Usage

For a single domain

```python3.10 takeover.py -d sample.com```

For a list of domain

```python3.10 takeover.py -iL domain.txt```
