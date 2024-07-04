var pentagonPyramidModel = {
  "vertexPositions" : new Float32Array([
    // Podstawa pięciokąta (leżąca na płaszczyźnie XZ)
    0.0, -9.0, -10.0,  // Wierzchołek 0
    9.51, -9.0, -3.09,  // Wierzchołek 1
    5.876, -9.0, 8.09,  // Wierzchołek 2
    -5.876, -9.0, 8.09,  // Wierzchołek 3
    -9.51, -9.0, -3.09,  // Wierzchołek 4
    0.0, 0.0, 0.0   // Wierzchołek szczytowy piramidy
  ]),
  
  "vertexNormals" : new Float32Array([
    // Normalne wektory dla wierzchołków podstawy
    0.0, -1.0, 0.0, // Wierzchołek 0
    0.0, -1.0, 0.0, // Wierzchołek 1
    0.0, -1.0, 0.0, // Wierzchołek 2
    0.0, -1.0, 0.0, // Wierzchołek 3
    0.0, -1.0, 0.0, // Wierzchołek 4

    // Normalne wektory dla wierzchołka szczytowego
    0.0, 1.0, 0.0  // Wierzchołek 5
  ]),
  
  "vertexTextureCoords" : new Float32Array([
    // Współrzędne tekstury dla wierzchołków podstawy
    0.5, 0.0, // Wierzchołek 0
    1.0, 0.0, // Wierzchołek 1
    1.0, 0.5, // Wierzchołek 2
    0.5, 1.0, // Wierzchołek 3
    0.0, 1.0, // Wierzchołek 4
    
    // Współrzędne tekstury dla wierzchołka szczytowego
    0.5, 0.5  // Wierzchołek 5
  ]),
  
  "indices" : new Uint16Array([
    // Ściany boczne piramidy
    0, 1, 5, // Ściana 1
    1, 2, 5, // Ściana 2
    2, 3, 5, // Ściana 3
    3, 4, 5, // Ściana 4
    4, 0, 5, // Ściana 5
    
    // Podstawa piramidy
    0, 1, 2, // Trójkąt 1
    2, 3, 4, // Trójkąt 2
    4, 0, 1  // Trójkąt 3
  ])
};
