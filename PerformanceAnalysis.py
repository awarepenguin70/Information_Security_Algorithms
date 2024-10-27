#pip install numpy
#pip install pandas
#pip install matplotlib seaborn

import time
import hashlib
import random
import string

# Generate random strings
strings = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(100)]

# Compute hashes and measure time
results = {algo: [] for algo in ['md5', 'sha1', 'sha256']}
for s in strings:
    for algo in results:
        start = time.time()
        hash_value = getattr(hashlib, algo)(s.encode()).hexdigest()
        results[algo].append((s, hash_value, time.time() - start))

# Detect collisions
collisions = {algo: {} for algo in results}
for algo, data in results.items():
    seen = {}
    for orig, hval, _ in data:
        if hval in seen:
            collisions[algo].setdefault(hval, []).append(seen[hval])
        else:
            seen[hval] = orig
        collisions[algo].setdefault(hval, []).append(orig)

# Display results
for algo, data in results.items():
    print(f"\n{algo.upper()} Results:")
    for orig, hval, t in data:
        print(f"{orig}: {hval}, Time: {t:.6f}")
    print(f"{algo.upper()} Collisions: {collisions[algo]}")
