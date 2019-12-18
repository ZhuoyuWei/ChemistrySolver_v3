# ChemistrySolver_v3
ChemistrySolver_v3

There are mainly three parts of this system:

    1. model, the graph data structure and graph action.

        The structure includes the definition of:

            a. Node, including its extend CVT

            b. Edge, can be property, relation, or other predicate

        The action set includes:

            a. build a situated graph

            b. _update_graph(self)

            c. split_node(self,node)

            d. merge_nodes(self,nodes)

            e. infer_one(self,func, in_edges,out_edges)

            f. infer_one_from_(funcs): solving math equation set ?

    2. solving (also independent with chemistry ?), the algorithm of solving problem, which could be DFS, RL or other algorithm

    3. func, all functions implement

The ideal status is these three parts are independent/decoupling/transparent with each other.