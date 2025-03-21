# Rod Cutting

Rod cutting is a classic problem that can be efficiently solved using dynamic programming. The objective is to determine the optimal way to cut a steel rod to maximize profit. Each segment of the rod has a price based on its length, and there's no cost associated with making the cuts.

Given a rod of length n, we can divide it into k pieces, where k can range from 1 (no cut) up to n (cut into 1-inch segments). We're allowed to sell the rod whole or in parts, and the goal is to find the most profitable combination of cuts. Each piece has a length of $i_\alpha$, and piece lengths are associated with corresponding price values $p_{i_\alpha}$, presented in the following table. 

$$ 1 \leq k \leq n $$
$$ n = i_1 + i_2 + i_3 + \cdots + i_k $$

<div align="center">

| Length ($i$) | 1 | 2 | 3 | 4 | 5  | 6  | 7  | 8  | 9  | 10 |
|------------|---|---|---|---|----|----|----|----|----|----|
| Price ($p_i$) | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30 |

</div>