# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    A sample depth first search implementation is provided for you to help you understand how to interact with the problem.
    """
    # 调用util写好的stack生成了一个堆
    mystack = util.Stack()
    # 设置了起始状态 node action cost path
    startState = (problem.getStartState(), '', 0, [])
    # 把起点压进来
    mystack.push(startState)
    # 设置访问的空集合 不能有重复的
    visited = set()
    # 只要栈中有元素
    while mystack:
        # 将头部元素pop出 state就是头部元素
        state = mystack.pop()
        # 设置四样东西
        node, action, cost, path = state
        if node not in visited:
            # 将node设置为已访问
            visited.add(node)
            # 如果是需要的终点
            if problem.isGoalState(node):
                # 算path
                path = path + [(node, action)]
                break;
            # 设置后续的点们
            succStates = problem.getSuccessors(node)
            # 对于每一个继承者们的
            for succState in succStates:
                # 设置各种继承状态的数据
                succNode, succAction, succCost = succState
                # 生成一个新的state
                newstate = (succNode, succAction, cost + succCost, path + [(node, action)])
                # 继续深度往下搜索，将新状态设置为当前状态推入栈
                mystack.push(newstate)
    actions = [action[1] for action in path]
    del actions[0]
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    myQueue = util.Queue()
    startState = (problem.getStartState(), '', 0, [])
    # bestHeuristic = util.manhattanDistance((1,1), startState[0])
    # print(bestHeuristic)
    myQueue.push(startState)
    visited = set()
    print(problem.goal)
    # 根节点设置为已访问
    while myQueue:
        # 将根节点状态取出来
        state = myQueue.pop()
        node, action, cost, path = state
        # print(state)
        visited.add(node)
        # 如果根节点是我们想要的结果，则直接采取行动
        if problem.isGoalState(node):
            path = path + [(node, action)]
            # print(node)
            break;
        # 否则获取根节点的相邻继承节点
        succStates = problem.getSuccessors(node)
        # print(succStates)

        # 对每个相邻节点状态
        for succState in succStates:
            succNode, succAction, succCost = succState
            # 如果该继承节点从未访问过，则添加进访问集合，队列
            if succNode not in visited:
                visited.add(succNode)
                # 生成一个新状态，并放入队列中
                newstate = (succNode, succAction, cost + succCost, path + [(node, action)])
                myQueue.push(newstate)
    actions = [action[1] for action in path]
    del actions[0]
    return actions


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myQueue = util.PriorityQueue()
    startState = (problem.getStartState(), '', 0, [])
    myQueue.push(startState, 0)
    visited = set()
    while myQueue:
        headState = myQueue.pop()
        node, action, cost, path = headState
        visited.add(node)
        if problem.isGoalState(node):
            path = path + [(node, action)]
            print(cost)
            actions = [action[1] for action in path]
            del actions[0]
            return actions

        succStates = problem.getSuccessors(node)

        for succState in succStates:
            succNode, succAction, succCost = succState
            if succNode not in visited:
                visited.add(succNode)
                g = cost + succCost
                # 启发函数不一样会变化
                # h = heuristic(succNode,problem.goal)
                h = util.manhattanDistance(succNode, problem.goal)
                # print(problem.goal)
                f = g + h
                newstate = (succNode, succAction, g, path + [(node, action)])
                myQueue.push(newstate, f)


def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    startState = (problem.getStartState(), '', 0, [])
    while not problem.isGoalState(startState[0]):
        startState = improve(problem, startState)
    node, action, cost, path = startState
    # print(path)
    path = path + [(node, action)]
    actions = [action[1] for action in path]
    del actions[0]
    return actions


def improve(problem, state):
    myQueue = util.Queue()
    node0, action0, cost0, path0 = state
    myQueue.push(state)
    visited = set()
    while myQueue:
        state = myQueue.pop()
        node, action, cost, path = state

        if node not in visited:
            visited.add(node)

            if util.manhattanDistance(node, problem.goal) < util.manhattanDistance(node0, problem.goal):
                return state

            succStates = problem.getSuccessors(node)
            myQueue.push(state)
            for succState in succStates:
                succNode, succAction, succCost = succState
                if succNode not in visited:
                    newstate = (succNode, succAction, cost + succCost, path + [(node, action)])
                    myQueue.push(newstate)


def idaStarSearch(problem, heuristic=nullHeuristic):
    bound = util.manhattanDistance(problem.startState, problem.goal)
    startState = (problem.getStartState(), '', 0, [])

    while not problem.isGoalState(problem.startState):

        startState, t = iterative(problem, startState, bound)

        if t == -1:
            node, action, cost, path = startState
            path = path + [(node, action)]
            actions = [action[1] for action in path]
            del actions[0]
            return actions

        if t > 99999:
            node, action, cost, path = startState
            path = path + [(node, action)]
            actions = [action[1] for action in path]
            del actions[0]
            return actions

        bound = t


def iterative(problem, state, bound):
    myQueue = util.PriorityQueue()
    myQueue.push(state, bound)
    visited = set()
    while myQueue:
        headState = myQueue.pop()
        node, action, cost, path = headState
        g = cost
        h = util.manhattanDistance(node, problem.goal)
        f = g + h
        visited.add(node)

        if f > bound:
            return state, f

        if problem.isGoalState(node):
            return state, -1

        min = 99999

        succStates = problem.getSuccessors(node)
        for succState in succStates:
            succNode, succAction, succCost = succState
            if succNode not in visited:
                visited.add(succNode)
                newstate = (succNode, succAction, cost + succCost, path + [(node, action)])
                newstate, t = iterative(problem, newstate, bound)
                myQueue.push(newstate, t)
                if t == -1:
                    return newstate, -1
                if t < min:
                    min = t

        return state, min


def aStarForPi(problem, start, end):
    myQueue = util.PriorityQueue()
    startState = (start, '', 0, [])
    myQueue.push(startState, 0)
    visited = set()
    while myQueue:
        headState = myQueue.pop()
        node, action, cost, path = headState
        visited.add(node)
        if node == end:
            path = path + [(node, action)]
            actions = [action[1] for action in path]
            del actions[0]
            return actions, cost

        succStates = problem.getSuccessors(node)

        for succState in succStates:
            succNode, succAction, succCost = succState
            if succNode not in visited:
                visited.add(succNode)
                g = cost + succCost
                h = util.manhattanDistance(succNode, end)
                f = g + h
                newstate = (succNode, succAction, g, path + [(node, action)])
                myQueue.push(newstate, f)


def aStarForT(problem, start, end, beita):
    myQueue = util.PriorityQueue()
    startState = (start, '', 0, [])
    myQueue.push(startState, 0)
    visited = set()
    while myQueue:
        headState = myQueue.pop()
        node, action, cost, path = headState
        visited.add(node)
        if cost == beita:
            return node

        succStates = problem.getSuccessors(node)

        for succState in succStates:
            succNode, succAction, succCost = succState
            if succNode not in visited:
                visited.add(succNode)
                g = cost + succCost
                h = util.manhattanDistance(succNode, end)
                f = g + h
                newstate = (succNode, succAction, g, path + [(node, action)])
                myQueue.push(newstate, f)


def aStarForPi3(problem, start, end, goal, fakeGoal):
    myQueue = util.PriorityQueue()
    startState = (start, '', 0, [])
    myQueue.push(startState, 0)
    visited = set()
    while myQueue:
        headState = myQueue.pop()
        node, action, cost, path = headState
        visited.add(node)
        whatever, hGoal = aStarForPi(problem, node, goal)
        anything, hFakeGoal = aStarForPi(problem, node, fakeGoal)

        if node == end:
            path = path + [(node, action)]
            actions = [action[1] for action in path]
            del actions[0]
            return actions

        succStates = problem.getSuccessors(node)

        for succState in succStates:
            succNode, succAction, succCost = succState
            if succNode not in visited:
                visited.add(succNode)
                g = cost + succCost
                h = util.manhattanDistance(succNode, end)
                f = g + h
                if hGoal < hFakeGoal:
                    f = 2 * f
                newstate = (succNode, succAction, g, path + [(node, action)])
                myQueue.push(newstate, f)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ehc = enforcedHillClimbing
ida = idaStarSearch
