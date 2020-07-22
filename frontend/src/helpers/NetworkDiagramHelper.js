export const transformLocalNetworkToDiagram = (data)=> {
      let nodes = [];
      let edges = [];
      let routerIndex = 0; 

      data.map( (element,index) => {
        if( element == '192.168.1.1' ){
	  routerIndex = index;
	}
        nodes.push({ id: index+1, label: `IP: ${element['IP']}\n${element['MAC']}`, title: `HOST ${index+1}` }); 
      });
      let sizeNodes = nodes.length + 1

      let lastIndex = nodes.length;
      nodes.map( (node,index) => {
          if(index != routerIndex){
            edges.push({ from: index+1,to: routerIndex+1}); 
          }
      });

      console.log({nodes,edges});
      return {nodes,edges};
}
