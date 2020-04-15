<h2 align="center">
    <img src="assets/esoterica.svg" style="background-color:rgba(0,0,0,0);" height="200" alt="esoterica"></a>
    <br>esoterica<br>
</h2>
<center>the wackiest, pessimal of algorithms that you won't ever need</center>

## algorithms

### bogosort

To sort a list, just shuffle it till entropy finds its way to order. Its name is a portmanteau of the words bogus and sort.

[ [View Source](https://github.com/say4n/esoterica/blob/master/bogosort.py) ]
[ [Description](https://en.wikipedia.org/wiki/Bogosort) ]

### intelligent design sort

Also known as "Assumption Sort": Assume the list is sorted, return!
The probability of the original input list being in the exact order it's in is 1/(n!). There is such a small likelihood of this that it's clearly absurd to say that this happened by chance, so it must have been consciously put in that order by an intelligent Sorter. Therefore it's safe to assume that it's already optimally Sorted in some way that transcends our naïve mortal understanding of "ascending order". Any attempt to change that order to conform to our own preconceptions would actually make it less sorted.

[ [View Source](https://github.com/say4n/esoterica/blob/master/idsort.py) ]
[ [Description](https://www.dangermouse.net/esoteric/intelligentdesignsort.html) ]

### sleep sort

To sort a list, it spawns a coroutine for each element that sleeps for the element's value, in seconds (times a multiplier for reducing wait time). The order the coroutines print in will be in sorted order, _almost always_&trade;.

[ [View Source](https://github.com/say4n/esoterica/blob/master/sleepsort.py) ]
[ [Description](https://www.reddit.com/r/algorithms/comments/9p4z8m/what_are_some_esoteric_algorithm_that_you_know/e7z4adl/) ]

## author

Sayan Goswami (@say4n)
