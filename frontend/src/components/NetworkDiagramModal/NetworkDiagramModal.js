import React, { useEffect, useState , Fragment } from "react";
import Graph from "react-graph-vis";

import { getDataFromLocalNetwork } from "../../services/localNetworkService";
import { transformLocalNetworkToDiagram } from "../../helpers/NetworkDiagramHelper";

const NetworkDiagramModal = () => {
  const [graph, setGraph] = useState(null);

  const options = {
    layout: {
      hierarchical: true
    },
    edges: {
      color: "red"
    },
    height: "300px"
  };

  const events = {
    select: function(event) {
      var { nodes, edges } = event;
    }
  };

  async function getDataLocalNetwork() {
    let result = await getDataFromLocalNetwork();
    let newData = transformLocalNetworkToDiagram(result.data);
    console.log(newData);
    setGraph(newData);
  }

  useEffect(() => {
    getDataLocalNetwork();
  }, []);

  return (
    <Fragment>
      {
    	graph != null &&(
	<Graph
        graph={graph}
        options={options}
        events={events}
        getNetwork={network => {}}
    	/> 
       )}	
    </Fragment>
  );
};

export default NetworkDiagramModal;
