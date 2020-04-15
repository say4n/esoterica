# esoterica

the wackiest of algorithms that you won't ever need, esoterica, is a repository for all things pessimal

## algorithms

### bogosort

To sort a list, just shuffle it till entropy finds its way to order. Its name is a portmanteau of the words bogus and sort.

[View Source](https://github.com/say4n/esoterica/blob/master/bogosort.py)

### intelligent design sort

Also known as "Assumption Sort": Assume the list is sorted, return!
The probability of the original input list being in the exact order it's in is 1/(n!). There is such a small likelihood of this that it's clearly absurd to say that this happened by chance, so it must have been consciously put in that order by an intelligent Sorter. Therefore it's safe to assume that it's already optimally Sorted in some way that transcends our naïve mortal understanding of "ascending order". Any attempt to change that order to conform to our own preconceptions would actually make it less sorted.

[View Source](https://github.com/say4n/esoterica/blob/master/idsort.py)

### sleep sort

To sort a list, it spawns a coroutine for each element that sleeps for the element's value, in seconds (times a multiplier for reducing wait time). The order the coroutines print in will be in sorted order, _almost always_&trade;.

[View Source](https://github.com/say4n/esoterica/blob/master/sleepsort.py)

## author

Sayan Goswami (@say4n)
