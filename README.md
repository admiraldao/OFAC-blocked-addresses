# OFAC-blocked-addresses
Cleaned, checksummed, deduplicated ETH addresses from the OFAC SDN List. 

## About the SDN List

The US Treasury's Office of Foreign Assets Control ("OFAC") maintains a list of Specially Designated Nationals and other persons (which term includes both individuals and entities) whose property is blocked (the "SDN List"). The full SDN List is available at https://www.treasury.gov/ofac/downloads/sdnlist.txt


Recently, OFAC has been adding ETH wallet addresses to the SDN List. Unfortunately, these addresses are frequently duplicated, not checksummed, and in at least one case, impossible: https://cointelegraph.com/news/us-treasury-blacklisted-a-non-existent-eth-address-in-connection-with-alleged-russian-election-interference


## Pull Requests
Please keep the text file in numerically sorted order (0 thru 9, then A thru F) and checksum any new addresses (especially important given the inaccuracies in the SDN list). Include a link to the relevant detailed OFAC announcement, for instance: https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions/20211118

It is our intent to merge valid PRs within one week of submission.

### Using the Address Parser
For ease of updating, we've created a parser that scrapes the raw SDN file for Ethereum-address-like entities and checksums them. Running `python parser.py PATH_TO_SDN_FILE` will produce the sorted, checksum output.

## License
AdmiralDAO has a non-exclusive license to distribute this software package from Shipyard Software, its copyright holder.
