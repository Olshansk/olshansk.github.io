In under half an hour, Claude discovered the origins of the NIST P-192, P-224, P-256, P-384 and P-521 seeds. None of them were the results of any hash algorithm at all, but rather the output of the C library’s lrand48 random-number generator, seeded with a Unix timestamp!

https://www.anthropic.com/research/ecdsa-curve-origins

Create a mini blog post saying TIL about the origins of ECDSA. Link to the blog post, quote what I gave you, and just add one or two sentences as a summary.
