# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Original Code | Fix Applied |
|---|---|---|---|
| Hardcoded moderator password | Security | `MODERATOR_PASSWORD = "reviews-demo"` | Read the password from the `MODERATOR_PASSWORD` environment variable. |
| Binding to all network interfaces | Security / Configuration | `STREAM_HOST = "0.0.0.0"` | Changed the host to `127.0.0.1` to restrict the configured address to localhost. |
| Weak hash algorithm | Security | `hashlib.md5(...)` | Replaced MD5 with SHA-256 for generating review identifiers. |
| Missing movie and rating validation | Reliability | `rateMovie()` did not verify that the movie existed or that the rating was an integer from 1 to 5. | Added movie-existence checks and rating-type and range validation. |
| Missing movie input validation | Reliability | `addMovie()` accepted empty titles and genres and invalid release years. | Added checks for non-empty titles and genres and a valid integer release year. |
| Unsafe empty collection handling | Reliability | `pickFeatured()` called `random.choice()` even when no movies existed. | Return `None` when the movie collection is empty. |

## Final Static Analysis Results

- Pylint: 10.00/10.
- Bandit: No issues identified.
- Flake8: No violations reported.
