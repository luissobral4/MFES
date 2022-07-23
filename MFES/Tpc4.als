// Representação entidade nodo
sig Node {

	var edge : set Node

}
one sig Atual {

	var atual : one Node

}

fact init{

	//O grafo não tem lacetes

 	always all n: Node | n not in n.edge

	//O grafo não-orientado

	always all n1,n2: Node | (n1 != n2 and n1 in n2.edge) implies n2 in n1.edge

       //Grafo convexo

	all n : Node | Node in n.*edge

	//cada nodo tem par num de adjacentes (# e rem)

	all n : Node | rem[#n.edge,2] = 0

}

pred remAresta [n1 : Node, n2 : Node]{

	// n1 tem de ser atual

	Atual.atual = n1

	// n2  vizinho do n1

	n2 in n1.edge


	// n1-n2 nao é cut edge

	// ou n1 só tem 1 vizinho

	n1 in n2.^(edge') or #n1.edge=1

	// efeito

	// n2 passa a ser atual

	Atual.atual' = n2
	// remove n1-n2

	n1.edge' = n1.edge - n2

	n2.edge' = n2.edge - n1


		//frames

	//nodos não alterados ficam iguais

	all n : Node - n1 - n2 | n.edge' = n.edge

}
pred nop {

	edge' = edge

	Atual.atual' = Atual.atual

}


fact Traces {

	always{

		nop or

 			( some n1,n2 : Node | remAresta[n1,n2] )

	}

}


run Exemplo {} for exactly 5 Node
