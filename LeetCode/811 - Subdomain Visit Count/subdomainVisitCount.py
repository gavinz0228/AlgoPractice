from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        lookup = {}
        for count_domain in cpdomains:
            cd = count_domain.split(" ")
            count = int(cd[0])
            domains = cd[1].split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                lookup[domain] = lookup.get(domain, 0) + count
        return [str(c) + " " + d for d, c in lookup.items()]
