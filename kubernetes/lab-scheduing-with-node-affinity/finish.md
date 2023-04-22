# Summary

In this lab, we learned how to use node affinity to schedule pods on specific nodes. We created a node with a label, and then created pods with node affinity rules that ensured they were scheduled on nodes with specific labels. We also created a pod with a node anti-affinity rule that ensured it was not scheduled on a node with a specific label. Finally, we created a pod with multiple node affinity rules that ensured it was scheduled on a node with labels that matched all of the rules.
