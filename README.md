# Rod Cutting

Rod cutting is a classic problem that can be efficiently solved using dynamic programming. The objective is to determine the optimal way to cut a steel rod to maximize profit. Each segment of the rod has a price based on its length, and there's no cost associated with making the cuts.

Given a rod of length n, we can divide it into k pieces, where k can range from 1 (no cut) up to n (cut into 1-inch segments). We're allowed to sell the rod whole or in parts, and the goal is to find the most profitable combination of cuts. Each piece has a length of $i_\alpha$, and piece lengths are associated with corresponding price values $p_{i_\alpha}$, presented in the following table. 

$$ 1 \leq k \leq n $$
$$ n = i_1 + i_2 + i_3 + \cdots + i_k $$
$$ r = p_{i_1} + p_{i_2} + p_{i_3} + \cdots + p_{i_k} $$
<div align="center">

| Length ($i$) | 1 | 2 | 3 | 4 | 5  | 6  | 7  | 8  | 9  | 10 |
|------------|---|---|---|---|----|----|----|----|----|----|
| Price ($p_i$) | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30 |

</div>

The rod with the length of $n$ can be split in $2^{n - 1}$ number of ways, and one of them is the optimal combination to have maximum revenue. How and in which combinations the pieces can be organized are presented below for the length of $3$ and $4$. 

$$n = 3 \rightarrow \\{ \\ (1, 1, 1), \\ (1, 2), \\ (2, 1), \\ (3) \\ \\}$$
$$n = 4 \rightarrow \\{ \\ (1, 1, 1, 1), \\ (1, 1, 2), \\ (1, 2, 1), \\ (2, 1, 1), \\ (1, 3), \\ (3, 1), \\ (2, 2), \\ (4) \\ \\}$$


When we try to solve this problem, the main intiution that we adapt in our minds is to think about all these possibilities and compute their corresponding revenues with respect to the price table. At this point, the combinations with same pieces produce same revenue; only the order of pieces are different. Hence, they can be filtered out:

$$n = 3 \rightarrow \\{ \\ (1, 1, 1), \\ (1, 2), \\ (3) \\ \\}$$
$$r_3 = max(p_{111}, p_{12}, p_3) \rightarrow r_3 = p_3 = 8$$

In this perspective, we actually calculate all cutting combinations and compare their revenues. This maximizes the revenue for the odd of length $3$. To generalize this idea, we can at first split the odd into $2$ arbitrary pieces, and continue to do the same operation over newly generated pieces. While doint that, we need to decide on the length of these pieces, and at some point, we need to stop. Since we dont know ahead of time which value of $i$ optimizes the revenue, we are obliged to consider all possible options. The critical point is the fact that we prioritize the maximization of the revenue for spliting into every two pieces. This defines a recursive structure where the solution of original problem requires the investigation of smaller problems from same type. 

$$r_n = max(p_n, \\ r_1 + r_{n-1}, \\ r_2 + r_{n-2}, \\ \cdots, \\ r_{n-1} + r_1)$$

Let's assume that you cut off the rod into two sub pieces. The optimal solution to our original rod actually incorporates the optimal solutions to those two sub pieces. To find it for both, we need to split again. This continues in a recursive manner. To summarize it, ***our approach is to maximize the revenue for every two pieces occuring after the cut off.*** This approach actually encapsulates our main intiution introduced before.

$$r_3 = max(p_{111}, p_{12}, p_3)$$
$$r_3 = max(r_1 + r_2, r_2 + r_1, p_3)$$

If we make a comparison between them, the term $r_1 + r_2$ can be decomposed into $r_1 + r_1 + r_1$, which refers to $p_{111}$, or results into $p_{12}$, where $r_2$ is not recursively expanded, instead replaced to be $p_2$. Whether $r_n$ terms will be decomposed (expanded) into more sub-problems or replaced as $p_n$ relies on profit maximixation criterion in recursive structure. 

In this approach, we recursively split the rod into two pieces, and how we split it relies on revenue maximization. This strategy guarantees the optimal solution, but poses so many recursive calls with same, repeated sub-cases. To simplify it, we instead split the rod into two pieces, but first piece will be fixed; recursive calls are maintained through only the second (right) piece. In this formulation, the optimal solution to the main problem is subject to the recursion of one subproblem, not two. This results in such a recursive structure. 

$$ r_n = max(p_i + r_{n-i} : \\ 1 \leq i \leq n)$$

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Rod-Cutting/blob/main/images/recursive_approaches.png" width="700" title="Recursive Structures">
</p>

## Recursive Top-down Implementation

In recursive implementation of `cut_rod()` function, we adapt the formulation $r_n = max(p_i + r_{n-i} : \\ 1 \leq i \leq n)$. This formulation is actually not a numerical calculation, instead a statement to define the general procedure. That is why, we can replicate the expression $p_i + r_{n - i}$ to define a set by iterating on index $i$ in a specific value range and apply `max()` operation on this set. In that case, we end up with the following expansion for $n = 5$:

$$ r_5 = max(p_1 + r_4, p_2 + r_3, p_3 + r_2, p_4 + r_1, p_5 + r_0)$$

In this expansion, the expression $p_i + r_{n-i}$ is abstractly instantiated, and max operation is applied on them. Nevertheless, in programming languages, we work with the values not the expressions. Hence, we need to compute each of these expressions individually, compare it with the next one by binary max operation, and store the result for the next compare. That is why, we define the variable `r`, which stores the result of $p_i + r_{n-i}$ for the next computation $p_{i+1} + r_{n-i+1}$. Technically, $r_{n-i}$ in $r_n = max(p_i + r_{n-i})$ corresponds to recursive function call. 

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Rod-Cutting/blob/main/images/implementation.png" width="700" title="Top-down Implementation">
</p>



