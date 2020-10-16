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

    New features:
    1. Separated graph definition [Done]
    2. Separated function definition [Done]
    3. Separated solver definition [Done]
    4. Retire CVT, use Compound Node instead [Pending]
    5. Retire set const method, use solving equation set instead [Pending]
    6. RL based Solver [Pending]
    7. Predicated normalized by/align to Satori Ontology [Pending]
    8. More domain functions [Pending]
    9. Extends to structural predicates or merge function and predicate into a universal framework [Pending]
