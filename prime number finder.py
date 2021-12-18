import wikipedia


N = 20

primes = []

for i in range(1,N):
    try:
        text = wikipedia.page(str(i)).content
    except wikipedia.DisambiguationError:
        text = wikipedia.page(str(i)+"_(number)").content
        

    if "prime" in text and "composite" not in text:
        primes.append(i)

print(f"The primes below {N} are:",primes)