class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        adj_dict = {i: n for i, n in enumerate(graph)}
        paths = []
        end = len(graph)-1
        current_node = 0
        current_path = [0]
        q = [(current_node, n) for n in adj_dict[current_node]]
        while True:

            if len(q) == 0:
                break

            current_root, current_node = q.pop()

            while current_root != current_path[-1]:
                    current_path.pop()

            current_path.append(current_node)
            q.extend([(current_node, n) for n in adj_dict[current_node]])

            if current_node == end:
                paths.append([n for n in current_path])
                current_path.pop()

        return paths
