# Mixed-Integer-Linear-Programming
A computational optimization project towards the goal of gerrymandering the results of a hypothetical election in the UK.


We seek to determine the best possible division of 14 shires on agiven map into 5 constituencies, each composed of one or more shires.
We do so towards the goal of maximising the number of such constituencies in which “Joris Bohnson” wins a majority of the total votes inside this constituency.
As a result, he is able to send the maximum possible of representatives to Parliament.

Within each shire, the total number of voters and the total number of votes forJoris are already set.
As such, we need only draw the boundaries upon the mapin order to secure representatives.
We do so subject to constraints regarding what makes a “valid” constituency, and the desire to maintain appearances by not allowing shire 10 to become a singleton (one shire) constituency.
