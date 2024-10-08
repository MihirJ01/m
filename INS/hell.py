sharedPrime = 71
sharedBase = 7

aliceSecret = 5
bobSecret = 12

print(f"Publicly Shared Prime: {sharedPrime}")
print(f"Publicly Shared Base: {sharedBase}")

alicePublic = (sharedBase ** aliceSecret) % sharedPrime
bobPublic = (sharedBase ** bobSecret) % sharedPrime

print(f"Alice Sends: {alicePublic}")
print(f"Bob Sends: {bobPublic}")

aliceSharedSecret = (bobPublic ** aliceSecret) % sharedPrime
bobSharedSecret = (alicePublic ** bobSecret) % sharedPrime

print(f"Alice Shared Secret: {aliceSharedSecret}")
print(f"Bob Shared Secret: {bobSharedSecret}")
