-- Why is public key encryption used over general encryption? How do you think we can protect our data and take into account increasing computer speeds?  
PKE is much more secure than general encryption since it is more difficult to crack with brute force. General encryption is also subject to the key being intercepted by an unwanted agent, but PKE is not susceptible to this flaw since there is not private key that is shared between users.  

Increasing the encryption bit size makes brute force more difficult since it provides exponentially more options that a brute force hacker would have to try. Not sure if we're going in this direction, but if quantum computing gets off the ground, I'm not sure there is any reasonable way to continue with PKE (given the nearly instantaneous speeds of quantum computing).  

-- Explain how the RSA algorithm works.  

Choose two large prime numbers, p and q. These numbers are kept secret. Calculate n = p * q. Choose a small number e that is relatively prime to (p-1)*(q-1). This number is the public key. Calculate d, which is the multiplicative inverse of e modulo (p-1)*(q-1). This number is the private key. To encrypt a message M, convert it into a number m. Raise m to the power of e modulo n. The result is the encrypted message C. To decrypt the message C, raise it to the power of d modulo n. The result is the original message m.