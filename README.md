# whereis
Python program that mines whois databases for a organisation name/keyword and returns CIDR net-ranges for further investigation.

Currently the program mines:
 * whois.arin.net
 * whois.ripe.net
 * whois.afrinic.net
 * whois.apnic.net

Ideal for red-teaming and bug-bounty hunters

## Example 1 - example keyword
```
$ ./whereis.py example
23.30.98.184/29
76.12.11.152/29
76.12.110.96/29
64.136.255.92/30
```
Manual check of each CIDR to confirm **example** keyword is actually returned:
```
NetRange:       23.30.98.184 - 23.30.98.191
CIDR:           23.30.98.184/29
NetName:        IMPORTEXAMPLES

NetRange:       76.12.11.152 - 76.12.11.159
CIDR:           76.12.11.152/29
NetName:        EXAMPLEESSAYS

NetRange:       64.136.255.92 - 64.136.255.95
CIDR:           64.136.255.92/30
NetName:        CTSC-S3362
NetHandle:      NET-64-136-255-92-1
Parent:         CTSTELECOM-BLK-1 (NET-64-136-224-0-1)
NetType:        Reassigned
OriginAS:       
Customer:       Digital Example (C06469865)
```
## Example 2 - encapsulated string
```
$ ./whereis.py "private bank"
173.8.132.248/29
12.130.41.144/29
216.47.232.224/28
...
```
manual check:
```
NetRange:       173.8.132.248 - 173.8.132.255
CIDR:           173.8.132.248/29
NetName:        BORELPRIVATEBANKTRUS
```
