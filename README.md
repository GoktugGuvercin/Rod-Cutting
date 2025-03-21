# Rod Cutting

Rod cutting is a simple problem that is solvable by dynamic programming. We try to decide on how we split steel rods. We cut these rods and sell them. We do not need to pay anything to cut the rods, but the prices of rod splits depend on their length. At this point, we aim to maximize our income, so we try to find the best split. 

Rod length is denoted as n, and we split the rods into k number of pieces. We don't have to cut the rods; we are allowed to preserve them as a whole for selling. It is also possible to split the rods into 1-inch pieces. In that case, the following two formulas become valid. 