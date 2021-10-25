####### PageRank
import networkx as nx
import matplotlib.pyplot as plt
import random

### 创建图
Graph = nx.DiGraph() # Create an empty graph structure (a “null graph”) with no nodes and no edges.
Graph.add_nodes_from(range(0,100))
for i in range(200):
    j = random.randint(0,100) # 随机产生0-100整数
    k = random.randint(0,100)
    Graph.add_edge(k,j)
nx.draw(Graph, with_labels=True)
plt.show()

### 计算PageRank
pr = nx.pagerank(Graph, max_iter=100, alpha=0.01)
print(pr)
max(pr.values())

### PR值最大的节点
import operator
max(pr.items(),key=operator.itemgetter(1))[0] # itemgetter用于获取对象的哪些位置的数据，参数即为代表位置的序号值; 获取dic中最大值的节点是谁

sum(pr.values())

min(pr.values())
































































