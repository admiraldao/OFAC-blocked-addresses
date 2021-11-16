# OFAC-blocked-addresses
Cleaned, checksummed, deduplicated ETH addresses from the OFAC SDN List.

## About the SDN List

The US Treasury's Office of Foreign Assets Control ("OFAC") maintains a list of Specially Designated Nationals and other persons (which term includes both individuals and entities) whose property is blocked (the "SDN List"). The SDN List is available at https://www.treasury.gov/ofac/downloads/sdnlist.txt


Recently, OFAC has been adding ETH wallet addresses to the SDN List. Unfortunately, these addresses are frequently duplicated, not checksummed, and in at least one case, impossible: https://cointelegraph.com/news/us-treasury-blacklisted-a-non-existent-eth-address-in-connection-with-alleged-russian-election-interference


## Pull Requests
Please keep the text file in numerically sorted order and checksum any included addresses (especially important given the inaccuracies in the SDN list)

Include a link to the relevant OFAC announcement.