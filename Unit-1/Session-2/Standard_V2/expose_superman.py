"""
Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.
"""


def expose_superman(trust, n):
    # trust_map = {}
    trust_set = set()
    for pop in trust:
        # person1, person2 = pop[0], pop[1]
        person2 = pop[1]

        # trust_map[person1] = trust_map.get(person1, 0) + 1

        trust_set.add(person2)

    if len(trust_set) > 1:
        return -1
    else:
        return trust_set.pop()


n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))
