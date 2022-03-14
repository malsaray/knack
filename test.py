from AGraph import  Graph
import Search

#INITIAL STATE:
initial_state = "1"

nodes= {
   "1":["2","3"],
   "2":["4","5","6"],
   "3":[],
   "4":[],
   "5":["7","8"],
   "6":["9"],
   "7":[],
   "8":[],
   "9":["10","11"] ,
   "10":["12"],
   "11":[],
   "12":["13"],
   "13":["14"],
   "14":[]
   }

labels= {
   "1":"S",
   "2":"A",
   "3":"M",
   "4":"B",
   "5":"C",
   "6":"I",
   "7":"D",
   "8":"E",
   "9":"J",
   "10":"K",
   "11":"L",
   "12":"L",
   "13":"M",
   "14":"G"    
   } 

#Test Breadth_First_Search
path = Search.Breadth_First_Search(nodes,initial_state)

#Test Depth_First_Search
#path =Search.Depth_First_Search(nodes,initial_state,[])

graph = Graph(nodes=nodes,labels=labels)
graph.Draw(path)

